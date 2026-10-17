"""Generated ACBr wire types; edit tools/generate_models.py instead.

All input properties are optional; omitted values use native defaults.
Readonly properties occur only in Output types. Decimal and civil ISO
date/time values are strings. Runtime validation is in acbr.contract.
Use acbr.describe_type(name) for contract metadata and typing.get_args
for the exact string values of a Literal alias.
Source: cosmemilton/acbr-node@5ff66828eb70f942608517f1e11719272b2786b8 (LGPL-2.1-or-later).
Contract SHA256: e5a497cefe8e0e350a30da5cc04e88b35c38a98535893d52f878890260d1346d.
"""

from __future__ import annotations

from typing import Literal, TypeAlias, TypedDict

TACBrProcessoEmissao: TypeAlias = Literal['peAplicativoContribuinte', 'peAvulsaFisco', 'peAvulsaContribuinte', 'peContribuinteAplicativoFisco', 'peProvedorAssinaturaAutorizacao']

TACBrTipoAmbiente: TypeAlias = Literal['taProducao', 'taHomologacao']

TACBrTipoEmissao: TypeAlias = Literal['teNormal', 'teContingencia', 'teSCAN', 'teDPEC', 'teFSDA', 'teSVCAN', 'teSVCRS', 'teSVCSP', 'teOffLine']

TACBrTipoImpressao: TypeAlias = Literal['tiSemGeracao', 'tiRetrato', 'tiPaisagem', 'tiSimplificado', 'tiNFCe', 'tiMsgEletronica', 'tiSimplificadoTipo2']

TcCredPres: TypeAlias = Literal['cpNenhum', 'cp01', 'cp02', 'cp03', 'cp04', 'cp05', 'cp06', 'cp07', 'cp08', 'cp09', 'cp10', 'cp11', 'cp12', 'cp13']

TCSOSNIcms: TypeAlias = Literal['csosnVazio', 'csosn101', 'csosn102', 'csosn103', 'csosn201', 'csosn202', 'csosn203', 'csosn300', 'csosn400', 'csosn500', 'csosn900']

TCSTCofins: TypeAlias = Literal['cof01', 'cof02', 'cof03', 'cof04', 'cof05', 'cof06', 'cof07', 'cof08', 'cof09', 'cof49', 'cof50', 'cof51', 'cof52', 'cof53', 'cof54', 'cof55', 'cof56', 'cof60', 'cof61', 'cof62', 'cof63', 'cof64', 'cof65', 'cof66', 'cof67', 'cof70', 'cof71', 'cof72', 'cof73', 'cof74', 'cof75', 'cof98', 'cof99']

TCSTIBSCBS: TypeAlias = Literal['cstNenhum', 'cst000', 'cst010', 'cst011', 'cst200', 'cst220', 'cst221', 'cst222', 'cst400', 'cst410', 'cst510', 'cst515', 'cst550', 'cst620', 'cst800', 'cst810', 'cst811', 'cst820', 'cst830']

TCSTIcms: TypeAlias = Literal['cstVazio', 'cst00', 'cst10', 'cst20', 'cst30', 'cst40', 'cst41', 'cst45', 'cst50', 'cst51', 'cst60', 'cst70', 'cst80', 'cst81', 'cst90', 'cstICMSOutraUF', 'cstICMSSN', 'cstPart10', 'cstPart90', 'cstRep41', 'cstRep60', 'cst02', 'cst15', 'cst53', 'cst61', 'cst01', 'cst12', 'cst13', 'cst14', 'cst21', 'cst72', 'cst73', 'cst74', 'cstPart20']

TCSTPis: TypeAlias = Literal['pis01', 'pis02', 'pis03', 'pis04', 'pis05', 'pis06', 'pis07', 'pis08', 'pis09', 'pis49', 'pis50', 'pis51', 'pis52', 'pis53', 'pis54', 'pis55', 'pis56', 'pis60', 'pis61', 'pis62', 'pis63', 'pis64', 'pis65', 'pis66', 'pis67', 'pis70', 'pis71', 'pis72', 'pis73', 'pis74', 'pis75', 'pis98', 'pis99']

TIndicadorEx: TypeAlias = Literal['tieNenhum', 'tieSim', 'tieNao']

TindIEDest: TypeAlias = Literal['inContribuinte', 'inIsento', 'inNaoContribuinte']

TindImport: TypeAlias = Literal['iiNacional', 'iiImportado']

TindIncentivo: TypeAlias = Literal['iiSim', 'iiNao']

TindIntermed: TypeAlias = Literal['iiSemOperacao', 'iiOperacaoSemIntermediador', 'iiOperacaoComIntermediador']

TIndSomaCOFINSST: TypeAlias = Literal['iscNenhum', 'iscCOFINSSTNaoCompoe', 'iscCOFINSSTCompoe']

TIndSomaPISST: TypeAlias = Literal['ispNenhum', 'ispPISSTNaoCompoe', 'ispPISSTCompoe']

TmotRedAdRem: TypeAlias = Literal['motTranspColetivo', 'motOutros']

TOrigemMercadoria: TypeAlias = Literal['oeNacional', 'oeEstrangeiraImportacaoDireta', 'oeEstrangeiraAdquiridaBrasil', 'oeNacionalConteudoImportacaoSuperior40', 'oeNacionalProcessosBasicos', 'oeNacionalConteudoImportacaoInferiorIgual40', 'oeEstrangeiraImportacaoDiretaSemSimilar', 'oeEstrangeiraAdquiridaBrasilSemSimilar', 'oeNacionalConteudoImportacaoSuperior70', 'oeReservadoParaUsoFuturo', 'oeVazio']

TpcnBandeiraCartao: TypeAlias = Literal['bcVisa', 'bcMasterCard', 'bcAmericanExpress', 'bcSorocred', 'bcDinersClub', 'bcElo', 'bcHipercard', 'bcAura', 'bcCabal', 'bcAlelo', 'bcBanesCard', 'bcCalCard', 'bcCredz', 'bcDiscover', 'bcGoodCard', 'bcGreenCard', 'bcHiper', 'bcJcB', 'bcMais', 'bcMaxVan', 'bcPolicard', 'bcRedeCompras', 'bcSodexo', 'bcValeCard', 'bcVerocheque', 'bcVR', 'bcTicket', 'bcOutros']

TpcnCondicaoVeiculo: TypeAlias = Literal['cvAcabado', 'cvInacabado', 'cvSemiAcabado']

TpcnConsumidorFinal: TypeAlias = Literal['cfNao', 'cfConsumidorFinal']

TpcnCRT: TypeAlias = Literal['crtSimplesNacional', 'crtSimplesExcessoReceita', 'crtRegimeNormal', 'crtMEI']

TpcnCstIpi: TypeAlias = Literal['ipi00', 'ipi49', 'ipi50', 'ipi99', 'ipi01', 'ipi02', 'ipi03', 'ipi04', 'ipi05', 'ipi51', 'ipi52', 'ipi53', 'ipi54', 'ipi55']

TpcnDestinoOperacao: TypeAlias = Literal['doInterna', 'doInterestadual', 'doExterior']

TpcnDeterminacaoBaseIcms: TypeAlias = Literal['dbiMargemValorAgregado', 'dbiPauta', 'dbiPrecoTabelado', 'dbiValorOperacao', 'dbiNenhum']

TpcnDeterminacaoBaseIcmsST: TypeAlias = Literal['dbisPrecoTabelado', 'dbisListaNegativa', 'dbisListaPositiva', 'dbisListaNeutra', 'dbisMargemValorAgregado', 'dbisPauta', 'dbisValordaOperacao']

TpcnECFModRef: TypeAlias = Literal['ECFModRefVazio', 'ECFModRef2B', 'ECFModRef2C', 'ECFModRef2D']

TpcnFinalidadeNFe: TypeAlias = Literal['fnNormal', 'fnComplementar', 'fnAjuste', 'fnDevolucao', 'fnCredito', 'fnDebito']

TpcnFormaPagamento: TypeAlias = Literal['fpDinheiro', 'fpCheque', 'fpCartaoCredito', 'fpCartaoDebito', 'fpCreditoLoja', 'fpValeAlimentacao', 'fpValeRefeicao', 'fpValePresente', 'fpValeCombustivel', 'fpDuplicataMercantil', 'fpBoletoBancario', 'fpDepositoBancario', 'fpPagamentoInstantaneo', 'fpTransfBancario', 'fpProgramaFidelidade', 'fpSemPagamento', 'fpRegimeEspecial', 'fpOutro', 'fpPagamentoInstantaneoEstatico', 'fpCreditoEmLojaPorDevolucao', 'fpFalhaHardware', 'fpPagamentoPosterior', 'fpPagInstantaneoPIXAutomatico', 'fpTEFBookTransfer']

TpcnIndEscala: TypeAlias = Literal['ieRelevante', 'ieNaoRelevante', 'ieNenhum']

TpcnIndicadorPagamento: TypeAlias = Literal['ipVista', 'ipPrazo', 'ipOutras', 'ipNenhum']

TpcnIndicadorProcesso: TypeAlias = Literal['ipSEFAZ', 'ipJusticaFederal', 'ipJusticaEstadual', 'ipSecexRFB', 'ipCONFAZ', 'ipOutros']

TpcnIndicadorTotal: TypeAlias = Literal['itSomaTotalNFe', 'itNaoSomaTotalNFe']

TpcnindISS: TypeAlias = Literal['iiExigivel', 'iiNaoIncidencia', 'iiIsencao', 'iiExportacao', 'iiImunidade', 'iiExigSuspDecisaoJudicial', 'iiExigSuspProcessoAdm']

TpcnindISSRet: TypeAlias = Literal['iirSim', 'iirNao']

TpcnISSQNcSitTrib: TypeAlias = Literal['ISSQNcSitTribVazio', 'ISSQNcSitTribNORMAL', 'ISSQNcSitTribRETIDA', 'ISSQNcSitTribSUBSTITUTA', 'ISSQNcSitTribISENTA']

TpcnModalidadeFrete: TypeAlias = Literal['mfContaEmitente', 'mfContaDestinatario', 'mfContaTerceiros', 'mfProprioRemetente', 'mfProprioDestinatario', 'mfSemFrete']

TpcnMotivoDesoneracaoICMS: TypeAlias = Literal['mdiTaxi', 'mdiDeficienteFisico', 'mdiProdutorAgropecuario', 'mdiFrotistaLocadora', 'mdiDiplomaticoConsular', 'mdiAmazoniaLivreComercio', 'mdiSuframa', 'mdiVendaOrgaosPublicos', 'mdiOutros', 'mdiDeficienteCondutor', 'mdiDeficienteNaoCondutor', 'mdiOrgaoFomento', 'mdiOlimpiadaRio2016', 'mdiSolicitadoFisco']

TpcnPresencaComprador: TypeAlias = Literal['pcNao', 'pcPresencial', 'pcInternet', 'pcTeleatendimento', 'pcEntregaDomicilio', 'pcPresencialForaEstabelecimento', 'pcOutros']

TpcnTipoArma: TypeAlias = Literal['taUsoPermitido', 'taUsoRestrito']

TpcnTipoIntermedio: TypeAlias = Literal['tiContaPropria', 'tiContaOrdem', 'tiEncomenda']

TpcnTipoOperacao: TypeAlias = Literal['toVendaConcessionaria', 'toFaturamentoDireto', 'toVendaDireta', 'toOutros']

TpcnTipoViaTransp: TypeAlias = Literal['tvMaritima', 'tvFluvial', 'tvLacustre', 'tvAerea', 'tvPostal', 'tvFerroviaria', 'tvRodoviaria', 'tvConduto', 'tvMeiosProprios', 'tvEntradaSaidaFicta', 'tvCourier', 'tvEmMaos', 'tvPorReboque']

TRegTribISSQN: TypeAlias = Literal['RTISSMicroempresaMunicipal', 'RTISSEstimativa', 'RTISSSociedadeProfissionais', 'RTISSCooperativa', 'RTISSMEI', 'RTISSMEEPP', 'RTISSNenhum']

TTipoNFe: TypeAlias = Literal['tnEntrada', 'tnSaida']

TtpALCZFMCBS: TypeAlias = Literal['tpALCZFMCBSnOpInd', 'tpALCZFMCBSOpInd']

TtpAto: TypeAlias = Literal['taNenhum', 'taTermoAcordo', 'taRegimeEspecial', 'taAutorizacaoEspecifica', 'taAjusteSNIEF', 'taConvenioICMS']

TTpCredPresIBSZFM: TypeAlias = Literal['tcpNenhum', 'tcpSemCredito', 'tcpBensConsumoFinal', 'tcpBensCapital', 'tcpBensIntermediarios', 'tcpBensInformaticaOutros']

TtpEnteGov: TypeAlias = Literal['tcgNenhum', 'tcgUniao', 'tcgEstados', 'tcgDistritoFederal', 'tcgMunicipios', 'tcgConsorcioPublico', 'tcgComiteGestorIBS']

TtpGuia: TypeAlias = Literal['tpgNenhum', 'tpgGTA', 'tpgTTA', 'tpgDTA', 'tpgATV', 'tpgPTV', 'tpgGTV', 'tpgGuiaFlorestal']

