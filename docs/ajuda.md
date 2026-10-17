# Ajuda de campos e tipos

A ajuda consulta o contrato ACBr incluído no pacote Python. Não exige
runtime instalado, A1 ou acesso à rede e não executa o motor nativo.
Os exemplos abaixo apenas consultam metadados; não iniciam operações fiscais.

## Versão publicada e checkout

A versão publicada no PyPI é **0.1.0a3**. Ela já oferece JSON pela CLI:

```console
python -m acbr ajuda Ide.tpNF
python -m acbr ajuda TTipoNFe
```

Em Python, `from acbr import describe_field` também funciona nessa versão.
O checkout **0.1.0a4.dev0**, ainda não publicado, acrescenta `describe`,
`--version` e a função `describe_type`. Para experimentar essas novidades,
instale sua cópia do repositório com `python -m pip install .` em um ambiente
virtual. Instalar `acbr-python==0.1.0a3` do PyPI não fornece esses acréscimos.

## Texto e JSON no checkout 0.1.0a4.dev0

```console
python -m acbr --version
python -m acbr --help
python -m acbr describe --help
python -m acbr describe Ide.tpNF
python -m acbr describe TTipoNFe
python -m acbr describe TTipoNFe --json
```

`--version` mostra `acbr-python 0.1.0a4.dev0` para este checkout. A descrição
do campo `Ide.tpNF` em texto é:

```text
TNFe.Ide.tpNF
Tipo: TTipoNFe (enum; entrada string)
Somente leitura: não
Valores: tnEntrada, tnSaida
Padrão declarado: tnSaida
```

A descrição do tipo `TTipoNFe` apresenta os mesmos valores, mas não inclui
`Padrão declarado`: esse metadado pertence ao campo `Ide.tpNF`. Nomes,
valores e padrões vêm exclusivamente do contrato. A ajuda não converte esses
valores para códigos fiscais nem determina qual usar em uma operação.

`describe TARGET --json` retorna o objeto de `describe_field(TARGET)`.
`ajuda TARGET` conserva a saída JSON compatível. Ambos usam os mesmos
metadados e a mesma formatação no checkout; `sdkVersion` informa a versão
do código Python que realizou a consulta. Para redirecionar o JSON:

```console
python -m acbr describe Ide.tpNF --json > campo.json
```

Sem TARGET, tanto `describe` quanto `ajuda` consultam `TNFe`.
`--json` também pode vir antes do TARGET em `describe`; `ajuda` sempre
retorna JSON e não aceita essa opção.

## Caminhos, coleções e tipos

Os nomes distinguem maiúsculas de minúsculas. O prefixo `TNFe.` é opcional
para campos. Use nomes completos quando um nome curto for ambíguo.

```console
python -m acbr describe TNFe.Ide.tpNF
python -m acbr describe TProd
python -m acbr describe Det
python -m acbr describe 'Det[].Prod.vProd'
python -m acbr describe 'Det[0].Prod.vProd'
```

`Det` descreve a coleção e seu tipo de item. `Det[].Prod.vProd` seleciona
um campo do item; um índice numérico é normalizado para `[]` no resultado.
Para percorrer uma coleção, é necessário usar `[]` ou um índice.

Objetos listam seus campos, tipos e indicadores de somente leitura. Listas
informam o tipo dos itens. Enums mostram os valores textuais aceitos. Limites
numéricos, escala e padrão só aparecem quando declarados para o campo.
`inputType` no JSON descreve o transporte JSON; por exemplo, decimais são
strings. Esses metadados não representam obrigatoriedade ou regras fiscais.

## API Python

```python
from typing import get_args

from acbr import describe_field
from acbr.models import TTipoNFe

campo = describe_field("Ide.tpNF")
print(campo["pascalType"])       # TTipoNFe
print(campo["values"])           # ['tnEntrada', 'tnSaida']
print(campo["declaredDefault"])  # tnSaida
print(get_args(TTipoNFe))         # ('tnEntrada', 'tnSaida')
```

`TTipoNFe` é um alias `Literal`, não uma classe `Enum`: use `get_args`
para consultar seus valores. A entrada do documento usa as strings do
contrato. A ajuda e `Documento` não inserem defaults nos campos omitidos.

A API nova do checkout oferece uma consulta estrita por nome de tipo:

```python
from acbr import AcbrError, describe_type  # 0.1.0a4.dev0, ainda não publicada

tipo = describe_type("TTipoNFe")
assert tipo["values"] == ["tnEntrada", "tnSaida"]
assert "declaredDefault" not in tipo

try:
    describe_type("Ide.tpNF")  # Caminho de campo não é nome de tipo.
except AcbrError as erro:
    assert erro.diagnostico.codigo == "TIPO_INVALIDO"
```

`describe_type` aceita tipos de objeto, lista ou enum do contrato, como
`TProd`, `TDetCollection` e `TTipoNFe`. Rejeita caminhos de campos, espaços,
capitalização diferente e aliases Python com sufixo `Output`. Para consultar
um campo, use `describe_field`.

As duas funções retornam dicionários independentes, incluindo revisão e
hashes do contrato, versão do SDK, tipo Pascal, tipo JSON e metadados
disponíveis. Alterar o dicionário retornado não altera o contrato do pacote.
Essas informações não validam um documento em schema ou em serviço fiscal.

## Canais e códigos de saída da CLI

| Consulta no checkout | Sucesso | Erro de consulta |
| --- | --- | --- |
| `describe TARGET` | Texto em stdout, saída 0 | Mensagem e ação em stderr, saída 1; stdout vazio |
| `describe TARGET --json` | Objeto JSON em stdout, saída 0 | Diagnóstico JSON em stdout, saída 1 |
| `ajuda TARGET` | Objeto JSON em stdout, saída 0 | Diagnóstico JSON em stdout, saída 1 |
| `--help` ou `--version` | Texto em stdout, saída 0 | Não realizam consulta de campo ou operação nativa |

Erros de sintaxe, como uma opção desconhecida ou um argumento excedente,
continuam sendo tratados pelo argparse: mensagem em stderr e saída 2.
Não confunda esse caso com um caminho de campo válido sintaticamente que
não existe no contrato, cujo código de saída é 1.

Exemplos de códigos seguros de diagnóstico: `CAMPO_AMBIGUO` para um nome
curto com mais de um caminho, `COLECAO_REQUER_INDICE` para percorrer coleção
sem seleção e `CAMPO_INEXISTENTE` para campo ausente. Na API Python,
`describe_type` usa `TIPO_INVALIDO` para uma consulta de tipo inválida.

A ajuda descreve apenas o contrato fixado. Para instalação e verificação
do runtime, veja o [README](../README.md); para as operações e seus limites,
veja a [API pública](api.md) e a [arquitetura](architecture.md).
