# Arquitetura e decisões do SDK

## Viabilidade

É viável oferecer um cliente Python sem reproduzir a lógica fiscal: o worker
Free Pascal/ACBr 0.2.0 já publica um protocolo JSON por processo e arquivos
nativos para Windows x64 e Linux x64/glibc. A camada Python traduz os nomes
de sua API para esse protocolo e reaproveita o mesmo contrato de tipos.
Node.js, PHP, Django, Flask e FFI não são requisitos de execução.

O alvo é CPython 3.11–3.14. Python 3.11 fornece `tomllib` para as verificações
do projeto e permite manter uma implementação de execução somente com a
biblioteca padrão. A CI cobre as quatro versões em Windows e Ubuntu.
O runtime Linux de referência usa Ubuntu 24.04/glibc; isso não estabelece
compatibilidade com toda distribuição Linux. Outras arquiteturas e sistemas
precisam de artefatos nativos e validação próprios.

## Camadas

1. `Configuracao`, `Documento`, certificado, `Consulta`, `Cancelamento`,
   `Inutilizacao`, resultados e erros definem a fronteira pública tipada,
   sem dependência de framework.
2. O contrato JSON preserva origem, nomes e tipos ACBr. Modelos Python são
   gerados de forma determinística; `tools/generate_models.py --check`
   identifica divergências. A ajuda consulta o mesmo contrato.
3. `Emissor` monta a requisição do worker, inicia um processo por chamada e
   converte a resposta em `ResultadoFiscal`. Nenhum shell é necessário.
4. A gestão nativa seleciona versão/plataforma, verifica SHA-256 e inventário,
   instala os arquivos originais e oferece diagnóstico local.

O pacote usa `pyproject.toml`, backend setuptools e layout `src`. Wheel e
sdist transportam Python, contrato JSON, manifesto e `py.typed`; executáveis
nativos são instalados separadamente e apenas mediante comando explícito.
Não há download nativo como efeito colateral de import ou de `pip install`.

O SDK é público e pode ser instalado por aplicações consumidoras públicas ou
privadas. Configuração de uma aplicação, persistência, filas e credenciais
pertencem à aplicação consumidora. O SDK não depende de um projeto privado
para fornecer sua API nem transporta dados ou segredos de um consumidor.

## Versões e ajuda offline

A versão 0.1.0a4 acrescenta ajuda em texto com `describe TARGET`, saída JSON
com `describe TARGET --json`, `--version` e a função `describe_type`.
`ajuda TARGET` mantém o JSON da interface 0.1.0a3, baseado em
`describe_field`. O campo `sdkVersion` reflete a versão do código consultado.
Essa mudança não altera o pin nativo 0.2.1 nem o contrato ACBr autenticado.

A ajuda lê o contrato JSON incluído no pacote; não instala ou verifica o
runtime, não inicia um processo nativo e não acessa rede. O renderizador de
texto usa apenas os metadados disponíveis. A API `describe_field` aceita
caminhos de campos e nomes de tipos; `describe_type` exige um nome exato de
tipo do contrato. Os modelos gerados representam enums por aliases
`typing.Literal`, consultáveis com `typing.get_args`, e não por classes
`Enum`. Defaults pertencem aos campos que os declaram e não são aplicados
pela ajuda ou pela validação estrutural Python.

O comando novo em texto envia erros de consulta a stderr; `--json` e
`ajuda` preservam o diagnóstico JSON em stdout. Ambos usam saída 1 para
falhas de consulta; erros de sintaxe continuam com saída 2 do argparse.
`--help` e `--version` encerram sem consultar o motor. Veja
[ajuda.md](ajuda.md) para os comandos disponíveis em cada versão.

## Escopo verificável

| Operação | Escopo desta versão | Evidência prevista |
| --- | --- | --- |
| `gerar_xml(Documento(...))` | Geração local pelo worker | Workers simulados e smoke nativo Windows/Linux com fixture sintética |
| `validar(xml)` | Validação local pelo worker | Workers simulados e resposta real do schema, incluindo rejeição de XML sem assinatura |
| `assinar(xml)` | Assinatura local pelo worker com A1 | Protocolo simulado e smoke nativo com A1 sintético efêmero |
| `transmitir(xml_assinado)` | Transmissão síncrona pelo worker com A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem envio SEFAZ |
| `consultar(Consulta(...))` | Consulta por chave, com recibo opcional, A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem consulta SEFAZ |
| `cancelar(Cancelamento(...))` | Evento de cancelamento, com A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem evento SEFAZ |
| `inutilizar(Inutilizacao(...))` | Pedido de inutilização, com A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem pedido SEFAZ |
| `recuperar_xml(xml_assinado)` | Interface experimental com A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem consulta SEFAZ |
| Outras operações do worker | Fora da API pública desta versão | Nenhuma promessa de implementação |

O smoke nativo encadeia geração, assinatura e validação locais pela API
pública e verifica rejeição de assinatura alterada. Ele cria um A1 sintético
efêmero com `cryptography>=46`, dependência exclusiva de teste, sem abrir
operação fiscal remota. Seu resultado não homologa certificado de contribuinte.
Uma rejeição de schema prevista pode comprovar a integração da validação;
ela não deve ser apresentada como validação fiscal bem-sucedida da fixture.
Cada relatório de execução deve distinguir testes locais, CI e itens não
exercitados. Definir uma matriz no workflow não comprova sua execução.