TtpIntegra: TypeAlias = Literal['tiNaoInformado', 'tiPagIntegrado', 'tiPagNaoIntegrado']

TtpNFCredito: TypeAlias = Literal['tcNenhum', 'tcMultaJuros', 'tcApropriacaoCreditoPresumido', 'tcRetorno', 'tcReducaoValores', 'tcTransferenciaCreditoSucessao', 'tcRetornoRecusaParcial']

TtpNFDebito: TypeAlias = Literal['tdNenhum', 'tdTransferenciaCreditoCooperativa', 'tdAnulacao', 'tdDebitosNaoProcessadas', 'tdMultaJuros', 'tdTransferenciaCreditoSucessao', 'tdPagamentoAntecipado', 'tdPerdaEmEstoque', 'tdDesenquadramentodoSN']

TtpOperGov: TypeAlias = Literal['togNenhum', 'togFornecimento', 'togRecebimentoPag', 'togFornecimentoPagRealizado', 'togRecebimentoPagFornecPosterior']

class TAdiCollectionItem(TypedDict, total=False):
    "Entrada parcial de TAdiCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TAdiCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TAdiCollectionItem')."
    cFabricante: str
    nAdicao: int
    nDraw: str
    nSeqAdi: int
    vDescDI: str

class Tagropecuario(TypedDict, total=False):
    "Entrada parcial de Tagropecuario, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TagropecuarioOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tagropecuario')."
    defensivo: TdefensivoCollection
    guiaTransito: TguiaTransito

class TArmaCollectionItem(TypedDict, total=False):
    "Entrada parcial de TArmaCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TArmaCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TArmaCollectionItem')."
    descr: str
    nCano: str
    nSerie: str
    tpArma: TpcnTipoArma

class TautXMLCollectionItem(TypedDict, total=False):
    "Entrada parcial de TautXMLCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TautXMLCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TautXMLCollectionItem')."
    CNPJCPF: str

class TAvulsa(TypedDict, total=False):
    "Entrada parcial de TAvulsa, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TAvulsaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TAvulsa')."
    CNPJ: str
    dEmi: str
    dPag: str
    fone: str
    matr: str
    nDAR: str
    repEmi: str
    UF: str
    vDAR: str
    xAgente: str
    xOrgao: str

class Tcana(TypedDict, total=False):
    "Entrada parcial de Tcana, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TcanaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tcana')."
    deduc: TDeducCollection
    fordia: TForDiaCollection
    qTotAnt: str
    qTotGer: str
    qTotMes: str
    ref: str
    safra: str
    vFor: str
    vLiqFor: str
    vTotDed: str

class TCIDE(TypedDict, total=False):
    "Entrada parcial de TCIDE, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCIDEOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCIDE')."
    qBCProd: str
    vAliqProd: str
    vCIDE: str

class TCobr(TypedDict, total=False):
    "Entrada parcial de TCobr, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCobrOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCobr')."
    Dup: TDupCollection
    Fat: TFat

class TCOFINS(TypedDict, total=False):
    "Entrada parcial de TCOFINS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCOFINSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCOFINS')."
    CST: TCSTCofins
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vBCProd: str
    vCOFINS: str

class TCOFINSST(TypedDict, total=False):
    "Entrada parcial de TCOFINSST, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCOFINSSTOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCOFINSST')."
    indSomaCOFINSST: TIndSomaCOFINSST
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vCOFINS: str

class TComb(TypedDict, total=False):
    "Entrada parcial de TComb, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCombOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TComb')."
    CIDE: TCIDE
    CODIF: str
    cProdANP: int
    descANP: str
    encerrante: Tencerrante
    ICMS: TICMSComb
    ICMSCons: TICMSCons
    ICMSInter: TICMSInter
    origComb: TorigCombCollection
    pBio: str
    pGLP: str
    pGNi: str
    pGNn: str
    pMixGN: str
    qTemp: str
    UFcons: str
    vPart: str

class TCompra(TypedDict, total=False):
    "Entrada parcial de TCompra, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCompraOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCompra')."
    xCont: str
    xNEmp: str
    xPed: str

class TCredPresIBSZFM(TypedDict, total=False):
    "Entrada parcial de TCredPresIBSZFM, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCredPresIBSZFMOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCredPresIBSZFM')."
    competApur: str
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    vCredPresIBSZFM: str

class TCredPresumidoCollectionItem(TypedDict, total=False):
    "Entrada parcial de TCredPresumidoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TCredPresumidoCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCredPresumidoCollectionItem')."
    cCredPresumido: str
    pCredPresumido: str
    vCredPresumido: str

class TDeducCollectionItem(TypedDict, total=False):
    "Entrada parcial de TDeducCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDeducCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDeducCollectionItem')."
    vDed: str
    xDed: str

class TdefensivoCollectionItem(TypedDict, total=False):
    "Entrada parcial de TdefensivoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TdefensivoCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TdefensivoCollectionItem')."
    CPFRespTec: str
    nReceituario: str

class TDest(TypedDict, total=False):
    "Entrada parcial de TDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDestOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDest')."
    CNPJCPF: str
    Email: str
    EnderDest: TEnderDest
    idEstrangeiro: str
    IE: str
    IM: str
    indIEDest: TindIEDest
    ISUF: str
    xNome: str

class TDetCollectionItem(TypedDict, total=False):
    "Entrada parcial de TDetCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDetCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDetCollectionItem')."
    DFeReferenciado: TDFeReferenciado
    Imposto: TImposto
    infAdProd: str
    obsCont: TobsItem
    obsFisco: TobsItem
    pDevol: str
    Prod: TProd
    vIPIDevol: str
    vItem: str

class TdetExportCollectionItem(TypedDict, total=False):
    "Entrada parcial de TdetExportCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TdetExportCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TdetExportCollectionItem')."
    chNFe: str
    nDraw: str
    nRE: str
    qExport: str

class TDFErefCollectionItem(TypedDict, total=False):
    "Entrada parcial de TDFErefCollectionItem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDFErefCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDFErefCollectionItem')."
    refDFeChave: str

class TDFeReferenciado(TypedDict, total=False):
    "Entrada parcial de TDFeReferenciado, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDFeReferenciadoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDFeReferenciado')."
    chaveAcesso: str
    nItem: int

class TDICollectionItem(TypedDict, total=False):
    "Entrada parcial de TDICollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDICollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDICollectionItem')."
    adi: TAdiCollection
    cExportador: str
    CNPJ: str
    dDesemb: str
    dDi: str
    nDi: str
    tpIntermedio: TpcnTipoIntermedio
    tpViaTransp: TpcnTipoViaTransp
    UFDesemb: str
    UFTerceiro: str
    vAFRMM: str
    xLocDesemb: str

class TDupCollectionItem(TypedDict, total=False):
    "Entrada parcial de TDupCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TDupCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDupCollectionItem')."
    dVenc: str
    nDup: str
    vDup: str

class TEmit(TypedDict, total=False):
    "Entrada parcial de TEmit, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TEmitOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEmit')."
    CNAE: str
    CNPJCPF: str
    CRT: TpcnCRT
    EnderEmit: TenderEmit
    IE: str
    IEST: str
    IM: str
    ISUFEmit: str
    xFant: str
    xNome: str

class Tencerrante(TypedDict, total=False):
    "Entrada parcial de Tencerrante, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TencerranteOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tencerrante')."
    nBico: int
    nBomba: int
    nTanque: int
    vEncFin: str
    vEncIni: str

class TEnderDest(TypedDict, total=False):
    "Entrada parcial de TEnderDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TEnderDestOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEnderDest')."
    CEP: int
    cMun: int
    cPais: int
    fone: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xPais: str

class TenderEmit(TypedDict, total=False):
    "Entrada parcial de TenderEmit, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TenderEmitOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TenderEmit')."
    CEP: int
    cMun: int
    cPais: int
    fone: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xPais: str

class TEntrega(TypedDict, total=False):
    "Entrada parcial de TEntrega, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TEntregaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEntrega')."
    CEP: int
    cMun: int
    CNPJCPF: str
    cPais: int
    Email: str
    fone: str
    IE: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xNome: str
    xPais: str

class TExporta(TypedDict, total=False):
    "Entrada parcial de TExporta, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TExportaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TExporta')."
    UFembarq: str
    UFSaidaPais: str
    xLocDespacho: str
    xLocEmbarq: str
    xLocExporta: str

class TFat(TypedDict, total=False):
    "Entrada parcial de TFat, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TFatOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TFat')."
    nFat: str
    vDesc: str
    vLiq: str
    vOrig: str

class TForDiaCollectionItem(TypedDict, total=False):
    "Entrada parcial de TForDiaCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TForDiaCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TForDiaCollectionItem')."
    dia: int
    qtde: str

class TgAjusteCompet(TypedDict, total=False):
    "Entrada parcial de TgAjusteCompet, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgAjusteCompetOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgAjusteCompet')."
    competApur: str
    vCBS: str
    vIBS: str

class TgALCZFMCBS(TypedDict, total=False):
    "Entrada parcial de TgALCZFMCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgALCZFMCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgALCZFMCBS')."
    nProcSuframa: str
    pAliqEfetRegCBS: str
    tpALCZFMCBS: TtpALCZFMCBS
    vTribRegCBS: str

class TgCBS(TypedDict, total=False):
    "Entrada parcial de TgCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBS')."
    vCBS: str
    vCredPres: str
    vCredPresCondSus: str
    vDevTrib: str
    vDif: str

class TgCBSMonoAdRem(TypedDict, total=False):
    "Entrada parcial de TgCBSMonoAdRem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCBSMonoAdRemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSMonoAdRem')."
    gMonoPadrao: TgMonoPadraoCBSQtde
    gMonoRet: TgMonoRetCBS
    gMonoReten: TgMonoRetenCBSQtde
    gpBioDiferenca: TgpBioDiferencaCBS

class TgCBSMonoAdValorem(TypedDict, total=False):
    "Entrada parcial de TgCBSMonoAdValorem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCBSMonoAdValoremOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSMonoAdValorem')."
    gMonoPadrao: TgMonoPadraoCBSAliq
    gMonoRet: TgMonoRetCBS
    gMonoReten: TgMonoRetenCBSAliq
    gpBioDiferenca: TgpBioDiferencaCBS

class TgCBSValores(TypedDict, total=False):
    "Entrada parcial de TgCBSValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCBSValoresOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSValores')."
    gALCZFMCBS: TgALCZFMCBS
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pCBS: str
    vCBS: str

class TgCompraGov(TypedDict, total=False):
    "Entrada parcial de TgCompraGov, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCompraGovOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCompraGov')."
    pRedutor: str
    refDFeAnt: TDFErefCollection
    tpEnteGov: TtpEnteGov
    tpOperGov: TtpOperGov

class TgCredPresOper(TypedDict, total=False):
    "Entrada parcial de TgCredPresOper, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgCredPresOperOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCredPresOper')."
    cCredPres: TcCredPres
    gCBSCredPres: TgIBSCBSCredPres
    gIBSCredPres: TgIBSCBSCredPres
    vBCCredPres: str

class TgDevTrib(TypedDict, total=False):
    "Entrada parcial de TgDevTrib, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgDevTribOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgDevTrib')."
    pDevTrib: str
    vDevTrib: str

class TgDif(TypedDict, total=False):
    "Entrada parcial de TgDif, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgDifOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgDif')."
    pDif: str
    vDif: str

class TgEstornoCred(TypedDict, total=False):
    "Entrada parcial de TgEstornoCred, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgEstornoCredOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgEstornoCred')."
    vCBSEstCred: str
    vIBSEstCred: str

class TgIBS(TypedDict, total=False):
    "Entrada parcial de TgIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBS')."
    gIBSMunTot: TgIBSMunTot
    gIBSUFTot: TgIBSUFTot
    vCredPres: str
    vCredPresCondSus: str
    vIBS: str

class TgIBSCBS(TypedDict, total=False):
    "Entrada parcial de TgIBSCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBS')."
    gCBS: TgCBSValores
    gIBSMun: TgIBSMunValores
    gIBSUF: TgIBSUFValores
    gTribCompraGov: TgTribCompraGov
    gTribRegular: TgTribRegular
    vBC: str
    vIBS: str
    vOperacIndiv: str
    vRedAjusteIndiv: str
    vRedSocialIndiv: str
    vTornaIndiv: str

class TgIBSCBSCredPres(TypedDict, total=False):
    "Entrada parcial de TgIBSCBSCredPres, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSCBSCredPresOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBSCredPres')."
    pCredPres: str
    vCredPres: str
    vCredPresCondSus: str

class TgIBSCBSMono(TypedDict, total=False):
    "Entrada parcial de TgIBSCBSMono, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSCBSMonoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBSMono')."
    gCBSMonoAdRem: TgCBSMonoAdRem
    gCBSMonoAdValorem: TgCBSMonoAdValorem
    gIBSMonoAdRem: TgIBSMonoAdRem
    gIBSMonoAdValorem: TgIBSMonoAdValorem
    vTotCBSMonoItem: str
    vTotIBSMonoItem: str

