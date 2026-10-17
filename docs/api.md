# API pública — 0.1.0a2

O pacote importa como `acbr` e funciona sem Django, Flask, Node.js ou PHP.
Esta referência descreve a API Python sobre o worker ACBr 0.2.0 original.
Não há homologação fiscal nem teste de rede contra a SEFAZ nesta entrega.

## Configuração e ciclo de vida

```python
from acbr import (
    AcbrError,
    Cancelamento,
    CertificadoA1,
    Configuracao,
    Consulta,
    Csc,
    Documento,
    Emissor,
    EventoEnvio,
    Inutilizacao,
    ResultadoFiscal,
)
```

`Configuracao(cnpj, uf, modelo=55, ambiente=2, certificado=None, csc=None)`
recebe CNPJ como texto, UF em maiúsculas, modelo 55 ou 65 e ambiente 1 ou 2.
Não descobre credenciais nem lê arquivos de certificado automaticamente.
`CertificadoA1(pfx: bytes, senha: str)` recebe o conteúdo PFX em memória;
`Csc(id: str, valor: str)` representa a configuração CSC para NFC-e.
Certificado e CSC devem vir da aplicação consumidora e não devem ser
versionados ou registrados em logs.

```python
Emissor(
    config: Configuracao,
    *,
    runtime_directory: Path | str,
    timeout: float = 120,
    max_bytes: int = 8 * 1024 * 1024,
    ao_iniciar_envio: Callable[[EventoEnvio], None] | None = None,
)
```

O diretório deve ser uma instalação verificada do runtime, normalmente
`destino/runtime` após `python -m acbr runtime install --directory destino`.
O prazo é expresso em segundos. O limite de bytes controla a comunicação
com o processo filho. Uma instância executa uma operação por vez e rejeita
concorrência com `EMISSOR_OCUPADO`; não há fila implícita.

Use `with Emissor(...) as emissor:` ou finalize com `emissor.fechar()`.
Cada operação inicia seu próprio worker e retorna `ResultadoFiscal`.
O fechamento é explícito e não inicia uma operação fiscal.

`ao_iniciar_envio` recebe um `EventoEnvio` imutável quando o cliente observa
o marcador de envio do worker para `transmitir`, `cancelar` ou `inutilizar`.
O evento contém `id` de correlação UUID e `comando`, sem dados fiscais ou
stdout bruto. A aplicação consumidora pode persistir esse marcador, mas o
callback não autoriza o envio, não confirma aceitação, não fornece
idempotência e não garante gravação anterior ao envio remoto. Se ele lançar
uma exceção, o resultado pode permanecer incerto e não há nova tentativa
automática.

## Entradas tipadas

| Tipo | Campos | Uso |
| --- | --- | --- |
| `Documento` | Dicionário com os nomes e tipos do contrato ACBr | Geração do XML |
| `Consulta` | `chave`, `recibo=None` | Consulta por chave com recibo opcional |
| `Cancelamento` | `chave`, `protocolo`, `justificativa` | Solicitação de cancelamento |
| `Inutilizacao` | `ano`, `serie`, `numero_inicial`, `numero_final`, `justificativa` | Solicitação de inutilização |

As entradas de operação são dataclasses com validação estrutural. Elas não
atestam autorização, prazo legal, situação do documento ou elegibilidade do
pedido; as regras fiscais continuam no worker e no serviço correspondente.
Chaves, recibos e protocolos são texto, preservando zeros à esquerda. A chave
tem 44 dígitos; recibo e protocolo têm 15 dígitos. `Consulta(chave, recibo=None)`
sempre exige chave, inclusive quando há recibo: o worker 0.2.0 não oferece
consulta somente por recibo.

`Cancelamento(chave, protocolo, justificativa)` exige justificativa entre
15 e 255 bytes UTF-8, conforme o limite do worker nativo.
`Inutilizacao(ano, serie, numero_inicial, numero_final,
justificativa)` recebe ano entre 0 e 99, série entre 0 e 999 e numeração de
1 a 999999999, com fim maior ou igual ao início. Ano é o valor de dois
dígitos; não informe o ano completo. Esses campos numéricos são inteiros,
e a justificativa tem o mesmo limite de 15 a 255 bytes UTF-8.

`Documento(dados)` valida o dicionário contra o contrato compartilhado.
Os modelos gerados em `acbr.models` ajudam a descrever entradas e saídas
tipadas. Campos ACBr são sensíveis a maiúsculas/minúsculas. Decimais são
strings com ponto; datas são strings civis nos formatos aceitos pelo contrato.
Campos omitidos continuam omitidos.

## Operações locais

As assinaturas abaixo são referências; não são um roteiro de execução fiscal.
O parâmetro `cancel` aceita `threading.Event | None` e tem padrão `None`.

```python
emissor.gerar_xml(documento: Documento | dict, *, cancel=None) -> ResultadoFiscal
emissor.validar(xml: str, *, cancel=None) -> ResultadoFiscal
emissor.assinar(xml: str, *, cancel=None) -> ResultadoFiscal
```

`gerar_xml` envia o documento estruturado ao worker. `validar` usa o fluxo
de validação local nativo. Um XML sem assinatura pode ser rejeitado pelo
schema; isso não é falha de transporte. `assinar` requer A1 na configuração e
produz assinatura local. Nenhuma dessas três operações exige autorização de
rede fiscal. O comportamento criptográfico vem do worker original.

