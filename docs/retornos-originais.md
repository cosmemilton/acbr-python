# Retornos originais disponíveis e limites do worker 0.2.0

`ResultadoFiscal.retorno_original` preserva o dicionário JSON terminal
validado que o worker entregou ao cliente. `AcbrError` oferece o mesmo acesso
quando um frame terminal válido foi recebido antes da falha. O campo não
contém o tráfego HTTP/SOAP bruto nem o retorno completo do ACBr: dados
descartados pelo worker continuam indisponíveis. Veja os
[limites do worker](#limites-do-worker).

## Contrato de acesso

- `retorno_original: dict | None` retorna uma cópia profunda, inclusive dos
  campos extras recebidos. Alterar essa cópia não altera a evidência mantida
  no resultado ou erro.
- `origem_retorno_original` retorna `"acbr_worker_jsonl"` quando há um frame,
  ou `None` quando não há. Essa identificação descreve a origem da interface;
  não é uma assinatura de autenticidade do conteúdo.
- Sem frame terminal válido, os dois acessos retornam `None`. Não se cria
  um retorno fiscal a partir de stderr, de bytes inválidos ou de uma resposta
  incompleta.
- O erro pode conservar um frame válido mesmo se, depois, ocorrer falha de
  transporte ou de encerramento. Preservar esse frame não elimina a
  incerteza indicada por `resultado_desconhecido` e pelo diagnóstico.

O valor é o JSON decodificado, não os bytes exatos da linha JSONL: espaços,
ordem textual de propriedades e delimitadores de transporte não são uma
captura de rede. Não representa todo o estado interno de `TACBrNFe`.

`ResultadoFiscal.to_dict()` continua sendo um resumo seguro, sem retorno
original, XML, identidade fiscal ou `xMotivo` bruto. Para erros, use
`erro.diagnostico.to_dict()` nos logs. `dataclasses.asdict(resultado)` inclui
campos privados, inclusive `_retorno_original`, e não deve substituir esse
resumo. Tampouco registre o `__dict__` de um erro.

O frame pode incluir `cStat`, `xMotivo`, `chave`, `protocolo`, `recibo` e
`xmlBase64`, conforme a operação e o ramo percorrido, além de estado,
sucesso, códigos e metadados de protocolo/correlação, como `versao`, `id`,
`sourceRevision` e `contractHash`. Esses campos não estão presentes em toda
resposta. O helper que seleciona os escalares e o XML está em
[NativeMotor.Resultado, revisão fixada](https://github.com/cosmemilton/acbr-node/blob/5ff66828eb70f942608517f1e11719272b2786b8/native/NativeMotor.pas#L143-L158).

## Mapa do XML que efetivamente sai do worker

Na tabela, “XML” significa o conteúdo selecionado pelo worker para
`xmlBase64`, acessível decodificado por `ResultadoFiscal.xml`. Uma falha pode
encerrar o fluxo antes dessa seleção. `RetWS` é o valor exposto pelo ACBr;
o nome não garante uma cópia do envelope SOAP ou da resposta HTTP original.

| Operação ou ramo | XML selecionado pelo worker 0.2.0 | Limite da evidência |
| --- | --- | --- |
| `gerar_xml` (`gerarXml`) | `NotasFiscais.Items[0].GerarXML` | Documento gerado localmente, sem resposta de serviço fiscal. |
| `validar` | Nenhum XML de saída | O XML recebido como entrada não é devolvido nesse ramo. |
| `assinar` | `NotasFiscais.Items[0].XMLAssinado` | Documento assinado localmente, sem resposta de serviço fiscal. |
| `transmitir` | `NotasFiscais.Items[0].XMLOriginal` | Pode ser o `nfeProc` autorizado ou o XML assinado de entrada em um resultado pendente; não é `Enviar.RetWS` do lote. |
| `consultar`, sem recibo | `WebServices.Consulta.RetWS` | É o retorno de consulta selecionado pelo ACBr, junto aos escalares escolhidos pelo motor. |
| `consultar`, com recibo e item `ProtDFe` correspondente | `XMLprotDFe` somente do item encontrado | Os escalares são os desse item; o envelope de retorno do lote não é exportado. |
| `consultar`, com recibo e sem itens `ProtDFe` | `WebServices.Retorno.RetWS` | Neste ramo o motor exporta o retorno do lote. Se houver itens, mas nenhum corresponder à chave, ocorre falha de identidade. |
| `inutilizar` | `WebServices.Inutilizacao.XML_ProcInutNFe` | É o XML processado selecionado pelo ACBr, não uma captura HTTP. |
| `cancelar`/ramo de eventos, exatamente um retorno | `RetInfEvento.XML` após o processamento final do ACBr | No fluxo normal com lote `cStat=128` e item `135`, `136` ou `155`, contém `procEventoNFe` completo, com evento assinado e `retEvento`. Em rejeição, o XML pode estar ausente; exceções após início de envio podem removê-lo. |
| Ramo de eventos, outra cardinalidade de retorno | `WebServices.EnvEvento.RetWS` | O motor seleciona o retorno do lote nesse ramo. |
| `recuperar_xml`, sucesso comprovado | XML composto pelo worker com a `NFe` original intacta e o `protNFe` da consulta | O `nfeProc` é uma composição validada pelo worker; o XML original de consulta não acompanha a resposta. |
| `recuperar_xml`, recuperação recusada | Nenhum XML da consulta | Podem sair código, motivo e chave, mas não `Consulta.RetWS`. |

No cancelamento normal com `cStat=135`, o XML exportado é o
`procEventoNFe` 1.00 completo. Isso resulta do pós-processamento do ACBr:
o parser inicialmente atribui `infEvento.OuterXml` a `RetInfEvento.XML`, mas
`TNFeEnvEvento.TratarResposta` compõe o documento processado e sobrescreve
as propriedades XML do retorno e do evento. A atribuição inicial do parser
não representa o estado final consumido pelo worker. Mesmo um
`procEventoNFe` completo com `cStat=136` não comprova vinculação à NF-e.
O documento processado também não é uma captura do envelope SOAP/HTTP.

Essa sequência foi conferida nas fontes ACBr da revisão 48590 incluídas em
`runtime/sources/acbr-source.tar.gz`, SHA-256
`c4f4aa2b35caddcede67367cf70ec929425979d56e3a16d0596340f3bd104c9c`:
o parser em `ACBrNFe.RetEnvEvento.pas`, linha 642, faz a atribuição inicial;
[ACBrNFeWebServices.pas, na revisão oficial fixada](https://sourceforge.net/p/acbr/code/48590/tree/trunk2/Fontes/ACBrDFe/ACBrNFe/ACBrNFeWebServices.pas),
em `TNFeEnvEvento.TratarResposta`, linhas 3772–3790, compõe o
`procEventoNFe` para os itens `135`, `136` e `155` quando o lote foi
processado, e as linhas 3810–3811 substituem ambas as propriedades XML.
Para item rejeitado, a composição fica vazia e não há garantia de XML
disponível no frame, nem de frame terminal válido em todo caminho de falha.
Outra cardinalidade de retorno segue o ramo
`EnvEvento.RetWS` da tabela.

Os ramos estão no código fixado de
[geração e recuperação](https://github.com/cosmemilton/acbr-node/blob/5ff66828eb70f942608517f1e11719272b2786b8/native/NativeMotor.pas#L174-L207),
[validação, assinatura, transmissão e inutilização](https://github.com/cosmemilton/acbr-node/blob/5ff66828eb70f942608517f1e11719272b2786b8/native/NativeMotor.pas#L208-L232)
e [consulta e eventos](https://github.com/cosmemilton/acbr-node/blob/5ff66828eb70f942608517f1e11719272b2786b8/native/NativeMotor.pas#L233-L258).
O ramo de eventos existe no worker; sua descrição não acrescenta operações
à API pública Python além das documentadas em [api.md](api.md).

## Limites do worker

O SDK pode preservar o frame que recebeu. Para disponibilizar os itens a
seguir, seria necessário alterar o worker, publicar novos artefatos e
versionar seus hashes e contrato de retorno:

- `Enviar.RetWS` completo na transmissão, separado do XML do documento.
- Envelope do retorno do lote por recibo quando o motor escolhe um item
  `ProtDFe`, inclusive dados dos demais itens e escalares próprios do lote.
- Envelope original do lote em `EnvEvento.RetWS` quando há exatamente um
  retorno de evento, separado do `procEventoNFe` pós-processado que já pode
  estar disponível. Preservar esse documento não equivale a preservar o
  envelope SOAP/HTTP.
- `Consulta.RetWS` original usado em `recuperar_xml`, tanto no sucesso como
  na recuperação recusada.
- Detalhes internos de validação em `Err` e mensagens originais de exceções
  que o motor substitui por códigos/mensagens estáticos.
- Valores que o tratamento de exceção após início de envio remove: `cStat`,
  protocolo, recibo e XML de resposta. Nesse ramo, `transmitir` pode recolocar
  o XML assinado original da chamada; isso não recupera a resposta fiscal.

Esse último comportamento está no
[tratamento de exceções do motor](https://github.com/cosmemilton/acbr-node/blob/5ff66828eb70f942608517f1e11719272b2786b8/native/NativeMotor.pas#L261-L267).
Um campo ausente nunca deve ser apresentado como recuperado por esta API.
Consultar o serviço novamente seria outra operação, com outro retorno, e
não restauraria os bytes de uma resposta anterior descartada.

## Uso privado e exemplo sintético

`retorno_original`, `c_stat`, `x_motivo`, protocolo e XML podem conter dados
fiscais e devem seguir somente para o armazenamento privado da aplicação
consumidora, quando necessário. Não os envie a logs públicos, telemetria,
issues ou exemplos versionados. PFX, senha e CSC não pertencem a esse
registro; nunca acrescente a configuração da chamada à evidência persistida.

O exemplo abaixo cria um erro manual com dados fictícios para mostrar os
acessos e a cópia profunda. Não inicia worker, não consulta serviço fiscal e
não constitui evidência de um retorno real do ACBr:

```python
from acbr import AcbrError

frame_sintetico = {
    "versao": 1,
    "id": "exemplo-sintetico",
    "sucesso": False,
    "estado": "ERRO",
    "codigo": "EXEMPLO_SINTETICO",
    "xMotivo": "Mensagem fictícia para testar armazenamento privado.",
}
erro = AcbrError(
    "EXEMPLO_SINTETICO",
    "Erro criado manualmente para documentação.",
    retorno_original=frame_sintetico,
)

# Encaminhe este objeto somente ao armazenamento privado da aplicação.
evidencia_privada = {
    "origem": erro.origem_retorno_original,
    "frame": erro.retorno_original,
}

copia = erro.retorno_original
assert copia is not None
copia["xMotivo"] = "Alteração apenas na cópia."
assert erro.retorno_original["xMotivo"] == frame_sintetico["xMotivo"]

# O diagnóstico continua separado da evidência fiscal.
resumo_seguro = erro.diagnostico.to_dict()
assert "retorno_original" not in resumo_seguro
```

Em resultados reais, use `resultado.retorno_original` e
`resultado.origem_retorno_original` da mesma maneira, sem transformar o
resumo seguro em um dump do objeto. A disponibilidade do frame não altera
as regras de consentimento de rede, resultado indeterminado ou ausência de
repetição automática descritas na [API pública](api.md).