class TgIBSMonoAdRem(TypedDict, total=False):
    "Entrada parcial de TgIBSMonoAdRem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSMonoAdRemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMonoAdRem')."
    gMonoPadrao: TgMonoPadraoIBSQtde
    gMonoRet: TgMonoRetIBS
    gMonoReten: TgMonoRetenIBSQtde
    gpBioDiferenca: TgpBioDiferencaIBS

class TgIBSMonoAdValorem(TypedDict, total=False):
    "Entrada parcial de TgIBSMonoAdValorem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSMonoAdValoremOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMonoAdValorem')."
    gMonoPadrao: TgMonoPadraoIBSAliq
    gMonoRet: TgMonoRetIBS
    gMonoReten: TgMonoRetenIBSAliq
    gpBioDiferenca: TgpBioDiferencaIBS

class TgIBSMunTot(TypedDict, total=False):
    "Entrada parcial de TgIBSMunTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSMunTotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMunTot')."
    vDevTrib: str
    vDif: str
    vIBSMun: str

class TgIBSMunValores(TypedDict, total=False):
    "Entrada parcial de TgIBSMunValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSMunValoresOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMunValores')."
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pIBSMun: str
    vIBSMun: str

class TgIBSUFTot(TypedDict, total=False):
    "Entrada parcial de TgIBSUFTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSUFTotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSUFTot')."
    vDevTrib: str
    vDif: str
    vIBSUF: str

class TgIBSUFValores(TypedDict, total=False):
    "Entrada parcial de TgIBSUFValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgIBSUFValoresOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSUFValores')."
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pIBSUF: str
    vIBSUF: str

class TgIS(TypedDict, total=False):
    "Entrada parcial de TgIS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgISOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIS')."
    adRemIS: str
    cClassTribIS: str
    CSTIS: str
    pIS: str
    qTrib: str
    uTrib: str
    vBCIS: str
    vIS: str

class TgMono(TypedDict, total=False):
    "Entrada parcial de TgMono, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMono')."
    vCBSMono: str
    vCBSMonoRet: str
    vCBSMonoReten: str
    vIBSMono: str
    vIBSMonoRet: str
    vIBSMonoReten: str

class TgMonoPadraoCBSAliq(TypedDict, total=False):
    "Entrada parcial de TgMonoPadraoCBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoPadraoCBSAliqOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoCBSAliq')."
    pAliqMonoCBS: str
    vBCMono: str
    vCBSMono: str

class TgMonoPadraoCBSQtde(TypedDict, total=False):
    "Entrada parcial de TgMonoPadraoCBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoPadraoCBSQtdeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoCBSQtde')."
    adRemCBS: str
    qBCMono: str
    vCBSMono: str

class TgMonoPadraoIBSAliq(TypedDict, total=False):
    "Entrada parcial de TgMonoPadraoIBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoPadraoIBSAliqOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoIBSAliq')."
    pAliqMonoMun: str
    pAliqMonoUF: str
    vBCMono: str
    vIBSMono: str
    vIBSMonoMun: str
    vIBSMonoUF: str

class TgMonoPadraoIBSQtde(TypedDict, total=False):
    "Entrada parcial de TgMonoPadraoIBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoPadraoIBSQtdeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoIBSQtde')."
    adRemIBS: str
    qBCMono: str
    vIBSMono: str

class TgMonoRetCBS(TypedDict, total=False):
    "Entrada parcial de TgMonoRetCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetCBS')."
    vCBSMonoRet: str

class TgMonoRetenCBSAliq(TypedDict, total=False):
    "Entrada parcial de TgMonoRetenCBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetenCBSAliqOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenCBSAliq')."
    pAliqMonoReten: str
    vBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenCBSQtde(TypedDict, total=False):
    "Entrada parcial de TgMonoRetenCBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetenCBSQtdeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenCBSQtde')."
    adRemCBSReten: str
    qBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenIBSAliq(TypedDict, total=False):
    "Entrada parcial de TgMonoRetenIBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetenIBSAliqOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenIBSAliq')."
    pAliqMonoReten: str
    vBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetenIBSQtde(TypedDict, total=False):
    "Entrada parcial de TgMonoRetenIBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetenIBSQtdeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenIBSQtde')."
    adRemIBSReten: str
    qBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetIBS(TypedDict, total=False):
    "Entrada parcial de TgMonoRetIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgMonoRetIBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetIBS')."
    vIBSMonoRet: str

class TgPagAntecipado(TypedDict, total=False):
    "Entrada parcial de TgPagAntecipado, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgPagAntecipadoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgPagAntecipado')."
    refNFe: TrefDFePagAntCollection

class TgpBioDiferencaCBS(TypedDict, total=False):
    "Entrada parcial de TgpBioDiferencaCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgpBioDiferencaCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgpBioDiferencaCBS')."
    qBCBioComb: str
    vCBSDiferenca: str

class TgpBioDiferencaIBS(TypedDict, total=False):
    "Entrada parcial de TgpBioDiferencaIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgpBioDiferencaIBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgpBioDiferencaIBS')."
    qBCBioComb: str
    vIBSDiferenca: str

class TgRed(TypedDict, total=False):
    "Entrada parcial de TgRed, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgRedOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgRed')."
    pAliqEfet: str
    pRedAliq: str

class TgTransfCred(TypedDict, total=False):
    "Entrada parcial de TgTransfCred, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgTransfCredOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTransfCred')."
    vCBS: str
    vIBS: str

class TgTribCompraGov(TypedDict, total=False):
    "Entrada parcial de TgTribCompraGov, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgTribCompraGovOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTribCompraGov')."
    pAliqCBS: str
    pAliqIBSMun: str
    pAliqIBSUF: str
    vTribCBS: str
    vTribIBSMun: str
    vTribIBSUF: str

class TgTribRegular(TypedDict, total=False):
    "Entrada parcial de TgTribRegular, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TgTribRegularOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTribRegular')."
    cClassTribReg: str
    CSTReg: TCSTIBSCBS
    pAliqEfetRegCBS: str
    pAliqEfetRegIBSMun: str
    pAliqEfetRegIBSUF: str
    vTribRegCBS: str
    vTribRegIBSMun: str
    vTribRegIBSUF: str

class TguiaTransito(TypedDict, total=False):
    "Entrada parcial de TguiaTransito, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TguiaTransitoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TguiaTransito')."
    nGuia: str
    serieGuia: str
    tpGuia: TtpGuia
    UFGuia: str

class TIBSCBS(TypedDict, total=False):
    "Entrada parcial de TIBSCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TIBSCBSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIBSCBS')."
    cClassTrib: str
    CST: TCSTIBSCBS
    gAjusteCompet: TgAjusteCompet
    gCredPresIBSZFM: TCredPresIBSZFM
    gCredPresOper: TgCredPresOper
    gEstornoCred: TgEstornoCred
    gIBSCBS: TgIBSCBS
    gIBSCBSMono: TgIBSCBSMono
    gTransfCred: TgTransfCred
    indDoacao: TIndicadorEx

class TIBSCBSTot(TypedDict, total=False):
    "Entrada parcial de TIBSCBSTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TIBSCBSTotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIBSCBSTot')."
    gCBS: TgCBS
    gEstornoCred: TgEstornoCred
    gIBS: TgIBS
    gMono: TgMono
    vBCIBSCBS: str

class TICMS(TypedDict, total=False):
    "Entrada parcial de TICMS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMS')."
    adRemICMS: str
    adRemICMSDif: str
    adRemICMSRet: str
    adRemICMSReten: str
    cBenefRBC: str
    CSOSN: TCSOSNIcms
    CST: TCSTIcms
    indDeduzDeson: TIndicadorEx
    modBC: TpcnDeterminacaoBaseIcms
    modBCST: TpcnDeterminacaoBaseIcmsST
    motDesICMS: TpcnMotivoDesoneracaoICMS
    motDesICMSST: TpcnMotivoDesoneracaoICMS
    motRedAdRem: TmotRedAdRem
    orig: TOrigemMercadoria
    pBCOp: str
    pCredSN: str
    pDif: str
    pFCP: str
    pFCPDif: str
    pFCPST: str
    pFCPSTRet: str
    pICMS: str
    pICMSEfet: str
    pICMSST: str
    pMVAST: str
    pRedAdRem: str
    pRedBC: str
    pRedBCEfet: str
    pRedBCST: str
    pST: str
    qBCMono: str
    qBCMonoDif: str
    qBCMonoRet: str
    qBCMonoReten: str
    UFST: str
    vBC: str
    vBCEfet: str
    vBCFCP: str
    vBCFCPST: str
    vBCFCPSTRet: str
    vBCST: str
    vBCSTDest: str
    vBCSTRet: str
    vCredICMSSN: str
    vFCP: str
    vFCPDif: str
    vFCPEfet: str
    vFCPST: str
    vFCPSTRet: str
    vICMS: str
    vICMSDeson: str
    vICMSDif: str
    vICMSEfet: str
    vICMSMono: str
    vICMSMonoDif: str
    vICMSMonoOp: str
    vICMSMonoRet: str
    vICMSMonoReten: str
    vICMSOp: str
    vICMSST: str
    vICMSSTDeson: str
    vICMSSTDest: str
    vICMSSTRet: str
    vICMSSubstituto: str

class TICMSComb(TypedDict, total=False):
    "Entrada parcial de TICMSComb, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSCombOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSComb')."
    vBCICMS: str
    vBCICMSST: str
    vICMS: str
    vICMSST: str

class TICMSCons(TypedDict, total=False):
    "Entrada parcial de TICMSCons, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSConsOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSCons')."
    UFcons: str
    vBCICMSSTCons: str
    vICMSSTCons: str

class TICMSInter(TypedDict, total=False):
    "Entrada parcial de TICMSInter, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSInterOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSInter')."
    vBCICMSSTDest: str
    vICMSSTDest: str

class TICMSTot(TypedDict, total=False):
    "Entrada parcial de TICMSTot, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSTotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSTot')."
    qBCMono: str
    qBCMonoRet: str
    qBCMonoReten: str
    vBC: str
    vBCST: str
    vCOFINS: str
    vDesc: str
    vFCP: str
    vFCPST: str
    vFCPSTRet: str
    vFCPUFDest: str
    vFrete: str
    vICMS: str
    vICMSDeson: str
    vICMSMono: str
    vICMSMonoRet: str
    vICMSMonoReten: str
    vICMSUFDest: str
    vICMSUFRemet: str
    vII: str
    vIPI: str
    vIPIDevol: str
    vNF: str
    vOutro: str
    vPIS: str
    vProd: str
    vSeg: str
    vST: str
    vTotTrib: str

class TICMSUFDest(TypedDict, total=False):
    "Entrada parcial de TICMSUFDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TICMSUFDestOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSUFDest')."
    pFCPUFDest: str
    pICMSInter: str
    pICMSInterPart: str
    pICMSUFDest: str
    vBCFCPUFDest: str
    vBCUFDest: str
    vFCPUFDest: str
    vICMSUFDest: str
    vICMSUFRemet: str

class TIde(TypedDict, total=False):
    "Entrada parcial de TIde, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TIdeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIde')."
    cDV: int
    cIndOp: str
    cMunFG: int
    cMunFGIBS: int
    cNF: int
    cUF: int
    dEmi: str
    dhCont: str
    dPrevEntrega: str
    dSaiEnt: str
    finNFe: TpcnFinalidadeNFe
    gCompraGov: TgCompraGov
    gPagAntecipado: TgPagAntecipado
    hSaiEnt: str
    idDest: TpcnDestinoOperacao
    indFinal: TpcnConsumidorFinal
    indIntermed: TindIntermed
    indPag: TpcnIndicadorPagamento
    indPres: TpcnPresencaComprador
    modelo: int
    natOp: str
    NFref: TNFrefCollection
    nNF: int
    procEmi: TACBrProcessoEmissao
    serie: int
    tpAmb: TACBrTipoAmbiente
    tpEmis: TACBrTipoEmissao
    tpImp: TACBrTipoImpressao
    tpNF: TTipoNFe
    tpNFCredito: TtpNFCredito
    tpNFDebito: TtpNFDebito
    verProc: str
    xJust: str

class TII(TypedDict, total=False):
    "Entrada parcial de TII, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TIIOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TII')."
    vBc: str
    vDespAdu: str
    vII: str
    vIOF: str

class TImposto(TypedDict, total=False):
    "Entrada parcial de TImposto, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TImpostoOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TImposto')."
    COFINS: TCOFINS
    COFINSST: TCOFINSST
    IBSCBS: TIBSCBS
    ICMS: TICMS
    ICMSUFDest: TICMSUFDest
    II: TII
    IPI: TIPI
    ISel: TgIS
    ISSQN: TISSQN
    PIS: TPIS
    PISST: TPISST
    vTotTrib: str

class TInfAdic(TypedDict, total=False):
    "Entrada parcial de TInfAdic, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TInfAdicOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TInfAdic')."
    infAdFisco: str
    infCpl: str
    obsCont: TobsContCollection
    obsFisco: TobsFiscoCollection
    procRef: TprocRefCollection

class TinfIntermed(TypedDict, total=False):
    "Entrada parcial de TinfIntermed, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TinfIntermedOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfIntermed')."
    CNPJ: str
    idCadIntTran: str

