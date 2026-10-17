# ACBr Python

Cliente Python independente de Django, Flask ou outro framework para o worker
nativo público ACBr NF-e/NFC-e. **Versão alpha 0.1.0a3, sem homologação fiscal.**
O pacote é instalado com pip e importa como `acbr`; não há dependências Python
de execução nem necessidade de Node.js ou PHP.

O SDK reaproveita o worker 0.2.0 e o contrato de `cosmemilton/acbr-node`, sem
reimplementar cálculos, assinatura ou regras fiscais. A API pública oferece
`gerar_xml`, `validar`, `assinar`, `transmitir`, `consultar`, `cancelar`,
`inutilizar` e a interface experimental `recuperar_xml`. Todas as operações
que podem acessar a SEFAZ exigem `allow_network=True` explícito por chamada.

O runtime fixado é **0.2.1**: ele preserva os executáveis e o contrato da
0.2.0 e completa os textos de licença que acompanham a distribuição nativa.

Este repositório contém o SDK público reutilizável. Aplicações consumidoras,
inclusive uma integração privada, instalam o pacote e fornecem sua própria
configuração em execução. Dados de empresas, certificados e credenciais da
aplicação consumidora não fazem parte do SDK.

## Plataformas e instalação

O cliente tem como alvo CPython **3.11 a 3.14**, Windows x64 e Linux x64 com
glibc. O runtime Linux de referência foi construído para Ubuntu 24.04.
A matriz da CI cobre essas versões nos dois sistemas; uma matriz configurada
não significa que uma execução tenha passado. macOS, ARM, Python 32 bits,
Alpine/musl e outras implementações Python não fazem parte deste MVP.

Crie um ambiente virtual:

```console
python -m venv .venv
```

Ative o ambiente (`.venv\Scripts\Activate.ps1` no PowerShell ou
`source .venv/bin/activate` no bash). Para instalar pelo PyPI quando a versão
estiver disponível:

```console
python -m pip install acbr-python==0.1.0a3
python -m acbr ajuda Ide.cUF
python -m acbr ajuda TProd
```

Para desenvolvimento ou antes da primeira publicação, instale na cópia
deste repositório com `python -m pip install .`; os comandos de ajuda são iguais.

Esses comandos de ajuda são offline e não exigem runtime. Para as operações
nativas, a instalação é uma etapa explícita, separada de `pip install`:

```console
python -m acbr runtime install --directory .runtime
python -m acbr doctor --directory .runtime/runtime
```

O instalador escolhe o arquivo original 0.2.1 para o sistema e arquitetura
atuais. Antes de extrair, verifica tamanho e SHA-256 fixados no pacote; depois
confere os arquivos do inventário. Não executa scripts de instalação npm.
Fontes, licenças, schemas, serviços e bibliotecas acompanham o runtime.
Para uma instalação sem download, obtenha previamente o `.tgz` correspondente
ao pin e use `--archive caminho/arquivo.tgz` no mesmo comando de instalação.

Use uma pasta de runtime sob seu controle e informe o caminho `runtime`
retornado pelo instalador ao cliente. `doctor` verifica a instalação; não
consulta a SEFAZ nem atesta validade fiscal de documentos.

## Uso com documento sintético

A fixture versionada é sintética, sem valor fiscal. O exemplo abaixo gera
XML localmente; não transmite documento nem usa certificado:

```python
import json
from pathlib import Path

from acbr import Configuracao, Documento, Emissor

dados = json.loads(Path("tests/fixtures/documento.json").read_text("utf-8"))
config = Configuracao(cnpj="11222333000181", uf="CE", modelo=55, ambiente=2)

with Emissor(config, runtime_directory=Path(".runtime/runtime"), timeout=120) as emissor:
    resultado = emissor.gerar_xml(Documento(dados))
    print(resultado.sucesso, resultado.estado, resultado.codigo)
    if resultado.sucesso and resultado.xml is not None:
        validacao = emissor.validar(resultado.xml)
        print(validacao.sucesso, validacao.codigo)
```

Um XML sem assinatura pode falhar no schema que exige assinatura. A validação
estrutural Python e a validação local nativa não substituem homologação nem
autorização fiscal. Nenhum teste desta entrega usa certificado A1 de contribuinte,
documentos privados ou tráfego fiscal.

## Modelos, campos e tipos

O contrato compartilhado fornece modelos gerados e ajuda de campos/tipos:

```console
python -m acbr ajuda 'Det[].Prod.vProd'
python examples/ajuda.py TProd
python tools/generate_models.py --check
```

Maiúsculas e minúsculas seguem o contrato ACBr. Decimais são strings, como
`"10.00"`, para evitar a perda de precisão de `float`. Datas seguem o formato
civil do contrato e campos omitidos não recebem defaults fiscais inventados.
Consulte a ajuda do tipo antes de construir um documento.

## Prazos, cancelamento e encerramento

Cada operação usa seu próprio processo nativo, com JSON pelo stdin/stdout,
sem shell. O cliente limita bytes, drena os pipes e impõe prazo à comunicação.
`timeout` é expresso em segundos; o limite padrão `max_bytes` é 8 MiB.
Use o emissor como context manager ou chame `fechar()` ao terminar.
Uma instância aceita uma operação por vez; chamadas concorrentes recebem
`EMISSOR_OCUPADO`, sem fila implícita. O prazo cobre comunicação e execução
do filho; a verificação prévia dos arquivos tem seu próprio custo.