## Fronteira de rede

`transmitir`, `consultar`, `cancelar`, `inutilizar` e `recuperar_xml` bloqueiam
rede por padrão e exigem `allow_network=True` por chamada, além do certificado
A1. A autorização é validada antes de iniciar o worker. `ambiente=2` escolhe
o ambiente fiscal de homologação; não transforma a operação em teste offline.
`gerar_xml`, `validar` e `assinar` executam operações locais do worker.

A CLI permanece restrita a ajuda, instalação explícita e diagnóstico do
runtime. Não expõe operações fiscais nem aceita certificado ou senha por
argumentos. A API Python é a única superfície dessas operações no SDK.
O contrato público e seus limites estão em [api.md](api.md).

## Processo, prazo e cancelamento

Cada chamada possui processo e pipes próprios. O cliente envia uma requisição
JSON pelo stdin e lê stdout/stderr com limites de bytes. O prazo e o evento
de cancelamento são verificados durante a comunicação. O encerramento
limita-se ao processo pertencente à chamada; o cliente não reinicia host,
Docker, WSL ou serviços compartilhados.

`cancel=threading.Event()` é cooperativo. Timeout/cancelamento não oferecem
rollback de uma chamada remota nem autorizam repetição automática. Sistemas
operacionais podem impedir confirmação imediata de término de um processo;
essa condição deve permanecer visível no erro/diagnóstico. Verificação de
integridade e abertura do processo possuem custos próprios, que devem ser
considerados ao definir o prazo da aplicação.

PFX e senha trafegam no stdin, não na linha de comando. Resultados expõem o
XML por acesso explícito. Logs da aplicação devem usar diagnósticos seguros,
sem registrar carga fiscal, certificados ou segredos. Os testes usam apenas
fixtures e materiais sintéticos.

O hook público `ao_iniciar_envio` permite à aplicação consumidora persistir
o marcador de envio observado. Ele recebe `EventoEnvio` imutável, contendo
somente correlação e comando (`transmitir`, `cancelar` ou `inutilizar`). O
callback não recebe stdout bruto nem payload fiscal. Observar esse marcador
não confirma autorização, não garante persistência anterior ao envio remoto
e não estabelece idempotência. Uma exceção no callback deixa o resultado
potencialmente incerto; o SDK não repete a operação.

## Runtime, integridade e distribuição

O pin do runtime é 0.2.1, com o contrato ACBr da revisão 48590. Os executáveis
e o contrato são idênticos aos da 0.2.0; a nova distribuição completa textos
de licença e seus inventários. O instalador
deve conferir o arquivo original e seu inventário, rejeitar entradas perigosas
de arquivo e preservar bibliotecas, schemas, serviços, fontes e licenças.
O `.tgz` original é obtido por HTTPS do registry npm, utilizado como
armazenamento de artefato. A instalação não requer Node.js ou npm e não
executa comandos npm; o Python inicia diretamente o executável Pascal.
O diretório instalado deve ter permissões adequadas; hashes detectam
divergências, mas não tornam confiável um diretório modificável por terceiros.

Os `.tgz` originais contêm fontes e licenças em `runtime/sources` e
`runtime/licenses`. O cliente não reempacota nem relicencia seus binários.
O projeto de referência declara LGPL-2.1-or-later; componentes nativos mantêm
suas licenças e exceções, que devem acompanhar qualquer redistribuição.
Alterar ou redistribuir um runtime exige rever as obrigações dos componentes,
inclusive a disponibilidade das fontes correspondentes. Consulte `NOTICE`.
Nos tarballs 0.2.1 publicados foram conferidos os hashes de todos os arquivos,
os avisos e textos canônicos, o inventário de licenças e suas referências.
Essa evidência resolve a ausência específica do texto Apache-2.0 no Linux
0.2.0; não constitui certificação jurídica integral.

## Limites e próximos passos

Não foram usados certificados privados, credenciais novas nem testes de
produção/homologação remotos. A ampliação da API em 0.1.0a2 acrescenta
assinatura, transmissão, consulta, cancelamento e inutilização, mantendo o
worker 0.2.0 original. Isso amplia a superfície pública; não comprova
homologação desses fluxos. A validação das operações de rede é limitada ao
protocolo com workers simulados. A recuperação real também depende de
homologação controlada posterior.

Carta de correção, outros eventos, filas, persistência e integrações de
framework permanecem fora desta versão. A aplicação consumidora deve tratar
resultados indeterminados e reconciliação; não há repetição automática.

A CI executa testes offline e empacotamento com permissões de leitura. O
smoke nativo usa instalação explícita em Windows e Ubuntu. Push em `main` e
atualizações de PR acionam a CI, sem duplicar a execução pelo push da branch
do mesmo PR. A publicação no PyPI exige disparo manual de `publish-pypi.yml`
em uma tag compatível com a versão, CI aprovada do SHA efetivo e aprovação
do revisor no environment `pypi`. A CI comum não publica pacotes e nenhum
workflow faz merge automaticamente.

## Fontes de projeto

- [Worker, contrato e licença ACBr Node](https://github.com/cosmemilton/acbr-node).
- [Cliente de referência ACBr PHP](https://github.com/cosmemilton/acbr-php).
- [Metadados e backend recomendados pela PyPA](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
- [Inclusão de arquivos no pacote setuptools](https://setuptools.pypa.io/en/latest/userguide/datafiles.html).