class TinfNFe(TypedDict, total=False):
    "Entrada parcial de TinfNFe, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TinfNFeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfNFe')."
    ID: str
    Versao: str

class TinfNFeSupl(TypedDict, total=False):
    "Entrada parcial de TinfNFeSupl, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TinfNFeSuplOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfNFeSupl')."
    qrCode: str
    urlChave: str

class TinfPAA(TypedDict, total=False):
    "Entrada parcial de TinfPAA, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TinfPAAOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfPAA')."
    CNPJPAA: str
    Exponent: str
    Modulus: str
    SignatureValue: str

class TinfRespTec(TypedDict, total=False):
    "Entrada parcial de TinfRespTec, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TinfRespTecOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfRespTec')."
    CNPJ: str
    email: str
    fone: str
    hashCSRT: str
    idCSRT: int
    xContato: str

class TIPI(TypedDict, total=False):
    "Entrada parcial de TIPI, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TIPIOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIPI')."
    cEnq: str
    clEnq: str
    CNPJProd: str
    cSelo: str
    CST: TpcnCstIpi
    pIPI: str
    qSelo: int
    qUnid: str
    vBC: str
    vIPI: str
    vUnid: str

class TISSQN(TypedDict, total=False):
    "Entrada parcial de TISSQN, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TISSQNOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISSQN')."
    cListServ: str
    cMun: int
    cMunFG: int
    cPais: int
    cServico: str
    cSitTrib: TpcnISSQNcSitTrib
    indIncentivo: TindIncentivo
    indISS: TpcnindISS
    indISSRet: TpcnindISSRet
    nProcesso: str
    vAliq: str
    vBC: str
    vDeducao: str
    vDescCond: str
    vDescIncond: str
    vISSQN: str
    vISSRet: str
    vOutro: str

class TISSQNtot(TypedDict, total=False):
    "Entrada parcial de TISSQNtot, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TISSQNtotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISSQNtot')."
    cRegTrib: TRegTribISSQN
    dCompet: str
    vBC: str
    vCOFINS: str
    vDeducao: str
    vDescCond: str
    vDescIncond: str
    vISS: str
    vISSRet: str
    vOutro: str
    vPIS: str
    vServ: str

class TISTot(TypedDict, total=False):
    "Entrada parcial de TISTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TISTotOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISTot')."
    vIS: str

class TLacresCollectionItem(TypedDict, total=False):
    "Entrada parcial de TLacresCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TLacresCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TLacresCollectionItem')."
    nLacre: str

class TMedCollectionItem(TypedDict, total=False):
    "Entrada parcial de TMedCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TMedCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TMedCollectionItem')."
    cProdANVISA: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str
    vPMC: str
    xMotivoIsencao: str

class TNFe(TypedDict, total=False):
    "Entrada parcial de TNFe, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TNFeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNFe')."
    agropecuario: Tagropecuario
    autXML: TautXMLCollection
    Avulsa: TAvulsa
    cana: Tcana
    Cobr: TCobr
    compra: TCompra
    Dest: TDest
    Det: TDetCollection
    Emit: TEmit
    Entrega: TEntrega
    exporta: TExporta
    Ide: TIde
    InfAdic: TInfAdic
    infIntermed: TinfIntermed
    infNFe: TinfNFe
    infPAA: TinfPAA
    infRespTec: TinfRespTec
    pag: TpagCollection
    Retirada: TRetirada
    Total: TTotal
    Transp: TTransp

class TNFrefCollectionItem(TypedDict, total=False):
    "Entrada parcial de TNFrefCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TNFrefCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNFrefCollectionItem')."
    refCTe: str
    RefECF: TRefECF
    RefNF: TRefNF
    refNFe: str
    refNFeSig: str
    RefNFP: TRefNFP

class TNVECollectionItem(TypedDict, total=False):
    "Entrada parcial de TNVECollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TNVECollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNVECollectionItem')."
    NVE: str

class TobsContCollectionItem(TypedDict, total=False):
    "Entrada parcial de TobsContCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TobsContCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsContCollectionItem')."
    xCampo: str
    xTexto: str

class TobsFiscoCollectionItem(TypedDict, total=False):
    "Entrada parcial de TobsFiscoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TobsFiscoCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsFiscoCollectionItem')."
    xCampo: str
    xTexto: str

class TobsItem(TypedDict, total=False):
    "Entrada parcial de TobsItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TobsItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsItem')."
    xCampo: str
    xTexto: str

class TorigCombCollectionItem(TypedDict, total=False):
    "Entrada parcial de TorigCombCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TorigCombCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TorigCombCollectionItem')."
    cUFOrig: int
    indImport: TindImport
    pOrig: str

class TpagCollectionItem(TypedDict, total=False):
    "Entrada parcial de TpagCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TpagCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TpagCollectionItem')."
    cAut: str
    CNPJ: str
    CNPJPag: str
    CNPJReceb: str
    dPag: str
    idTermPag: str
    indPag: TpcnIndicadorPagamento
    tBand: TpcnBandeiraCartao
    tPag: TpcnFormaPagamento
    tpIntegra: TtpIntegra
    UFPag: str
    vPag: str
    xPag: str

class TPIS(TypedDict, total=False):
    "Entrada parcial de TPIS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TPISOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TPIS')."
    CST: TCSTPis
    pPIS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vPIS: str

class TPISST(TypedDict, total=False):
    "Entrada parcial de TPISST, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TPISSTOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TPISST')."
    indSomaPISST: TIndSomaPISST
    pPis: str
    qBCProd: str
    vAliqProd: str
    vBc: str
    vPIS: str

class TProcDFe(TypedDict, total=False):
    "Entrada parcial de TProcDFe, unidade ACBrDFeComum.Proc.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TProcDFeOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TProcDFe')."
    chDFe: str
    cMsg: int
    cStat: int
    dhRecbto: str
    digVal: str
    Id: str
    nProt: str
    PathDFe: str
    PathRetConsReciDFe: str
    PathRetConsSitDFe: str
    tpAmb: TACBrTipoAmbiente
    verAplic: str
    XML_DFe: str
    XML_prot: str
    xMotivo: str
    xMsg: str

class TprocRefCollectionItem(TypedDict, total=False):
    "Entrada parcial de TprocRefCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TprocRefCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TprocRefCollectionItem')."
    indProc: TpcnIndicadorProcesso
    nProc: str
    tpAto: TtpAto

class TProd(TypedDict, total=False):
    "Entrada parcial de TProd, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TProdOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TProd')."
    arma: TArmaCollection
    cBarra: str
    cBarraTrib: str
    cBenef: str
    cEAN: str
    cEANTrib: str
    CEST: str
    CFOP: str
    CNPJFab: str
    comb: TComb
    cProd: str
    CredPresumido: TCredPresumidoCollection
    detExport: TdetExportCollection
    DI: TDICollection
    EXTIPI: str
    indBemMovelUsado: TIndicadorEx
    indEscala: TpcnIndEscala
    IndTot: TpcnIndicadorTotal
    med: TMedCollection
    NCM: str
    nFCI: str
    nItem: int
    nItemPed: str
    nRECOPI: str
    NVE: TNVECollection
    qCom: str
    qTrib: str
    rastro: TRastroCollection
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    uCom: str
    uTrib: str
    vDesc: str
    veicProd: TveicProd
    vFrete: str
    vOutro: str
    vProd: str
    vSeg: str
    vUnCom: str
    vUnTrib: str
    xPed: str
    xProd: str

class TRastroCollectionItem(TypedDict, total=False):
    "Entrada parcial de TRastroCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TRastroCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRastroCollectionItem')."
    cAgreg: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str

class TReboqueCollectionItem(TypedDict, total=False):
    "Entrada parcial de TReboqueCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TReboqueCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TReboqueCollectionItem')."
    placa: str
    RNTC: str
    UF: str

class TrefDFePagAntCollectionItem(TypedDict, total=False):
    "Entrada parcial de TrefDFePagAntCollectionItem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TrefDFePagAntCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TrefDFePagAntCollectionItem')."
    refDFEChave: str

class TRefECF(TypedDict, total=False):
    "Entrada parcial de TRefECF, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TRefECFOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefECF')."
    modelo: TpcnECFModRef
    nCOO: str
    nECF: str

class TRefNF(TypedDict, total=False):
    "Entrada parcial de TRefNF, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TRefNFOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefNF')."
    AAMM: str
    CNPJ: str
    cUF: int
    modelo: int
    nNF: int
    serie: int

class TRefNFP(TypedDict, total=False):
    "Entrada parcial de TRefNFP, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TRefNFPOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefNFP')."
    AAMM: str
    CNPJCPF: str
    cUF: int
    IE: str
    modelo: str
    nNF: int
    serie: int

class TRetirada(TypedDict, total=False):
    "Entrada parcial de TRetirada, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TRetiradaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRetirada')."
    CEP: int
    cMun: int
    CNPJCPF: str
    cPais: int
    Email: str
    fone: str
    IE: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xNome: str
    xPais: str

class TretTransp(TypedDict, total=False):
    "Entrada parcial de TretTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TretTranspOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TretTransp')."
    CFOP: str
    cMunFG: int
    pICMSRet: str
    vBCRet: str
    vICMSRet: str
    vServ: str

class TretTrib(TypedDict, total=False):
    "Entrada parcial de TretTrib, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TretTribOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TretTrib')."
    vBCIRRF: str
    vBCRetPrev: str
    vIRRF: str
    vRetCOFINS: str
    vRetCSLL: str
    vRetPIS: str
    vRetPrev: str

class TSignature(TypedDict, total=False):
    "Entrada parcial de TSignature, unidade ACBrXmlBase.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TSignatureOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TSignature')."
    DigestValue: str
    IdSignature: str
    IdSignatureValue: str
    SignatureValue: str
    URI: str
    X509Certificate: str

class TTotal(TypedDict, total=False):
    "Entrada parcial de TTotal, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TTotalOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTotal')."
    IBSCBSTot: TIBSCBSTot
    ICMSTot: TICMSTot
    ISSQNtot: TISSQNtot
    ISTot: TISTot
    retTrib: TretTrib
    vNFTot: str

class TTransp(TypedDict, total=False):
    "Entrada parcial de TTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TTranspOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTransp')."
    balsa: str
    modFrete: TpcnModalidadeFrete
    Reboque: TReboqueCollection
    retTransp: TretTransp
    Transporta: TTransporta
    vagao: str
    veicTransp: TveicTransp
    Vol: TVolCollection

class TTransporta(TypedDict, total=False):
    "Entrada parcial de TTransporta, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TTransportaOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTransporta')."
    CNPJCPF: str
    IE: str
    UF: str
    xEnder: str
    xMun: str
    xNome: str

class TveicProd(TypedDict, total=False):
    "Entrada parcial de TveicProd, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TveicProdOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TveicProd')."
    anoFab: int
    anoMod: int
    cCor: str
    cCorDENATRAN: str
    chassi: str
    Cilin: str
    cMod: str
    CMT: str
    condVeic: TpcnCondicaoVeiculo
    dist: str
    espVeic: int
    lota: int
    nMotor: str
    nSerie: str
    pesoB: str
    pesoL: str
    pot: str
    tpComb: str
    tpOP: TpcnTipoOperacao
    tpPint: str
    tpRest: int
    tpVeic: int
    VIN: str
    xCor: str

class TveicTransp(TypedDict, total=False):
    "Entrada parcial de TveicTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TveicTranspOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TveicTransp')."
    placa: str
    RNTC: str
    UF: str

class TVolCollectionItem(TypedDict, total=False):
    "Entrada parcial de TVolCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nOmite propriedades somente leitura; TVolCollectionItemOutput admite todas.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TVolCollectionItem')."
    esp: str
    Lacres: TLacresCollection
    marca: str
    nVol: str
    pesoB: str
    pesoL: str
    qVol: int

TAdiCollection: TypeAlias = list["TAdiCollectionItem"]

TArmaCollection: TypeAlias = list["TArmaCollectionItem"]

TautXMLCollection: TypeAlias = list["TautXMLCollectionItem"]

TCredPresumidoCollection: TypeAlias = list["TCredPresumidoCollectionItem"]

TDeducCollection: TypeAlias = list["TDeducCollectionItem"]

TdefensivoCollection: TypeAlias = list["TdefensivoCollectionItem"]

TDetCollection: TypeAlias = list["TDetCollectionItem"]

TdetExportCollection: TypeAlias = list["TdetExportCollectionItem"]

TDFErefCollection: TypeAlias = list["TDFErefCollectionItem"]

TDICollection: TypeAlias = list["TDICollectionItem"]

TDupCollection: TypeAlias = list["TDupCollectionItem"]

TForDiaCollection: TypeAlias = list["TForDiaCollectionItem"]

TLacresCollection: TypeAlias = list["TLacresCollectionItem"]

TMedCollection: TypeAlias = list["TMedCollectionItem"]

TNFrefCollection: TypeAlias = list["TNFrefCollectionItem"]

TNVECollection: TypeAlias = list["TNVECollectionItem"]

