# Arquitetura e decisões do MVP

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

1. `Configuracao`, `Documento`, certificado, resultados e erros definem a
   fronteira pública tipada, sem dependência de framework.
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

## Escopo verificável

| Operação | Escopo desta versão | Evidência prevista |
| --- | --- | --- |
| `gerar_xml(Documento(...))` | Geração local pelo worker | Workers simulados e smoke nativo Windows/Linux com fixture sintética |
| `validar(xml)` | Validação local pelo worker | Workers simulados e resposta real do schema, incluindo rejeição de XML sem assinatura |
| `recuperar_xml(xml_assinado)` | Interface experimental com A1 e `allow_network=True` | Somente contrato/protocolo simulado; sem consulta SEFAZ |
| Outras operações | Fora da API pública do MVP | Nenhuma promessa de implementação |

Os testes nativos não precisam de A1 e não abrem uma operação fiscal remota.
Uma rejeição de schema prevista pode comprovar a integração da validação;
ela não deve ser apresentada como validação fiscal bem-sucedida da fixture.
Cada relatório de execução deve distinguir testes locais, CI e itens não
exercitados. Definir uma matriz no workflow não comprova sua execução.

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

## Runtime, integridade e distribuição

O pin do runtime é 0.2.0, com o contrato ACBr da revisão 48590. O instalador
deve conferir o arquivo original e seu inventário, rejeitar entradas perigosas
de arquivo e preservar bibliotecas, schemas, serviços, fontes e licenças.
O diretório instalado deve ter permissões adequadas; hashes detectam
divergências, mas não tornam confiável um diretório modificável por terceiros.

Os `.tgz` originais contêm fontes e licenças em `runtime/sources` e
`runtime/licenses`. O cliente não reempacota nem relicencia seus binários.
O projeto de referência declara LGPL-2.1-or-later; componentes nativos mantêm
suas licenças e exceções, que devem acompanhar qualquer redistribuição.
Alterar ou redistribuir um runtime exige rever as obrigações dos componentes,
inclusive a disponibilidade das fontes correspondentes. Consulte `NOTICE`.

## Limites e próximos passos

Não foram assumidos certificados privados, credenciais novas nem testes de
produção/homologação remotos. Assinatura, emissão, consulta, eventos fiscais,
filas e integrações de framework ficam para incrementos separados com testes
específicos. A recuperação real depende de homologação controlada posterior;
esta versão só estabelece sua fronteira explícita de rede e certificado.

A CI executa testes offline e empacotamento com permissões de leitura. O
smoke nativo usa instalação explícita em Windows e Ubuntu. Nenhum workflow
publica no PyPI ou faz merge automaticamente.

## Fontes de projeto

- [Worker, contrato e licença ACBr Node](https://github.com/cosmemilton/acbr-node).
- [Cliente de referência ACBr PHP](https://github.com/cosmemilton/acbr-php).
- [Metadados e backend recomendados pela PyPA](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/).
- [Inclusão de arquivos no pacote setuptools](https://setuptools.pypa.io/en/latest/userguide/datafiles.html).
