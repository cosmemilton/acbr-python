"""A1 sintético efêmero para testes locais. Nunca transmitir documentos desta fixture."""
from datetime import datetime, timedelta, timezone


def synthetic_a1(cnpj="11222333000181", *, expired=False, password="SYNTHETIC-OFFLINE-ONLY"):
    # Test-only dependency. The SDK itself has no third-party Python dependency.
    from cryptography import x509
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa
    from cryptography.hazmat.primitives.serialization import pkcs12
    from cryptography.x509.oid import ExtendedKeyUsageOID, NameOID, ObjectIdentifier
    from acbr import CertificadoA1

    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    name = x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "ACBR PYTHON SYNTHETIC:" + cnpj),
        x509.NameAttribute(NameOID.COUNTRY_NAME, "BR"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, "SYNTHETIC OFFLINE TEST"),
    ])
    clock = datetime.now(timezone.utc)
    # The ICP-Brasil CNPJ otherName is a DER UTF8String, as in upstream fixtures.
    encoded = cnpj.encode("ascii")
    other = x509.OtherName(ObjectIdentifier("2.16.76.1.3.3"), b"\x0c" + bytes([len(encoded)]) + encoded)
    cert = (x509.CertificateBuilder().subject_name(name).issuer_name(name).public_key(key.public_key())
            .serial_number(x509.random_serial_number()).not_valid_before(clock - timedelta(days=2))
            .not_valid_after(clock + timedelta(days=-1 if expired else 30))
            .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
            .add_extension(x509.KeyUsage(digital_signature=True, content_commitment=True, key_encipherment=True,
                                        data_encipherment=False, key_agreement=False, key_cert_sign=False,
                                        crl_sign=False, encipher_only=None, decipher_only=None), critical=True)
            .add_extension(x509.ExtendedKeyUsage([ExtendedKeyUsageOID.CLIENT_AUTH]), critical=False)
            .add_extension(x509.SubjectAlternativeName([other]), critical=False)
            .sign(key, hashes.SHA256()))
    data = pkcs12.serialize_key_and_certificates(b"SYNTHETIC OFFLINE ONLY", key, cert, None,
                                              serialization.BestAvailableEncryption(password.encode("ascii")))
    return CertificadoA1(data, password)