TobsContCollection: TypeAlias = list["TobsContCollectionItem"]

TobsFiscoCollection: TypeAlias = list["TobsFiscoCollectionItem"]

TorigCombCollection: TypeAlias = list["TorigCombCollectionItem"]

TpagCollection: TypeAlias = list["TpagCollectionItem"]

TprocRefCollection: TypeAlias = list["TprocRefCollectionItem"]

TRastroCollection: TypeAlias = list["TRastroCollectionItem"]

TReboqueCollection: TypeAlias = list["TReboqueCollectionItem"]

TrefDFePagAntCollection: TypeAlias = list["TrefDFePagAntCollectionItem"]

TVolCollection: TypeAlias = list["TVolCollectionItem"]

class TAdiCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TAdiCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TAdiCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TAdiCollectionItem')."
    cFabricante: str
    nAdicao: int
    nDraw: str
    nSeqAdi: int
    vDescDI: str

class TagropecuarioOutput(TypedDict, total=False):
    "Saída parcial de Tagropecuario, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use Tagropecuario para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tagropecuario')."
    defensivo: TdefensivoCollectionOutput
    guiaTransito: TguiaTransitoOutput

class TArmaCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TArmaCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TArmaCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TArmaCollectionItem')."
    descr: str
    nCano: str
    nSerie: str
    tpArma: TpcnTipoArma

class TautXMLCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TautXMLCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TautXMLCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TautXMLCollectionItem')."
    CNPJCPF: str

class TAvulsaOutput(TypedDict, total=False):
    "Saída parcial de TAvulsa, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TAvulsa para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TAvulsa')."
    CNPJ: str
    dEmi: str
    dPag: str
    fone: str
    matr: str
    nDAR: str
    repEmi: str
    UF: str
    vDAR: str
    xAgente: str
    xOrgao: str

class TcanaOutput(TypedDict, total=False):
    "Saída parcial de Tcana, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use Tcana para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tcana')."
    deduc: TDeducCollectionOutput
    fordia: TForDiaCollectionOutput
    qTotAnt: str
    qTotGer: str
    qTotMes: str
    ref: str
    safra: str
    vFor: str
    vLiqFor: str
    vTotDed: str

class TCIDEOutput(TypedDict, total=False):
    "Saída parcial de TCIDE, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCIDE para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCIDE')."
    qBCProd: str
    vAliqProd: str
    vCIDE: str

class TCobrOutput(TypedDict, total=False):
    "Saída parcial de TCobr, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCobr para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCobr')."
    Dup: TDupCollectionOutput
    Fat: TFatOutput

class TCOFINSOutput(TypedDict, total=False):
    "Saída parcial de TCOFINS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCOFINS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCOFINS')."
    CST: TCSTCofins
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vBCProd: str
    vCOFINS: str

class TCOFINSSTOutput(TypedDict, total=False):
    "Saída parcial de TCOFINSST, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCOFINSST para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCOFINSST')."
    indSomaCOFINSST: TIndSomaCOFINSST
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vCOFINS: str

class TCombOutput(TypedDict, total=False):
    "Saída parcial de TComb, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TComb para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TComb')."
    CIDE: TCIDEOutput
    CODIF: str
    cProdANP: int
    descANP: str
    encerrante: TencerranteOutput
    ICMS: TICMSCombOutput
    ICMSCons: TICMSConsOutput
    ICMSInter: TICMSInterOutput
    origComb: TorigCombCollectionOutput
    pBio: str
    pGLP: str
    pGNi: str
    pGNn: str
    pMixGN: str
    qTemp: str
    UFcons: str
    vPart: str

class TCompraOutput(TypedDict, total=False):
    "Saída parcial de TCompra, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCompra para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCompra')."
    xCont: str
    xNEmp: str
    xPed: str

class TCredPresIBSZFMOutput(TypedDict, total=False):
    "Saída parcial de TCredPresIBSZFM, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCredPresIBSZFM para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCredPresIBSZFM')."
    competApur: str
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    vCredPresIBSZFM: str

class TCredPresumidoCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TCredPresumidoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TCredPresumidoCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TCredPresumidoCollectionItem')."
    cCredPresumido: str
    pCredPresumido: str
    vCredPresumido: str

class TDeducCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TDeducCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDeducCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDeducCollectionItem')."
    vDed: str
    xDed: str

class TdefensivoCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TdefensivoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TdefensivoCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TdefensivoCollectionItem')."
    CPFRespTec: str
    nReceituario: str

class TDestOutput(TypedDict, total=False):
    "Saída parcial de TDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDest para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDest')."
    CNPJCPF: str
    Email: str
    EnderDest: TEnderDestOutput
    idEstrangeiro: str
    IE: str
    IM: str
    indIEDest: TindIEDest
    ISUF: str
    xNome: str

class TDetCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TDetCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDetCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDetCollectionItem')."
    DFeReferenciado: TDFeReferenciadoOutput
    Imposto: TImpostoOutput
    infAdProd: str
    obsCont: TobsItemOutput
    obsFisco: TobsItemOutput
    pDevol: str
    Prod: TProdOutput
    vIPIDevol: str
    vItem: str

class TdetExportCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TdetExportCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TdetExportCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TdetExportCollectionItem')."
    chNFe: str
    nDraw: str
    nRE: str
    qExport: str

class TDFErefCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TDFErefCollectionItem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDFErefCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDFErefCollectionItem')."
    refDFeChave: str

class TDFeReferenciadoOutput(TypedDict, total=False):
    "Saída parcial de TDFeReferenciado, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDFeReferenciado para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDFeReferenciado')."
    chaveAcesso: str
    nItem: int

class TDICollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TDICollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDICollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDICollectionItem')."
    adi: TAdiCollectionOutput
    cExportador: str
    CNPJ: str
    dDesemb: str
    dDi: str
    nDi: str
    tpIntermedio: TpcnTipoIntermedio
    tpViaTransp: TpcnTipoViaTransp
    UFDesemb: str
    UFTerceiro: str
    vAFRMM: str
    xLocDesemb: str

class TDupCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TDupCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TDupCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TDupCollectionItem')."
    dVenc: str
    nDup: str
    vDup: str

class TEmitOutput(TypedDict, total=False):
    "Saída parcial de TEmit, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TEmit para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEmit')."
    CNAE: str
    CNPJCPF: str
    CRT: TpcnCRT
    EnderEmit: TenderEmitOutput
    IE: str
    IEST: str
    IM: str
    ISUFEmit: str
    xFant: str
    xNome: str

class TencerranteOutput(TypedDict, total=False):
    "Saída parcial de Tencerrante, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use Tencerrante para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('Tencerrante')."
    nBico: int
    nBomba: int
    nTanque: int
    vEncFin: str
    vEncIni: str

class TEnderDestOutput(TypedDict, total=False):
    "Saída parcial de TEnderDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TEnderDest para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEnderDest')."
    CEP: int
    cMun: int
    cPais: int
    fone: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xPais: str

class TenderEmitOutput(TypedDict, total=False):
    "Saída parcial de TenderEmit, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TenderEmit para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TenderEmit')."
    CEP: int
    cMun: int
    cPais: int
    fone: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xPais: str

class TEntregaOutput(TypedDict, total=False):
    "Saída parcial de TEntrega, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TEntrega para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TEntrega')."
    CEP: int
    cMun: int
    CNPJCPF: str
    cPais: int
    Email: str
    fone: str
    IE: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xNome: str
    xPais: str

class TExportaOutput(TypedDict, total=False):
    "Saída parcial de TExporta, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TExporta para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TExporta')."
    UFembarq: str
    UFSaidaPais: str
    xLocDespacho: str
    xLocEmbarq: str
    xLocExporta: str

class TFatOutput(TypedDict, total=False):
    "Saída parcial de TFat, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TFat para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TFat')."
    nFat: str
    vDesc: str
    vLiq: str
    vOrig: str

class TForDiaCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TForDiaCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TForDiaCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TForDiaCollectionItem')."
    dia: int
    qtde: str

class TgAjusteCompetOutput(TypedDict, total=False):
    "Saída parcial de TgAjusteCompet, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgAjusteCompet para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgAjusteCompet')."
    competApur: str
    vCBS: str
    vIBS: str

class TgALCZFMCBSOutput(TypedDict, total=False):
    "Saída parcial de TgALCZFMCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgALCZFMCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgALCZFMCBS')."
    nProcSuframa: str
    pAliqEfetRegCBS: str
    tpALCZFMCBS: TtpALCZFMCBS
    vTribRegCBS: str

class TgCBSOutput(TypedDict, total=False):
    "Saída parcial de TgCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBS')."
    vCBS: str
    vCredPres: str
    vCredPresCondSus: str
    vDevTrib: str
    vDif: str

class TgCBSMonoAdRemOutput(TypedDict, total=False):
    "Saída parcial de TgCBSMonoAdRem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCBSMonoAdRem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSMonoAdRem')."
    gMonoPadrao: TgMonoPadraoCBSQtdeOutput
    gMonoRet: TgMonoRetCBSOutput
    gMonoReten: TgMonoRetenCBSQtdeOutput
    gpBioDiferenca: TgpBioDiferencaCBSOutput

class TgCBSMonoAdValoremOutput(TypedDict, total=False):
    "Saída parcial de TgCBSMonoAdValorem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCBSMonoAdValorem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSMonoAdValorem')."
    gMonoPadrao: TgMonoPadraoCBSAliqOutput
    gMonoRet: TgMonoRetCBSOutput
    gMonoReten: TgMonoRetenCBSAliqOutput
    gpBioDiferenca: TgpBioDiferencaCBSOutput

class TgCBSValoresOutput(TypedDict, total=False):
    "Saída parcial de TgCBSValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCBSValores para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCBSValores')."
    gALCZFMCBS: TgALCZFMCBSOutput
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pCBS: str
    vCBS: str

class TgCompraGovOutput(TypedDict, total=False):
    "Saída parcial de TgCompraGov, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCompraGov para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCompraGov')."
    pRedutor: str
    refDFeAnt: TDFErefCollectionOutput
    tpEnteGov: TtpEnteGov
    tpOperGov: TtpOperGov

class TgCredPresOperOutput(TypedDict, total=False):
    "Saída parcial de TgCredPresOper, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgCredPresOper para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgCredPresOper')."
    cCredPres: TcCredPres
    gCBSCredPres: TgIBSCBSCredPresOutput
    gIBSCredPres: TgIBSCBSCredPresOutput
    vBCCredPres: str

class TgDevTribOutput(TypedDict, total=False):
    "Saída parcial de TgDevTrib, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgDevTrib para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgDevTrib')."
    pDevTrib: str
    vDevTrib: str

class TgDifOutput(TypedDict, total=False):
    "Saída parcial de TgDif, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgDif para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgDif')."
    pDif: str
    vDif: str

class TgEstornoCredOutput(TypedDict, total=False):
    "Saída parcial de TgEstornoCred, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgEstornoCred para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgEstornoCred')."
    vCBSEstCred: str
    vIBSEstCred: str

class TgIBSOutput(TypedDict, total=False):
    "Saída parcial de TgIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBS')."
    gIBSMunTot: TgIBSMunTotOutput
    gIBSUFTot: TgIBSUFTotOutput
    vCredPres: str
    vCredPresCondSus: str
    vIBS: str

class TgIBSCBSOutput(TypedDict, total=False):
    "Saída parcial de TgIBSCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBS')."
    gCBS: TgCBSValoresOutput
    gIBSMun: TgIBSMunValoresOutput
    gIBSUF: TgIBSUFValoresOutput
    gTribCompraGov: TgTribCompraGovOutput
    gTribRegular: TgTribRegularOutput
    vBC: str
    vIBS: str
    vOperacIndiv: str
    vRedAjusteIndiv: str
    vRedSocialIndiv: str
    vTornaIndiv: str

class TgIBSCBSCredPresOutput(TypedDict, total=False):
    "Saída parcial de TgIBSCBSCredPres, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSCBSCredPres para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBSCredPres')."
    pCredPres: str
    vCredPres: str
    vCredPresCondSus: str

class TgIBSCBSMonoOutput(TypedDict, total=False):
    "Saída parcial de TgIBSCBSMono, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSCBSMono para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSCBSMono')."
    gCBSMonoAdRem: TgCBSMonoAdRemOutput
    gCBSMonoAdValorem: TgCBSMonoAdValoremOutput
    gIBSMonoAdRem: TgIBSMonoAdRemOutput
    gIBSMonoAdValorem: TgIBSMonoAdValoremOutput
    vTotCBSMonoItem: str
    vTotIBSMonoItem: str

class TgIBSMonoAdRemOutput(TypedDict, total=False):
    "Saída parcial de TgIBSMonoAdRem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSMonoAdRem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMonoAdRem')."
    gMonoPadrao: TgMonoPadraoIBSQtdeOutput
    gMonoRet: TgMonoRetIBSOutput
    gMonoReten: TgMonoRetenIBSQtdeOutput
    gpBioDiferenca: TgpBioDiferencaIBSOutput