As operações aceitam `cancel=evento`, com `evento` do tipo `threading.Event`.
Definir o evento solicita cancelamento cooperativo durante a chamada; não
reverte uma operação que já tenha ocorrido no serviço remoto. O cliente não
repete chamadas automaticamente. Um prazo excedido ou uma resposta perdida
não prova que uma operação remota deixou de acontecer.

Resultados e erros têm tipos próprios; `ResultadoFiscal.xml` exige acesso
explícito ao conteúdo. Não registre XML, PFX, senhas nem a carga completa de
uma chamada. As representações padrão ocultam conteúdo sensível.

Para registrar o início observado de um envio na aplicação consumidora,
`Emissor(..., ao_iniciar_envio=callback)` entrega ao callback um `EventoEnvio`
imutável, com identificador de correlação e comando, sem dados fiscais.
O evento apenas observa o marcador do worker para `transmitir`, `cancelar`
ou `inutilizar`; não confirma aceitação, não fornece idempotência e não
garante persistência antes do envio. Se o callback falhar, o resultado pode
ser incerto e não há repetição automática.

## Operações públicas e acesso à rede

| Método | Entrada | Rede fiscal |
| --- | --- | --- |
| `gerar_xml` | `Documento` ou dicionário do contrato | Não |
| `validar` | XML em texto | Não |
| `assinar` | XML em texto, com A1 na configuração | Não |
| `transmitir` | XML assinado | Exige `allow_network=True` |
| `consultar` | `Consulta` com chave e recibo opcional | Exige `allow_network=True` |
| `cancelar` | `Cancelamento` | Exige `allow_network=True` |
| `inutilizar` | `Inutilizacao` | Exige `allow_network=True` |
| `recuperar_xml` | XML assinado, interface experimental | Exige `allow_network=True` |

`Consulta`, `Cancelamento` e `Inutilizacao` são dataclasses de entrada
exportadas por `acbr`. Todas as operações retornam `ResultadoFiscal` e
aceitam `cancel=threading.Event()`. Os métodos de rede também requerem A1 na
configuração. O bloqueio é aplicado antes de iniciar uma chamada ao worker;
selecionar `ambiente=2` não libera rede por si só.

O cliente não oferece repetição automática nem opções de lote ou modo
assíncrono. A transmissão segue o comportamento síncrono do worker fixado.
A CLI oferece somente ajuda e gestão do runtime: não há comandos CLI para
transmitir, consultar, cancelar ou inutilizar documentos.

Veja as assinaturas, tipos, resultados e erros na [referência da API](docs/api.md).
As operações de rede são verificadas por protocolo simulado; nenhuma delas
foi exercitada contra a SEFAZ nesta entrega.

### Recuperação de XML: interface experimental

`recuperar_xml(xml_assinado)` requer `CertificadoA1(pfx: bytes, senha: str)` na
configuração e pode consultar a SEFAZ para reconstruir o XML processado.
A chamada só permite rede com `allow_network=True` explícito; o padrão a
bloqueia. O cliente envia o certificado pelo stdin, nunca por argumentos.

Nesta entrega, essa interface só é verificada por testes de protocolo com
worker simulado e materiais sintéticos. Não há teste de recuperação na SEFAZ
nem uso de certificado de contribuinte. A implementação não deve ser tratada
como homologada. Não é disponibilizado exemplo que realize essa consulta.

## Desenvolvimento e verificação

```console
python -m pip install -e .
python -m unittest discover -s tests -v
python tools/generate_models.py --check
python -m pip install build
python -m build
```

A suíte padrão usa fixtures e workers simulados e dispensa internet após a
instalação das ferramentas. O teste nativo é opt-in: defina
`ACBR_TEST_RUNTIME` para o caminho de uma instalação verificada e execute
`python -m unittest discover -s tests -p test_native.py -v`. Instale antes
`python -m pip install "cryptography>=46"`: essa dependência é somente dos
testes e cria um A1 sintético efêmero; ela não é dependência de execução do
SDK. O smoke cobre geração, assinatura e validação locais pela API pública,
rejeição de assinatura alterada e entrada inválida, sem operações fiscais
remotas. A CI instala explicitamente os runtimes Windows e Linux e essa
dependência de teste, além da matriz de testes offline e build.
Não há publicação automática nem credenciais de publicação na CI.

Veja [arquitetura e escopo](docs/architecture.md) para as decisões do SDK.

## Licenças e fontes

Cliente e contrato: LGPL-2.1-or-later; consulte [LICENSE](LICENSE) e
[NOTICE](NOTICE). O wheel não incorpora binários nativos. A instalação
preserva fontes e licenças dos arquivos originais do runtime; os componentes
nativos mantêm as respectivas licenças e exceções.

Referências oficiais consultadas:

- [ACBr Node e seu worker](https://github.com/cosmemilton/acbr-node), origem 0.2.0 e distribuição nativa fixada 0.2.1.
- [ACBr PHP](https://github.com/cosmemilton/acbr-php), referência de adaptação.
- [Guia PyPA para pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
- [Dados de pacote no setuptools](https://setuptools.pypa.io/en/latest/userguide/datafiles.html).

Este é um projeto independente, sem certificação oficial pelo Projeto ACBr.