## Operações que podem usar rede

```python
emissor.transmitir(xml_assinado: str, *, allow_network=False, cancel=None) -> ResultadoFiscal
emissor.consultar(consulta: Consulta, *, allow_network=False, cancel=None) -> ResultadoFiscal
emissor.cancelar(cancelamento: Cancelamento, *, allow_network=False, cancel=None) -> ResultadoFiscal
emissor.inutilizar(inutilizacao: Inutilizacao, *, allow_network=False, cancel=None) -> ResultadoFiscal
emissor.recuperar_xml(xml_assinado: str, *, allow_network=False, cancel=None) -> ResultadoFiscal
```

Cada chamada exige `allow_network=True` explícito e certificado A1 na
configuração. A omissão ou outro valor de autorização bloqueia a operação
antes de iniciar o worker. O ambiente de homologação (`ambiente=2`) também
usa rede real; ele não substitui esse consentimento por chamada.

`transmitir` recebe XML assinado. O SDK não oferece parâmetros para lote,
modo assíncrono ou número de tentativas: usa o comportamento síncrono e uma
tentativa do worker fixado. Não há assinatura automática nessa chamada.
`consultar` recebe os dados de consulta; `cancelar` e `inutilizar` recebem
suas respectivas dataclasses. Esses métodos podem produzir efeitos fiscais
quando a aplicação os chama com rede autorizada.

`recuperar_xml` é experimental: consulta a situação do XML assinado para
reconstruir o XML processado. Não é um método genérico de download de XML e
não retransmite o documento. Seu protocolo é testado com worker simulado;
não houve recuperação na SEFAZ nesta entrega.

Não há comandos CLI correspondentes a essas operações. A CLI somente oferece
ajuda de contrato, instalação do runtime e diagnóstico local.

## Resultados e erros

`ResultadoFiscal` expõe `sucesso`, `estado`, `codigo`, `c_stat` e
`diagnostico`. A propriedade `xml` fornece o XML, quando presente; resultados
podem não conter XML. Dados fiscais adicionais, como chave, protocolo,
recibo e motivo, devem receber o mesmo cuidado com privacidade.

O resumo `resultado.to_dict()` e `diagnostico.to_dict()` são as superfícies
destinadas a diagnóstico seguro. O resumo não inclui o XML nem a carga
fiscal completa. Não deduza autorização somente da ausência de exceção:
inspecione `sucesso`, `estado` e os códigos retornados.

`AcbrError` representa falhas de configuração, entrada, autorização de rede,
integridade, execução e protocolo. Seu atributo `diagnostico` contém o
diagnóstico seguro. Uma rejeição fiscal representada em `ResultadoFiscal`
deve ser tratada conforme o estado e os códigos; não é equivalente a uma
falha de comunicação.

`AcbrError.resultado_desconhecido` indica que a aplicação deve reconciliar
o resultado antes de decidir nova tentativa. Em uma falha de `transmitir`
após iniciar o processo, `AcbrError.xml_original` pode disponibilizar o XML
assinado original da chamada, por acesso explícito. Esse conteúdo é sensível e fica fora
do `repr` do erro e do resumo do diagnóstico; não o registre em logs.
`limpeza_confirmada` informa se o cliente confirmou o encerramento observado.

## Cancelamento, prazo e reconciliação

Todas as operações aceitam um evento de cancelamento. O cancelamento
cooperativo interrompe a comunicação e solicita encerramento do processo
pertencente à chamada. Ele não desfaz uma operação remota. O prazo cobre
comunicação e execução do filho; a verificação prévia do runtime também tem
custo e não está incluída nesse prazo.

Não há repetição automática. Timeout, cancelamento, falha de protocolo ou
perda da resposta podem deixar o resultado de uma chamada remota
indeterminado. A aplicação consumidora precisa reconciliar a situação antes
de decidir qualquer nova tentativa. O diagnóstico indica as condições de
encerramento observadas; não garante rollback fiscal.

`ResultadoFiscal.envio_iniciado` registra o marcador observado do worker.
Ausência desse marcador não prova ausência de envio: após uma falha de
transporte em `transmitir`, `cancelar` ou `inutilizar`, não deduza que uma
repetição é segura somente porque o marcador não chegou. Consulte o
diagnóstico, trate `resultado_desconhecido` e reconcilie a situação.

## Evidência e limites

A suíte offline verifica entradas, bloqueios de rede, requisições e respostas
por workers simulados. Os testes de transmissão, consulta, cancelamento,
inutilização e recuperação validam o protocolo do cliente; não demonstram
aceitação por um serviço fiscal. O smoke nativo encadeia geração, assinatura
e validação locais e rejeita uma assinatura alterada. Ele usa fixtures
sintéticas e um A1 efêmero criado por `cryptography>=46`, dependência exclusiva
dos testes. Qualquer relatório de assinatura nativa deve identificar os
sistemas efetivamente testados.

O alvo permanece CPython 3.11–3.14, Windows x64 e Linux x64/glibc, com CI nos
dois sistemas. O runtime e os pins de integridade continuam na versão 0.2.0.
Veja [arquitetura](architecture.md) e o relatório da execução de testes para
os limites observados. Nenhum teste autoriza usar este SDK como homologado.