class TgIBSMonoAdValoremOutput(TypedDict, total=False):
    "Saída parcial de TgIBSMonoAdValorem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSMonoAdValorem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMonoAdValorem')."
    gMonoPadrao: TgMonoPadraoIBSAliqOutput
    gMonoRet: TgMonoRetIBSOutput
    gMonoReten: TgMonoRetenIBSAliqOutput
    gpBioDiferenca: TgpBioDiferencaIBSOutput

class TgIBSMunTotOutput(TypedDict, total=False):
    "Saída parcial de TgIBSMunTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSMunTot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMunTot')."
    vDevTrib: str
    vDif: str
    vIBSMun: str

class TgIBSMunValoresOutput(TypedDict, total=False):
    "Saída parcial de TgIBSMunValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSMunValores para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSMunValores')."
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pIBSMun: str
    vIBSMun: str

class TgIBSUFTotOutput(TypedDict, total=False):
    "Saída parcial de TgIBSUFTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSUFTot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSUFTot')."
    vDevTrib: str
    vDif: str
    vIBSUF: str

class TgIBSUFValoresOutput(TypedDict, total=False):
    "Saída parcial de TgIBSUFValores, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIBSUFValores para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIBSUFValores')."
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pIBSUF: str
    vIBSUF: str

class TgISOutput(TypedDict, total=False):
    "Saída parcial de TgIS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgIS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgIS')."
    adRemIS: str
    cClassTribIS: str
    CSTIS: str
    pIS: str
    qTrib: str
    uTrib: str
    vBCIS: str
    vIS: str

class TgMonoOutput(TypedDict, total=False):
    "Saída parcial de TgMono, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMono para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMono')."
    vCBSMono: str
    vCBSMonoRet: str
    vCBSMonoReten: str
    vIBSMono: str
    vIBSMonoRet: str
    vIBSMonoReten: str

class TgMonoPadraoCBSAliqOutput(TypedDict, total=False):
    "Saída parcial de TgMonoPadraoCBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoPadraoCBSAliq para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoCBSAliq')."
    pAliqMonoCBS: str
    vBCMono: str
    vCBSMono: str

class TgMonoPadraoCBSQtdeOutput(TypedDict, total=False):
    "Saída parcial de TgMonoPadraoCBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoPadraoCBSQtde para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoCBSQtde')."
    adRemCBS: str
    qBCMono: str
    vCBSMono: str

class TgMonoPadraoIBSAliqOutput(TypedDict, total=False):
    "Saída parcial de TgMonoPadraoIBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoPadraoIBSAliq para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoIBSAliq')."
    pAliqMonoMun: str
    pAliqMonoUF: str
    vBCMono: str
    vIBSMono: str
    vIBSMonoMun: str
    vIBSMonoUF: str

class TgMonoPadraoIBSQtdeOutput(TypedDict, total=False):
    "Saída parcial de TgMonoPadraoIBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoPadraoIBSQtde para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoPadraoIBSQtde')."
    adRemIBS: str
    qBCMono: str
    vIBSMono: str

class TgMonoRetCBSOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetCBS')."
    vCBSMonoRet: str

class TgMonoRetenCBSAliqOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetenCBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetenCBSAliq para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenCBSAliq')."
    pAliqMonoReten: str
    vBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenCBSQtdeOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetenCBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetenCBSQtde para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenCBSQtde')."
    adRemCBSReten: str
    qBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenIBSAliqOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetenIBSAliq, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetenIBSAliq para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenIBSAliq')."
    pAliqMonoReten: str
    vBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetenIBSQtdeOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetenIBSQtde, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetenIBSQtde para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetenIBSQtde')."
    adRemIBSReten: str
    qBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetIBSOutput(TypedDict, total=False):
    "Saída parcial de TgMonoRetIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgMonoRetIBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgMonoRetIBS')."
    vIBSMonoRet: str

class TgPagAntecipadoOutput(TypedDict, total=False):
    "Saída parcial de TgPagAntecipado, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgPagAntecipado para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgPagAntecipado')."
    refNFe: TrefDFePagAntCollectionOutput

class TgpBioDiferencaCBSOutput(TypedDict, total=False):
    "Saída parcial de TgpBioDiferencaCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgpBioDiferencaCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgpBioDiferencaCBS')."
    qBCBioComb: str
    vCBSDiferenca: str

class TgpBioDiferencaIBSOutput(TypedDict, total=False):
    "Saída parcial de TgpBioDiferencaIBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgpBioDiferencaIBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgpBioDiferencaIBS')."
    qBCBioComb: str
    vIBSDiferenca: str

class TgRedOutput(TypedDict, total=False):
    "Saída parcial de TgRed, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgRed para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgRed')."
    pAliqEfet: str
    pRedAliq: str

class TgTransfCredOutput(TypedDict, total=False):
    "Saída parcial de TgTransfCred, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgTransfCred para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTransfCred')."
    vCBS: str
    vIBS: str

class TgTribCompraGovOutput(TypedDict, total=False):
    "Saída parcial de TgTribCompraGov, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgTribCompraGov para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTribCompraGov')."
    pAliqCBS: str
    pAliqIBSMun: str
    pAliqIBSUF: str
    vTribCBS: str
    vTribIBSMun: str
    vTribIBSUF: str

class TgTribRegularOutput(TypedDict, total=False):
    "Saída parcial de TgTribRegular, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TgTribRegular para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TgTribRegular')."
    cClassTribReg: str
    CSTReg: TCSTIBSCBS
    pAliqEfetRegCBS: str
    pAliqEfetRegIBSMun: str
    pAliqEfetRegIBSUF: str
    vTribRegCBS: str
    vTribRegIBSMun: str
    vTribRegIBSUF: str

class TguiaTransitoOutput(TypedDict, total=False):
    "Saída parcial de TguiaTransito, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TguiaTransito para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TguiaTransito')."
    nGuia: str
    serieGuia: str
    tpGuia: TtpGuia
    UFGuia: str

class TIBSCBSOutput(TypedDict, total=False):
    "Saída parcial de TIBSCBS, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TIBSCBS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIBSCBS')."
    cClassTrib: str
    CST: TCSTIBSCBS
    gAjusteCompet: TgAjusteCompetOutput
    gCredPresIBSZFM: TCredPresIBSZFMOutput
    gCredPresOper: TgCredPresOperOutput
    gEstornoCred: TgEstornoCredOutput
    gIBSCBS: TgIBSCBSOutput
    gIBSCBSMono: TgIBSCBSMonoOutput
    gTransfCred: TgTransfCredOutput
    indDoacao: TIndicadorEx

class TIBSCBSTotOutput(TypedDict, total=False):
    "Saída parcial de TIBSCBSTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TIBSCBSTot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIBSCBSTot')."
    gCBS: TgCBSOutput
    gEstornoCred: TgEstornoCredOutput
    gIBS: TgIBSOutput
    gMono: TgMonoOutput
    vBCIBSCBS: str

class TICMSOutput(TypedDict, total=False):
    "Saída parcial de TICMS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMS')."
    adRemICMS: str
    adRemICMSDif: str
    adRemICMSRet: str
    adRemICMSReten: str
    cBenefRBC: str
    CSOSN: TCSOSNIcms
    CST: TCSTIcms
    indDeduzDeson: TIndicadorEx
    modBC: TpcnDeterminacaoBaseIcms
    modBCST: TpcnDeterminacaoBaseIcmsST
    motDesICMS: TpcnMotivoDesoneracaoICMS
    motDesICMSST: TpcnMotivoDesoneracaoICMS
    motRedAdRem: TmotRedAdRem
    orig: TOrigemMercadoria
    pBCOp: str
    pCredSN: str
    pDif: str
    pFCP: str
    pFCPDif: str
    pFCPST: str
    pFCPSTRet: str
    pICMS: str
    pICMSEfet: str
    pICMSST: str
    pMVAST: str
    pRedAdRem: str
    pRedBC: str
    pRedBCEfet: str
    pRedBCST: str
    pST: str
    qBCMono: str
    qBCMonoDif: str
    qBCMonoRet: str
    qBCMonoReten: str
    UFST: str
    vBC: str
    vBCEfet: str
    vBCFCP: str
    vBCFCPST: str
    vBCFCPSTRet: str
    vBCST: str
    vBCSTDest: str
    vBCSTRet: str
    vCredICMSSN: str
    vFCP: str
    vFCPDif: str
    vFCPEfet: str
    vFCPST: str
    vFCPSTRet: str
    vICMS: str
    vICMSDeson: str
    vICMSDif: str
    vICMSEfet: str
    vICMSMono: str
    vICMSMonoDif: str
    vICMSMonoOp: str
    vICMSMonoRet: str
    vICMSMonoReten: str
    vICMSOp: str
    vICMSST: str
    vICMSSTDeson: str
    vICMSSTDest: str
    vICMSSTRet: str
    vICMSSubstituto: str

class TICMSCombOutput(TypedDict, total=False):
    "Saída parcial de TICMSComb, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMSComb para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSComb')."
    vBCICMS: str
    vBCICMSST: str
    vICMS: str
    vICMSST: str

class TICMSConsOutput(TypedDict, total=False):
    "Saída parcial de TICMSCons, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMSCons para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSCons')."
    UFcons: str
    vBCICMSSTCons: str
    vICMSSTCons: str

class TICMSInterOutput(TypedDict, total=False):
    "Saída parcial de TICMSInter, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMSInter para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSInter')."
    vBCICMSSTDest: str
    vICMSSTDest: str

class TICMSTotOutput(TypedDict, total=False):
    "Saída parcial de TICMSTot, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMSTot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSTot')."
    qBCMono: str
    qBCMonoRet: str
    qBCMonoReten: str
    vBC: str
    vBCST: str
    vCOFINS: str
    vDesc: str
    vFCP: str
    vFCPST: str
    vFCPSTRet: str
    vFCPUFDest: str
    vFrete: str
    vICMS: str
    vICMSDeson: str
    vICMSMono: str
    vICMSMonoRet: str
    vICMSMonoReten: str
    vICMSUFDest: str
    vICMSUFRemet: str
    vII: str
    vIPI: str
    vIPIDevol: str
    vNF: str
    vOutro: str
    vPIS: str
    vProd: str
    vSeg: str
    vST: str
    vTotTrib: str

class TICMSUFDestOutput(TypedDict, total=False):
    "Saída parcial de TICMSUFDest, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TICMSUFDest para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TICMSUFDest')."
    pFCPUFDest: str
    pICMSInter: str
    pICMSInterPart: str
    pICMSUFDest: str
    vBCFCPUFDest: str
    vBCUFDest: str
    vFCPUFDest: str
    vICMSUFDest: str
    vICMSUFRemet: str

class TIdeOutput(TypedDict, total=False):
    "Saída parcial de TIde, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TIde para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIde')."
    cDV: int
    cIndOp: str
    cMunFG: int
    cMunFGIBS: int
    cNF: int
    cUF: int
    dEmi: str
    dhCont: str
    dPrevEntrega: str
    dSaiEnt: str
    finNFe: TpcnFinalidadeNFe
    gCompraGov: TgCompraGovOutput
    gPagAntecipado: TgPagAntecipadoOutput
    hSaiEnt: str
    idDest: TpcnDestinoOperacao
    indFinal: TpcnConsumidorFinal
    indIntermed: TindIntermed
    indPag: TpcnIndicadorPagamento
    indPres: TpcnPresencaComprador
    modelo: int
    natOp: str
    NFref: TNFrefCollectionOutput
    nNF: int
    procEmi: TACBrProcessoEmissao
    serie: int
    tpAmb: TACBrTipoAmbiente
    tpEmis: TACBrTipoEmissao
    tpImp: TACBrTipoImpressao
    tpNF: TTipoNFe
    tpNFCredito: TtpNFCredito
    tpNFDebito: TtpNFDebito
    verProc: str
    xJust: str

class TIIOutput(TypedDict, total=False):
    "Saída parcial de TII, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TII para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TII')."
    vBc: str
    vDespAdu: str
    vII: str
    vIOF: str

class TImpostoOutput(TypedDict, total=False):
    "Saída parcial de TImposto, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TImposto para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TImposto')."
    COFINS: TCOFINSOutput
    COFINSST: TCOFINSSTOutput
    IBSCBS: TIBSCBSOutput
    ICMS: TICMSOutput
    ICMSUFDest: TICMSUFDestOutput
    II: TIIOutput
    IPI: TIPIOutput
    ISel: TgISOutput
    ISSQN: TISSQNOutput
    PIS: TPISOutput
    PISST: TPISSTOutput
    vTotTrib: str

class TInfAdicOutput(TypedDict, total=False):
    "Saída parcial de TInfAdic, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TInfAdic para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TInfAdic')."
    infAdFisco: str
    infCpl: str
    obsCont: TobsContCollectionOutput
    obsFisco: TobsFiscoCollectionOutput
    procRef: TprocRefCollectionOutput

class TinfIntermedOutput(TypedDict, total=False):
    "Saída parcial de TinfIntermed, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TinfIntermed para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfIntermed')."
    CNPJ: str
    idCadIntTran: str

class TinfNFeOutput(TypedDict, total=False):
    "Saída parcial de TinfNFe, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TinfNFe para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfNFe')."
    ID: str
    Versao: str

class TinfNFeSuplOutput(TypedDict, total=False):
    "Saída parcial de TinfNFeSupl, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TinfNFeSupl para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfNFeSupl')."
    qrCode: str
    urlChave: str

class TinfPAAOutput(TypedDict, total=False):
    "Saída parcial de TinfPAA, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TinfPAA para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfPAA')."
    CNPJPAA: str
    Exponent: str
    Modulus: str
    SignatureValue: str

class TinfRespTecOutput(TypedDict, total=False):
    "Saída parcial de TinfRespTec, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TinfRespTec para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TinfRespTec')."
    CNPJ: str
    email: str
    fone: str
    hashCSRT: str
    idCSRT: int
    xContato: str

class TIPIOutput(TypedDict, total=False):
    "Saída parcial de TIPI, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TIPI para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TIPI')."
    cEnq: str
    clEnq: str
    CNPJProd: str
    cSelo: str
    CST: TpcnCstIpi
    pIPI: str
    qSelo: int
    qUnid: str
    vBC: str
    vIPI: str
    vUnid: str

class TISSQNOutput(TypedDict, total=False):
    "Saída parcial de TISSQN, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TISSQN para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISSQN')."
    cListServ: str
    cMun: int
    cMunFG: int
    cPais: int
    cServico: str
    cSitTrib: TpcnISSQNcSitTrib
    indIncentivo: TindIncentivo
    indISS: TpcnindISS
    indISSRet: TpcnindISSRet
    nProcesso: str
    vAliq: str
    vBC: str
    vDeducao: str
    vDescCond: str
    vDescIncond: str
    vISSQN: str
    vISSRet: str
    vOutro: str

class TISSQNtotOutput(TypedDict, total=False):
    "Saída parcial de TISSQNtot, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TISSQNtot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISSQNtot')."
    cRegTrib: TRegTribISSQN
    dCompet: str
    vBC: str
    vCOFINS: str
    vDeducao: str
    vDescCond: str
    vDescIncond: str
    vISS: str
    vISSRet: str
    vOutro: str
    vPIS: str
    vServ: str

class TISTotOutput(TypedDict, total=False):
    "Saída parcial de TISTot, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TISTot para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TISTot')."
    vIS: str

class TLacresCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TLacresCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TLacresCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TLacresCollectionItem')."
    nLacre: str

class TMedCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TMedCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TMedCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TMedCollectionItem')."
    cProdANVISA: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str
    vPMC: str
    xMotivoIsencao: str

class TNFeOutput(TypedDict, total=False):
    "Saída parcial de TNFe, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TNFe para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNFe')."
    agropecuario: TagropecuarioOutput
    autXML: TautXMLCollectionOutput
    Avulsa: TAvulsaOutput
    cana: TcanaOutput
    Cobr: TCobrOutput
    compra: TCompraOutput
    Dest: TDestOutput
    Det: TDetCollectionOutput
    Emit: TEmitOutput
    Entrega: TEntregaOutput
    exporta: TExportaOutput
    Ide: TIdeOutput
    InfAdic: TInfAdicOutput
    infIntermed: TinfIntermedOutput
    infNFe: TinfNFeOutput
    infNFeSupl: TinfNFeSuplOutput
    infPAA: TinfPAAOutput
    infRespTec: TinfRespTecOutput
    pag: TpagCollectionOutput
    procNFe: TProcDFeOutput
    Retirada: TRetiradaOutput
    signature: TSignatureOutput
    Total: TTotalOutput
    Transp: TTranspOutput

class TNFrefCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TNFrefCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TNFrefCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNFrefCollectionItem')."
    refCTe: str
    RefECF: TRefECFOutput
    RefNF: TRefNFOutput
    refNFe: str
    refNFeSig: str
    RefNFP: TRefNFPOutput

class TNVECollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TNVECollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TNVECollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TNVECollectionItem')."
    NVE: str

class TobsContCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TobsContCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TobsContCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsContCollectionItem')."
    xCampo: str
    xTexto: str

class TobsFiscoCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TobsFiscoCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TobsFiscoCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsFiscoCollectionItem')."
    xCampo: str
    xTexto: str

class TobsItemOutput(TypedDict, total=False):
    "Saída parcial de TobsItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TobsItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TobsItem')."
    xCampo: str
    xTexto: str

class TorigCombCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TorigCombCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TorigCombCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TorigCombCollectionItem')."
    cUFOrig: int
    indImport: TindImport
    pOrig: str

class TpagCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TpagCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TpagCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TpagCollectionItem')."
    cAut: str
    CNPJ: str
    CNPJPag: str
    CNPJReceb: str
    dPag: str
    idTermPag: str
    indPag: TpcnIndicadorPagamento
    tBand: TpcnBandeiraCartao
    tPag: TpcnFormaPagamento
    tpIntegra: TtpIntegra
    UFPag: str
    vPag: str
    xPag: str

class TPISOutput(TypedDict, total=False):
    "Saída parcial de TPIS, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TPIS para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TPIS')."
    CST: TCSTPis
    pPIS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vPIS: str

class TPISSTOutput(TypedDict, total=False):
    "Saída parcial de TPISST, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TPISST para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TPISST')."
    indSomaPISST: TIndSomaPISST
    pPis: str
    qBCProd: str
    vAliqProd: str
    vBc: str
    vPIS: str

class TProcDFeOutput(TypedDict, total=False):
    "Saída parcial de TProcDFe, unidade ACBrDFeComum.Proc.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TProcDFe para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TProcDFe')."
    chDFe: str
    cMsg: int
    cStat: int
    dhRecbto: str
    digVal: str
    Id: str
    nProt: str
    PathDFe: str
    PathRetConsReciDFe: str
    PathRetConsSitDFe: str
    tpAmb: TACBrTipoAmbiente
    verAplic: str
    XML_DFe: str
    XML_prot: str
    xMotivo: str
    xMsg: str

class TprocRefCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TprocRefCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TprocRefCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TprocRefCollectionItem')."
    indProc: TpcnIndicadorProcesso
    nProc: str
    tpAto: TtpAto

class TProdOutput(TypedDict, total=False):
    "Saída parcial de TProd, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TProd para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TProd')."
    arma: TArmaCollectionOutput
    cBarra: str
    cBarraTrib: str
    cBenef: str
    cEAN: str
    cEANTrib: str
    CEST: str
    CFOP: str
    CNPJFab: str
    comb: TCombOutput
    cProd: str
    CredPresumido: TCredPresumidoCollectionOutput
    detExport: TdetExportCollectionOutput
    DI: TDICollectionOutput
    EXTIPI: str
    indBemMovelUsado: TIndicadorEx
    indEscala: TpcnIndEscala
    IndTot: TpcnIndicadorTotal
    med: TMedCollectionOutput
    NCM: str
    nFCI: str
    nItem: int
    nItemPed: str
    nRECOPI: str
    NVE: TNVECollectionOutput
    qCom: str
    qTrib: str
    rastro: TRastroCollectionOutput
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    uCom: str
    uTrib: str
    vDesc: str
    veicProd: TveicProdOutput
    vFrete: str
    vOutro: str
    vProd: str
    vSeg: str
    vUnCom: str
    vUnTrib: str
    xPed: str
    xProd: str

class TRastroCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TRastroCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TRastroCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRastroCollectionItem')."
    cAgreg: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str

class TReboqueCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TReboqueCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TReboqueCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TReboqueCollectionItem')."
    placa: str
    RNTC: str
    UF: str

class TrefDFePagAntCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TrefDFePagAntCollectionItem, unidade ACBrDFe.RTC.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TrefDFePagAntCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TrefDFePagAntCollectionItem')."
    refDFEChave: str

class TRefECFOutput(TypedDict, total=False):
    "Saída parcial de TRefECF, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TRefECF para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefECF')."
    modelo: TpcnECFModRef
    nCOO: str
    nECF: str

class TRefNFOutput(TypedDict, total=False):
    "Saída parcial de TRefNF, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TRefNF para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefNF')."
    AAMM: str
    CNPJ: str
    cUF: int
    modelo: int
    nNF: int
    serie: int

class TRefNFPOutput(TypedDict, total=False):
    "Saída parcial de TRefNFP, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TRefNFP para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRefNFP')."
    AAMM: str
    CNPJCPF: str
    cUF: int
    IE: str
    modelo: str
    nNF: int
    serie: int

class TRetiradaOutput(TypedDict, total=False):
    "Saída parcial de TRetirada, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TRetirada para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TRetirada')."
    CEP: int
    cMun: int
    CNPJCPF: str
    cPais: int
    Email: str
    fone: str
    IE: str
    nro: str
    UF: str
    xBairro: str
    xCpl: str
    xLgr: str
    xMun: str
    xNome: str
    xPais: str

class TretTranspOutput(TypedDict, total=False):
    "Saída parcial de TretTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TretTransp para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TretTransp')."
    CFOP: str
    cMunFG: int
    pICMSRet: str
    vBCRet: str
    vICMSRet: str
    vServ: str

class TretTribOutput(TypedDict, total=False):
    "Saída parcial de TretTrib, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TretTrib para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TretTrib')."
    vBCIRRF: str
    vBCRetPrev: str
    vIRRF: str
    vRetCOFINS: str
    vRetCSLL: str
    vRetPIS: str
    vRetPrev: str

class TSignatureOutput(TypedDict, total=False):
    "Saída parcial de TSignature, unidade ACBrXmlBase.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TSignature para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TSignature')."
    DigestValue: str
    IdSignature: str
    IdSignatureValue: str
    SignatureValue: str
    URI: str
    X509Certificate: str

class TTotalOutput(TypedDict, total=False):
    "Saída parcial de TTotal, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TTotal para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTotal')."
    IBSCBSTot: TIBSCBSTotOutput
    ICMSTot: TICMSTotOutput
    ISSQNtot: TISSQNtotOutput
    ISTot: TISTotOutput
    retTrib: TretTribOutput
    vNFTot: str

class TTranspOutput(TypedDict, total=False):
    "Saída parcial de TTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TTransp para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTransp')."
    balsa: str
    modFrete: TpcnModalidadeFrete
    Reboque: TReboqueCollectionOutput
    retTransp: TretTranspOutput
    Transporta: TTransportaOutput
    vagao: str
    veicTransp: TveicTranspOutput
    Vol: TVolCollectionOutput

class TTransportaOutput(TypedDict, total=False):
    "Saída parcial de TTransporta, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TTransporta para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TTransporta')."
    CNPJCPF: str
    IE: str
    UF: str
    xEnder: str
    xMun: str
    xNome: str

class TveicProdOutput(TypedDict, total=False):
    "Saída parcial de TveicProd, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TveicProd para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TveicProd')."
    anoFab: int
    anoMod: int
    cCor: str
    cCorDENATRAN: str
    chassi: str
    Cilin: str
    cMod: str
    CMT: str
    CombDescricao: str
    condVeic: TpcnCondicaoVeiculo
    dist: str
    espVeic: int
    lota: int
    nMotor: str
    nSerie: str
    pesoB: str
    pesoL: str
    pot: str
    tpComb: str
    tpOP: TpcnTipoOperacao
    tpPint: str
    tpRest: int
    tpVeic: int
    VIN: str
    xCor: str

class TveicTranspOutput(TypedDict, total=False):
    "Saída parcial de TveicTransp, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TveicTransp para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TveicTransp')."
    placa: str
    RNTC: str
    UF: str

class TVolCollectionItemOutput(TypedDict, total=False):
    "Saída parcial de TVolCollectionItem, unidade ACBrNFe.Classes.\n\nTypedDict total=False: todos os membros são opcionais estruturalmente.\nAdmite propriedades somente leitura; use TVolCollectionItem para entrada.\nTypedDict não valida valores em execução.\nPara validar a estrutura de uma entrada TNFe, use acbr.validate_document.\nSchema e regras fiscais dependem do runtime ACBr.\nEnums usam strings Literal; decimais e datas/horários civis ISO usam str.\nMetadados do contrato: acbr.describe_type('TVolCollectionItem')."
    esp: str
    Lacres: TLacresCollectionOutput
    marca: str
    nVol: str
    pesoB: str
    pesoL: str
    qVol: int

TAdiCollectionOutput: TypeAlias = list["TAdiCollectionItemOutput"]

TArmaCollectionOutput: TypeAlias = list["TArmaCollectionItemOutput"]

TautXMLCollectionOutput: TypeAlias = list["TautXMLCollectionItemOutput"]

TCredPresumidoCollectionOutput: TypeAlias = list["TCredPresumidoCollectionItemOutput"]

TDeducCollectionOutput: TypeAlias = list["TDeducCollectionItemOutput"]

TdefensivoCollectionOutput: TypeAlias = list["TdefensivoCollectionItemOutput"]

TDetCollectionOutput: TypeAlias = list["TDetCollectionItemOutput"]

TdetExportCollectionOutput: TypeAlias = list["TdetExportCollectionItemOutput"]

TDFErefCollectionOutput: TypeAlias = list["TDFErefCollectionItemOutput"]

TDICollectionOutput: TypeAlias = list["TDICollectionItemOutput"]

TDupCollectionOutput: TypeAlias = list["TDupCollectionItemOutput"]

TForDiaCollectionOutput: TypeAlias = list["TForDiaCollectionItemOutput"]

TLacresCollectionOutput: TypeAlias = list["TLacresCollectionItemOutput"]

TMedCollectionOutput: TypeAlias = list["TMedCollectionItemOutput"]

TNFrefCollectionOutput: TypeAlias = list["TNFrefCollectionItemOutput"]

TNVECollectionOutput: TypeAlias = list["TNVECollectionItemOutput"]

TobsContCollectionOutput: TypeAlias = list["TobsContCollectionItemOutput"]

TobsFiscoCollectionOutput: TypeAlias = list["TobsFiscoCollectionItemOutput"]

TorigCombCollectionOutput: TypeAlias = list["TorigCombCollectionItemOutput"]

TpagCollectionOutput: TypeAlias = list["TpagCollectionItemOutput"]

TprocRefCollectionOutput: TypeAlias = list["TprocRefCollectionItemOutput"]

TRastroCollectionOutput: TypeAlias = list["TRastroCollectionItemOutput"]

TReboqueCollectionOutput: TypeAlias = list["TReboqueCollectionItemOutput"]

TrefDFePagAntCollectionOutput: TypeAlias = list["TrefDFePagAntCollectionItemOutput"]

TVolCollectionOutput: TypeAlias = list["TVolCollectionItemOutput"]

__all__ = [
    'TACBrProcessoEmissao',
    'TACBrTipoAmbiente',
    'TACBrTipoEmissao',
    'TACBrTipoImpressao',
    'TAdiCollection',
    'TAdiCollectionItem',
    'Tagropecuario',
    'TArmaCollection',
    'TArmaCollectionItem',
    'TautXMLCollection',
    'TautXMLCollectionItem',
    'TAvulsa',
    'Tcana',
    'TcCredPres',
    'TCIDE',
    'TCobr',
    'TCOFINS',
    'TCOFINSST',
    'TComb',
    'TCompra',
    'TCredPresIBSZFM',
    'TCredPresumidoCollection',
    'TCredPresumidoCollectionItem',
    'TCSOSNIcms',
    'TCSTCofins',
    'TCSTIBSCBS',
    'TCSTIcms',
    'TCSTPis',
    'TDeducCollection',
    'TDeducCollectionItem',
    'TdefensivoCollection',
    'TdefensivoCollectionItem',
    'TDest',
    'TDetCollection',
    'TDetCollectionItem',
    'TdetExportCollection',
    'TdetExportCollectionItem',
    'TDFErefCollection',
    'TDFErefCollectionItem',
    'TDFeReferenciado',
    'TDICollection',
    'TDICollectionItem',
    'TDupCollection',
    'TDupCollectionItem',
    'TEmit',
    'Tencerrante',
    'TEnderDest',
    'TenderEmit',
    'TEntrega',
    'TExporta',
    'TFat',
    'TForDiaCollection',
    'TForDiaCollectionItem',
    'TgAjusteCompet',
    'TgALCZFMCBS',
    'TgCBS',
    'TgCBSMonoAdRem',
    'TgCBSMonoAdValorem',
    'TgCBSValores',
    'TgCompraGov',
    'TgCredPresOper',
    'TgDevTrib',
    'TgDif',
    'TgEstornoCred',
    'TgIBS',
    'TgIBSCBS',
    'TgIBSCBSCredPres',
    'TgIBSCBSMono',
    'TgIBSMonoAdRem',
    'TgIBSMonoAdValorem',
    'TgIBSMunTot',
    'TgIBSMunValores',
    'TgIBSUFTot',
    'TgIBSUFValores',
    'TgIS',
    'TgMono',
    'TgMonoPadraoCBSAliq',
    'TgMonoPadraoCBSQtde',
    'TgMonoPadraoIBSAliq',
    'TgMonoPadraoIBSQtde',
    'TgMonoRetCBS',
    'TgMonoRetenCBSAliq',
    'TgMonoRetenCBSQtde',
    'TgMonoRetenIBSAliq',
    'TgMonoRetenIBSQtde',
    'TgMonoRetIBS',
    'TgPagAntecipado',
    'TgpBioDiferencaCBS',
    'TgpBioDiferencaIBS',
    'TgRed',
    'TgTransfCred',
    'TgTribCompraGov',
    'TgTribRegular',
    'TguiaTransito',
    'TIBSCBS',
    'TIBSCBSTot',
    'TICMS',
    'TICMSComb',
    'TICMSCons',
    'TICMSInter',
    'TICMSTot',
    'TICMSUFDest',
    'TIde',
    'TII',
    'TImposto',
    'TIndicadorEx',
    'TindIEDest',
    'TindImport',
    'TindIncentivo',
    'TindIntermed',
    'TIndSomaCOFINSST',
    'TIndSomaPISST',
    'TInfAdic',
    'TinfIntermed',
    'TinfNFe',
    'TinfNFeSupl',
    'TinfPAA',
    'TinfRespTec',
    'TIPI',
    'TISSQN',
    'TISSQNtot',
    'TISTot',
    'TLacresCollection',
    'TLacresCollectionItem',
    'TMedCollection',
    'TMedCollectionItem',
    'TmotRedAdRem',
    'TNFe',
    'TNFrefCollection',
    'TNFrefCollectionItem',
    'TNVECollection',
    'TNVECollectionItem',
    'TobsContCollection',
    'TobsContCollectionItem',
    'TobsFiscoCollection',
    'TobsFiscoCollectionItem',
    'TobsItem',
    'TorigCombCollection',
    'TorigCombCollectionItem',
    'TOrigemMercadoria',
    'TpagCollection',
    'TpagCollectionItem',
    'TpcnBandeiraCartao',
    'TpcnCondicaoVeiculo',
    'TpcnConsumidorFinal',
    'TpcnCRT',
    'TpcnCstIpi',
    'TpcnDestinoOperacao',
    'TpcnDeterminacaoBaseIcms',
    'TpcnDeterminacaoBaseIcmsST',
    'TpcnECFModRef',
    'TpcnFinalidadeNFe',
    'TpcnFormaPagamento',
    'TpcnIndEscala',
    'TpcnIndicadorPagamento',
    'TpcnIndicadorProcesso',
    'TpcnIndicadorTotal',
    'TpcnindISS',
    'TpcnindISSRet',
    'TpcnISSQNcSitTrib',
    'TpcnModalidadeFrete',
    'TpcnMotivoDesoneracaoICMS',
    'TpcnPresencaComprador',
    'TpcnTipoArma',
    'TpcnTipoIntermedio',
    'TpcnTipoOperacao',
    'TpcnTipoViaTransp',
    'TPIS',
    'TPISST',
    'TProcDFe',
    'TprocRefCollection',
    'TprocRefCollectionItem',
    'TProd',
    'TRastroCollection',
    'TRastroCollectionItem',
    'TReboqueCollection',
    'TReboqueCollectionItem',
    'TrefDFePagAntCollection',
    'TrefDFePagAntCollectionItem',
    'TRefECF',
    'TRefNF',
    'TRefNFP',
    'TRegTribISSQN',
    'TRetirada',
    'TretTransp',
    'TretTrib',
    'TSignature',
    'TTipoNFe',
    'TTotal',
    'TtpALCZFMCBS',
    'TtpAto',
    'TTpCredPresIBSZFM',
    'TtpEnteGov',
    'TtpGuia',
    'TtpIntegra',
    'TtpNFCredito',
    'TtpNFDebito',
    'TtpOperGov',
    'TTransp',
    'TTransporta',
    'TveicProd',
    'TveicTransp',
    'TVolCollection',
    'TVolCollectionItem',
    'TAdiCollectionOutput',
    'TAdiCollectionItemOutput',
    'TagropecuarioOutput',
    'TArmaCollectionOutput',
    'TArmaCollectionItemOutput',
    'TautXMLCollectionOutput',
    'TautXMLCollectionItemOutput',
    'TAvulsaOutput',
    'TcanaOutput',
    'TCIDEOutput',
    'TCobrOutput',
    'TCOFINSOutput',
    'TCOFINSSTOutput',
    'TCombOutput',
    'TCompraOutput',
    'TCredPresIBSZFMOutput',
    'TCredPresumidoCollectionOutput',
    'TCredPresumidoCollectionItemOutput',
    'TDeducCollectionOutput',
    'TDeducCollectionItemOutput',
    'TdefensivoCollectionOutput',
    'TdefensivoCollectionItemOutput',
    'TDestOutput',
    'TDetCollectionOutput',
    'TDetCollectionItemOutput',
    'TdetExportCollectionOutput',
    'TdetExportCollectionItemOutput',
    'TDFErefCollectionOutput',
    'TDFErefCollectionItemOutput',
    'TDFeReferenciadoOutput',
    'TDICollectionOutput',
    'TDICollectionItemOutput',
    'TDupCollectionOutput',
    'TDupCollectionItemOutput',
    'TEmitOutput',
    'TencerranteOutput',
    'TEnderDestOutput',
    'TenderEmitOutput',
    'TEntregaOutput',
    'TExportaOutput',
    'TFatOutput',
    'TForDiaCollectionOutput',
    'TForDiaCollectionItemOutput',
    'TgAjusteCompetOutput',
    'TgALCZFMCBSOutput',
    'TgCBSOutput',
    'TgCBSMonoAdRemOutput',
    'TgCBSMonoAdValoremOutput',
    'TgCBSValoresOutput',
    'TgCompraGovOutput',
    'TgCredPresOperOutput',
    'TgDevTribOutput',
    'TgDifOutput',
    'TgEstornoCredOutput',
    'TgIBSOutput',
    'TgIBSCBSOutput',
    'TgIBSCBSCredPresOutput',
    'TgIBSCBSMonoOutput',
    'TgIBSMonoAdRemOutput',
    'TgIBSMonoAdValoremOutput',
    'TgIBSMunTotOutput',
    'TgIBSMunValoresOutput',
    'TgIBSUFTotOutput',
    'TgIBSUFValoresOutput',
    'TgISOutput',
    'TgMonoOutput',
    'TgMonoPadraoCBSAliqOutput',
    'TgMonoPadraoCBSQtdeOutput',
    'TgMonoPadraoIBSAliqOutput',
    'TgMonoPadraoIBSQtdeOutput',
    'TgMonoRetCBSOutput',
    'TgMonoRetenCBSAliqOutput',
    'TgMonoRetenCBSQtdeOutput',
    'TgMonoRetenIBSAliqOutput',
    'TgMonoRetenIBSQtdeOutput',
    'TgMonoRetIBSOutput',
    'TgPagAntecipadoOutput',
    'TgpBioDiferencaCBSOutput',
    'TgpBioDiferencaIBSOutput',
    'TgRedOutput',
    'TgTransfCredOutput',
    'TgTribCompraGovOutput',
    'TgTribRegularOutput',
    'TguiaTransitoOutput',
    'TIBSCBSOutput',
    'TIBSCBSTotOutput',
    'TICMSOutput',
    'TICMSCombOutput',
    'TICMSConsOutput',
    'TICMSInterOutput',
    'TICMSTotOutput',
    'TICMSUFDestOutput',
    'TIdeOutput',
    'TIIOutput',
    'TImpostoOutput',
    'TInfAdicOutput',
    'TinfIntermedOutput',
    'TinfNFeOutput',
    'TinfNFeSuplOutput',
    'TinfPAAOutput',
    'TinfRespTecOutput',
    'TIPIOutput',
    'TISSQNOutput',
    'TISSQNtotOutput',
    'TISTotOutput',
    'TLacresCollectionOutput',
    'TLacresCollectionItemOutput',
    'TMedCollectionOutput',
    'TMedCollectionItemOutput',
    'TNFeOutput',
    'TNFrefCollectionOutput',
    'TNFrefCollectionItemOutput',
    'TNVECollectionOutput',
    'TNVECollectionItemOutput',
    'TobsContCollectionOutput',
    'TobsContCollectionItemOutput',
    'TobsFiscoCollectionOutput',
    'TobsFiscoCollectionItemOutput',
    'TobsItemOutput',
    'TorigCombCollectionOutput',
    'TorigCombCollectionItemOutput',
    'TpagCollectionOutput',
    'TpagCollectionItemOutput',
    'TPISOutput',
    'TPISSTOutput',
    'TProcDFeOutput',
    'TprocRefCollectionOutput',
    'TprocRefCollectionItemOutput',
    'TProdOutput',
    'TRastroCollectionOutput',
    'TRastroCollectionItemOutput',
    'TReboqueCollectionOutput',
    'TReboqueCollectionItemOutput',
    'TrefDFePagAntCollectionOutput',
    'TrefDFePagAntCollectionItemOutput',
    'TRefECFOutput',
    'TRefNFOutput',
    'TRefNFPOutput',
    'TRetiradaOutput',
    'TretTranspOutput',
    'TretTribOutput',
    'TSignatureOutput',
    'TTotalOutput',
    'TTranspOutput',
    'TTransportaOutput',
    'TveicProdOutput',
    'TveicTranspOutput',
    'TVolCollectionOutput',
    'TVolCollectionItemOutput',
]
