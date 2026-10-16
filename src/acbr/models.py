"""Generated ACBr wire types; edit tools/generate_models.py instead.

All input properties are optional; omitted values use native defaults.
Readonly properties occur only in Output types. Decimal and civil ISO
date/time values are strings. Runtime validation is in acbr.contract.
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
    cFabricante: str
    nAdicao: int
    nDraw: str
    nSeqAdi: int
    vDescDI: str

class Tagropecuario(TypedDict, total=False):
    defensivo: TdefensivoCollection
    guiaTransito: TguiaTransito

class TArmaCollectionItem(TypedDict, total=False):
    descr: str
    nCano: str
    nSerie: str
    tpArma: TpcnTipoArma

class TautXMLCollectionItem(TypedDict, total=False):
    CNPJCPF: str

class TAvulsa(TypedDict, total=False):
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
    qBCProd: str
    vAliqProd: str
    vCIDE: str

class TCobr(TypedDict, total=False):
    Dup: TDupCollection
    Fat: TFat

class TCOFINS(TypedDict, total=False):
    CST: TCSTCofins
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vBCProd: str
    vCOFINS: str

class TCOFINSST(TypedDict, total=False):
    indSomaCOFINSST: TIndSomaCOFINSST
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vCOFINS: str

class TComb(TypedDict, total=False):
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
    xCont: str
    xNEmp: str
    xPed: str

class TCredPresIBSZFM(TypedDict, total=False):
    competApur: str
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    vCredPresIBSZFM: str

class TCredPresumidoCollectionItem(TypedDict, total=False):
    cCredPresumido: str
    pCredPresumido: str
    vCredPresumido: str

class TDeducCollectionItem(TypedDict, total=False):
    vDed: str
    xDed: str

class TdefensivoCollectionItem(TypedDict, total=False):
    CPFRespTec: str
    nReceituario: str

class TDest(TypedDict, total=False):
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
    chNFe: str
    nDraw: str
    nRE: str
    qExport: str

class TDFErefCollectionItem(TypedDict, total=False):
    refDFeChave: str

class TDFeReferenciado(TypedDict, total=False):
    chaveAcesso: str
    nItem: int

class TDICollectionItem(TypedDict, total=False):
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
    dVenc: str
    nDup: str
    vDup: str

class TEmit(TypedDict, total=False):
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
    nBico: int
    nBomba: int
    nTanque: int
    vEncFin: str
    vEncIni: str

class TEnderDest(TypedDict, total=False):
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
    UFembarq: str
    UFSaidaPais: str
    xLocDespacho: str
    xLocEmbarq: str
    xLocExporta: str

class TFat(TypedDict, total=False):
    nFat: str
    vDesc: str
    vLiq: str
    vOrig: str

class TForDiaCollectionItem(TypedDict, total=False):
    dia: int
    qtde: str

class TgAjusteCompet(TypedDict, total=False):
    competApur: str
    vCBS: str
    vIBS: str

class TgALCZFMCBS(TypedDict, total=False):
    nProcSuframa: str
    pAliqEfetRegCBS: str
    tpALCZFMCBS: TtpALCZFMCBS
    vTribRegCBS: str

class TgCBS(TypedDict, total=False):
    vCBS: str
    vCredPres: str
    vCredPresCondSus: str
    vDevTrib: str
    vDif: str

class TgCBSMonoAdRem(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoCBSQtde
    gMonoRet: TgMonoRetCBS
    gMonoReten: TgMonoRetenCBSQtde
    gpBioDiferenca: TgpBioDiferencaCBS

class TgCBSMonoAdValorem(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoCBSAliq
    gMonoRet: TgMonoRetCBS
    gMonoReten: TgMonoRetenCBSAliq
    gpBioDiferenca: TgpBioDiferencaCBS

class TgCBSValores(TypedDict, total=False):
    gALCZFMCBS: TgALCZFMCBS
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pCBS: str
    vCBS: str

class TgCompraGov(TypedDict, total=False):
    pRedutor: str
    refDFeAnt: TDFErefCollection
    tpEnteGov: TtpEnteGov
    tpOperGov: TtpOperGov

class TgCredPresOper(TypedDict, total=False):
    cCredPres: TcCredPres
    gCBSCredPres: TgIBSCBSCredPres
    gIBSCredPres: TgIBSCBSCredPres
    vBCCredPres: str

class TgDevTrib(TypedDict, total=False):
    pDevTrib: str
    vDevTrib: str

class TgDif(TypedDict, total=False):
    pDif: str
    vDif: str

class TgEstornoCred(TypedDict, total=False):
    vCBSEstCred: str
    vIBSEstCred: str

class TgIBS(TypedDict, total=False):
    gIBSMunTot: TgIBSMunTot
    gIBSUFTot: TgIBSUFTot
    vCredPres: str
    vCredPresCondSus: str
    vIBS: str

class TgIBSCBS(TypedDict, total=False):
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
    pCredPres: str
    vCredPres: str
    vCredPresCondSus: str

class TgIBSCBSMono(TypedDict, total=False):
    gCBSMonoAdRem: TgCBSMonoAdRem
    gCBSMonoAdValorem: TgCBSMonoAdValorem
    gIBSMonoAdRem: TgIBSMonoAdRem
    gIBSMonoAdValorem: TgIBSMonoAdValorem
    vTotCBSMonoItem: str
    vTotIBSMonoItem: str

class TgIBSMonoAdRem(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoIBSQtde
    gMonoRet: TgMonoRetIBS
    gMonoReten: TgMonoRetenIBSQtde
    gpBioDiferenca: TgpBioDiferencaIBS

class TgIBSMonoAdValorem(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoIBSAliq
    gMonoRet: TgMonoRetIBS
    gMonoReten: TgMonoRetenIBSAliq
    gpBioDiferenca: TgpBioDiferencaIBS

class TgIBSMunTot(TypedDict, total=False):
    vDevTrib: str
    vDif: str
    vIBSMun: str

class TgIBSMunValores(TypedDict, total=False):
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pIBSMun: str
    vIBSMun: str

class TgIBSUFTot(TypedDict, total=False):
    vDevTrib: str
    vDif: str
    vIBSUF: str

class TgIBSUFValores(TypedDict, total=False):
    gDevTrib: TgDevTrib
    gDif: TgDif
    gRed: TgRed
    pIBSUF: str
    vIBSUF: str

class TgIS(TypedDict, total=False):
    adRemIS: str
    cClassTribIS: str
    CSTIS: str
    pIS: str
    qTrib: str
    uTrib: str
    vBCIS: str
    vIS: str

class TgMono(TypedDict, total=False):
    vCBSMono: str
    vCBSMonoRet: str
    vCBSMonoReten: str
    vIBSMono: str
    vIBSMonoRet: str
    vIBSMonoReten: str

class TgMonoPadraoCBSAliq(TypedDict, total=False):
    pAliqMonoCBS: str
    vBCMono: str
    vCBSMono: str

class TgMonoPadraoCBSQtde(TypedDict, total=False):
    adRemCBS: str
    qBCMono: str
    vCBSMono: str

class TgMonoPadraoIBSAliq(TypedDict, total=False):
    pAliqMonoMun: str
    pAliqMonoUF: str
    vBCMono: str
    vIBSMono: str
    vIBSMonoMun: str
    vIBSMonoUF: str

class TgMonoPadraoIBSQtde(TypedDict, total=False):
    adRemIBS: str
    qBCMono: str
    vIBSMono: str

class TgMonoRetCBS(TypedDict, total=False):
    vCBSMonoRet: str

class TgMonoRetenCBSAliq(TypedDict, total=False):
    pAliqMonoReten: str
    vBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenCBSQtde(TypedDict, total=False):
    adRemCBSReten: str
    qBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenIBSAliq(TypedDict, total=False):
    pAliqMonoReten: str
    vBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetenIBSQtde(TypedDict, total=False):
    adRemIBSReten: str
    qBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetIBS(TypedDict, total=False):
    vIBSMonoRet: str

class TgPagAntecipado(TypedDict, total=False):
    refNFe: TrefDFePagAntCollection

class TgpBioDiferencaCBS(TypedDict, total=False):
    qBCBioComb: str
    vCBSDiferenca: str

class TgpBioDiferencaIBS(TypedDict, total=False):
    qBCBioComb: str
    vIBSDiferenca: str

class TgRed(TypedDict, total=False):
    pAliqEfet: str
    pRedAliq: str

class TgTransfCred(TypedDict, total=False):
    vCBS: str
    vIBS: str

class TgTribCompraGov(TypedDict, total=False):
    pAliqCBS: str
    pAliqIBSMun: str
    pAliqIBSUF: str
    vTribCBS: str
    vTribIBSMun: str
    vTribIBSUF: str

class TgTribRegular(TypedDict, total=False):
    cClassTribReg: str
    CSTReg: TCSTIBSCBS
    pAliqEfetRegCBS: str
    pAliqEfetRegIBSMun: str
    pAliqEfetRegIBSUF: str
    vTribRegCBS: str
    vTribRegIBSMun: str
    vTribRegIBSUF: str

class TguiaTransito(TypedDict, total=False):
    nGuia: str
    serieGuia: str
    tpGuia: TtpGuia
    UFGuia: str

class TIBSCBS(TypedDict, total=False):
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
    gCBS: TgCBS
    gEstornoCred: TgEstornoCred
    gIBS: TgIBS
    gMono: TgMono
    vBCIBSCBS: str

class TICMS(TypedDict, total=False):
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
    vBCICMS: str
    vBCICMSST: str
    vICMS: str
    vICMSST: str

class TICMSCons(TypedDict, total=False):
    UFcons: str
    vBCICMSSTCons: str
    vICMSSTCons: str

class TICMSInter(TypedDict, total=False):
    vBCICMSSTDest: str
    vICMSSTDest: str

class TICMSTot(TypedDict, total=False):
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
    vBc: str
    vDespAdu: str
    vII: str
    vIOF: str

class TImposto(TypedDict, total=False):
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
    infAdFisco: str
    infCpl: str
    obsCont: TobsContCollection
    obsFisco: TobsFiscoCollection
    procRef: TprocRefCollection

class TinfIntermed(TypedDict, total=False):
    CNPJ: str
    idCadIntTran: str

class TinfNFe(TypedDict, total=False):
    ID: str
    Versao: str

class TinfNFeSupl(TypedDict, total=False):
    qrCode: str
    urlChave: str

class TinfPAA(TypedDict, total=False):
    CNPJPAA: str
    Exponent: str
    Modulus: str
    SignatureValue: str

class TinfRespTec(TypedDict, total=False):
    CNPJ: str
    email: str
    fone: str
    hashCSRT: str
    idCSRT: int
    xContato: str

class TIPI(TypedDict, total=False):
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
    vIS: str

class TLacresCollectionItem(TypedDict, total=False):
    nLacre: str

class TMedCollectionItem(TypedDict, total=False):
    cProdANVISA: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str
    vPMC: str
    xMotivoIsencao: str

class TNFe(TypedDict, total=False):
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
    refCTe: str
    RefECF: TRefECF
    RefNF: TRefNF
    refNFe: str
    refNFeSig: str
    RefNFP: TRefNFP

class TNVECollectionItem(TypedDict, total=False):
    NVE: str

class TobsContCollectionItem(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TobsFiscoCollectionItem(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TobsItem(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TorigCombCollectionItem(TypedDict, total=False):
    cUFOrig: int
    indImport: TindImport
    pOrig: str

class TpagCollectionItem(TypedDict, total=False):
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
    CST: TCSTPis
    pPIS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vPIS: str

class TPISST(TypedDict, total=False):
    indSomaPISST: TIndSomaPISST
    pPis: str
    qBCProd: str
    vAliqProd: str
    vBc: str
    vPIS: str

class TProcDFe(TypedDict, total=False):
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
    indProc: TpcnIndicadorProcesso
    nProc: str
    tpAto: TtpAto

class TProd(TypedDict, total=False):
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
    cAgreg: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str

class TReboqueCollectionItem(TypedDict, total=False):
    placa: str
    RNTC: str
    UF: str

class TrefDFePagAntCollectionItem(TypedDict, total=False):
    refDFEChave: str

class TRefECF(TypedDict, total=False):
    modelo: TpcnECFModRef
    nCOO: str
    nECF: str

class TRefNF(TypedDict, total=False):
    AAMM: str
    CNPJ: str
    cUF: int
    modelo: int
    nNF: int
    serie: int

class TRefNFP(TypedDict, total=False):
    AAMM: str
    CNPJCPF: str
    cUF: int
    IE: str
    modelo: str
    nNF: int
    serie: int

class TRetirada(TypedDict, total=False):
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
    CFOP: str
    cMunFG: int
    pICMSRet: str
    vBCRet: str
    vICMSRet: str
    vServ: str

class TretTrib(TypedDict, total=False):
    vBCIRRF: str
    vBCRetPrev: str
    vIRRF: str
    vRetCOFINS: str
    vRetCSLL: str
    vRetPIS: str
    vRetPrev: str

class TSignature(TypedDict, total=False):
    DigestValue: str
    IdSignature: str
    IdSignatureValue: str
    SignatureValue: str
    URI: str
    X509Certificate: str

class TTotal(TypedDict, total=False):
    IBSCBSTot: TIBSCBSTot
    ICMSTot: TICMSTot
    ISSQNtot: TISSQNtot
    ISTot: TISTot
    retTrib: TretTrib
    vNFTot: str

class TTransp(TypedDict, total=False):
    balsa: str
    modFrete: TpcnModalidadeFrete
    Reboque: TReboqueCollection
    retTransp: TretTransp
    Transporta: TTransporta
    vagao: str
    veicTransp: TveicTransp
    Vol: TVolCollection

class TTransporta(TypedDict, total=False):
    CNPJCPF: str
    IE: str
    UF: str
    xEnder: str
    xMun: str
    xNome: str

class TveicProd(TypedDict, total=False):
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
    placa: str
    RNTC: str
    UF: str

class TVolCollectionItem(TypedDict, total=False):
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
    cFabricante: str
    nAdicao: int
    nDraw: str
    nSeqAdi: int
    vDescDI: str

class TagropecuarioOutput(TypedDict, total=False):
    defensivo: TdefensivoCollectionOutput
    guiaTransito: TguiaTransitoOutput

class TArmaCollectionItemOutput(TypedDict, total=False):
    descr: str
    nCano: str
    nSerie: str
    tpArma: TpcnTipoArma

class TautXMLCollectionItemOutput(TypedDict, total=False):
    CNPJCPF: str

class TAvulsaOutput(TypedDict, total=False):
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
    qBCProd: str
    vAliqProd: str
    vCIDE: str

class TCobrOutput(TypedDict, total=False):
    Dup: TDupCollectionOutput
    Fat: TFatOutput

class TCOFINSOutput(TypedDict, total=False):
    CST: TCSTCofins
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vBCProd: str
    vCOFINS: str

class TCOFINSSTOutput(TypedDict, total=False):
    indSomaCOFINSST: TIndSomaCOFINSST
    pCOFINS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vCOFINS: str

class TCombOutput(TypedDict, total=False):
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
    xCont: str
    xNEmp: str
    xPed: str

class TCredPresIBSZFMOutput(TypedDict, total=False):
    competApur: str
    tpCredPresIBSZFM: TTpCredPresIBSZFM
    vCredPresIBSZFM: str

class TCredPresumidoCollectionItemOutput(TypedDict, total=False):
    cCredPresumido: str
    pCredPresumido: str
    vCredPresumido: str

class TDeducCollectionItemOutput(TypedDict, total=False):
    vDed: str
    xDed: str

class TdefensivoCollectionItemOutput(TypedDict, total=False):
    CPFRespTec: str
    nReceituario: str

class TDestOutput(TypedDict, total=False):
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
    chNFe: str
    nDraw: str
    nRE: str
    qExport: str

class TDFErefCollectionItemOutput(TypedDict, total=False):
    refDFeChave: str

class TDFeReferenciadoOutput(TypedDict, total=False):
    chaveAcesso: str
    nItem: int

class TDICollectionItemOutput(TypedDict, total=False):
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
    dVenc: str
    nDup: str
    vDup: str

class TEmitOutput(TypedDict, total=False):
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
    nBico: int
    nBomba: int
    nTanque: int
    vEncFin: str
    vEncIni: str

class TEnderDestOutput(TypedDict, total=False):
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
    UFembarq: str
    UFSaidaPais: str
    xLocDespacho: str
    xLocEmbarq: str
    xLocExporta: str

class TFatOutput(TypedDict, total=False):
    nFat: str
    vDesc: str
    vLiq: str
    vOrig: str

class TForDiaCollectionItemOutput(TypedDict, total=False):
    dia: int
    qtde: str

class TgAjusteCompetOutput(TypedDict, total=False):
    competApur: str
    vCBS: str
    vIBS: str

class TgALCZFMCBSOutput(TypedDict, total=False):
    nProcSuframa: str
    pAliqEfetRegCBS: str
    tpALCZFMCBS: TtpALCZFMCBS
    vTribRegCBS: str

class TgCBSOutput(TypedDict, total=False):
    vCBS: str
    vCredPres: str
    vCredPresCondSus: str
    vDevTrib: str
    vDif: str

class TgCBSMonoAdRemOutput(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoCBSQtdeOutput
    gMonoRet: TgMonoRetCBSOutput
    gMonoReten: TgMonoRetenCBSQtdeOutput
    gpBioDiferenca: TgpBioDiferencaCBSOutput

class TgCBSMonoAdValoremOutput(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoCBSAliqOutput
    gMonoRet: TgMonoRetCBSOutput
    gMonoReten: TgMonoRetenCBSAliqOutput
    gpBioDiferenca: TgpBioDiferencaCBSOutput

class TgCBSValoresOutput(TypedDict, total=False):
    gALCZFMCBS: TgALCZFMCBSOutput
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pCBS: str
    vCBS: str

class TgCompraGovOutput(TypedDict, total=False):
    pRedutor: str
    refDFeAnt: TDFErefCollectionOutput
    tpEnteGov: TtpEnteGov
    tpOperGov: TtpOperGov

class TgCredPresOperOutput(TypedDict, total=False):
    cCredPres: TcCredPres
    gCBSCredPres: TgIBSCBSCredPresOutput
    gIBSCredPres: TgIBSCBSCredPresOutput
    vBCCredPres: str

class TgDevTribOutput(TypedDict, total=False):
    pDevTrib: str
    vDevTrib: str

class TgDifOutput(TypedDict, total=False):
    pDif: str
    vDif: str

class TgEstornoCredOutput(TypedDict, total=False):
    vCBSEstCred: str
    vIBSEstCred: str

class TgIBSOutput(TypedDict, total=False):
    gIBSMunTot: TgIBSMunTotOutput
    gIBSUFTot: TgIBSUFTotOutput
    vCredPres: str
    vCredPresCondSus: str
    vIBS: str

class TgIBSCBSOutput(TypedDict, total=False):
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
    pCredPres: str
    vCredPres: str
    vCredPresCondSus: str

class TgIBSCBSMonoOutput(TypedDict, total=False):
    gCBSMonoAdRem: TgCBSMonoAdRemOutput
    gCBSMonoAdValorem: TgCBSMonoAdValoremOutput
    gIBSMonoAdRem: TgIBSMonoAdRemOutput
    gIBSMonoAdValorem: TgIBSMonoAdValoremOutput
    vTotCBSMonoItem: str
    vTotIBSMonoItem: str

class TgIBSMonoAdRemOutput(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoIBSQtdeOutput
    gMonoRet: TgMonoRetIBSOutput
    gMonoReten: TgMonoRetenIBSQtdeOutput
    gpBioDiferenca: TgpBioDiferencaIBSOutput

class TgIBSMonoAdValoremOutput(TypedDict, total=False):
    gMonoPadrao: TgMonoPadraoIBSAliqOutput
    gMonoRet: TgMonoRetIBSOutput
    gMonoReten: TgMonoRetenIBSAliqOutput
    gpBioDiferenca: TgpBioDiferencaIBSOutput

class TgIBSMunTotOutput(TypedDict, total=False):
    vDevTrib: str
    vDif: str
    vIBSMun: str

class TgIBSMunValoresOutput(TypedDict, total=False):
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pIBSMun: str
    vIBSMun: str

class TgIBSUFTotOutput(TypedDict, total=False):
    vDevTrib: str
    vDif: str
    vIBSUF: str

class TgIBSUFValoresOutput(TypedDict, total=False):
    gDevTrib: TgDevTribOutput
    gDif: TgDifOutput
    gRed: TgRedOutput
    pIBSUF: str
    vIBSUF: str

class TgISOutput(TypedDict, total=False):
    adRemIS: str
    cClassTribIS: str
    CSTIS: str
    pIS: str
    qTrib: str
    uTrib: str
    vBCIS: str
    vIS: str

class TgMonoOutput(TypedDict, total=False):
    vCBSMono: str
    vCBSMonoRet: str
    vCBSMonoReten: str
    vIBSMono: str
    vIBSMonoRet: str
    vIBSMonoReten: str

class TgMonoPadraoCBSAliqOutput(TypedDict, total=False):
    pAliqMonoCBS: str
    vBCMono: str
    vCBSMono: str

class TgMonoPadraoCBSQtdeOutput(TypedDict, total=False):
    adRemCBS: str
    qBCMono: str
    vCBSMono: str

class TgMonoPadraoIBSAliqOutput(TypedDict, total=False):
    pAliqMonoMun: str
    pAliqMonoUF: str
    vBCMono: str
    vIBSMono: str
    vIBSMonoMun: str
    vIBSMonoUF: str

class TgMonoPadraoIBSQtdeOutput(TypedDict, total=False):
    adRemIBS: str
    qBCMono: str
    vIBSMono: str

class TgMonoRetCBSOutput(TypedDict, total=False):
    vCBSMonoRet: str

class TgMonoRetenCBSAliqOutput(TypedDict, total=False):
    pAliqMonoReten: str
    vBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenCBSQtdeOutput(TypedDict, total=False):
    adRemCBSReten: str
    qBCMonoReten: str
    vCBSMonoReten: str

class TgMonoRetenIBSAliqOutput(TypedDict, total=False):
    pAliqMonoReten: str
    vBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetenIBSQtdeOutput(TypedDict, total=False):
    adRemIBSReten: str
    qBCMonoReten: str
    vIBSMonoReten: str

class TgMonoRetIBSOutput(TypedDict, total=False):
    vIBSMonoRet: str

class TgPagAntecipadoOutput(TypedDict, total=False):
    refNFe: TrefDFePagAntCollectionOutput

class TgpBioDiferencaCBSOutput(TypedDict, total=False):
    qBCBioComb: str
    vCBSDiferenca: str

class TgpBioDiferencaIBSOutput(TypedDict, total=False):
    qBCBioComb: str
    vIBSDiferenca: str

class TgRedOutput(TypedDict, total=False):
    pAliqEfet: str
    pRedAliq: str

class TgTransfCredOutput(TypedDict, total=False):
    vCBS: str
    vIBS: str

class TgTribCompraGovOutput(TypedDict, total=False):
    pAliqCBS: str
    pAliqIBSMun: str
    pAliqIBSUF: str
    vTribCBS: str
    vTribIBSMun: str
    vTribIBSUF: str

class TgTribRegularOutput(TypedDict, total=False):
    cClassTribReg: str
    CSTReg: TCSTIBSCBS
    pAliqEfetRegCBS: str
    pAliqEfetRegIBSMun: str
    pAliqEfetRegIBSUF: str
    vTribRegCBS: str
    vTribRegIBSMun: str
    vTribRegIBSUF: str

class TguiaTransitoOutput(TypedDict, total=False):
    nGuia: str
    serieGuia: str
    tpGuia: TtpGuia
    UFGuia: str

class TIBSCBSOutput(TypedDict, total=False):
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
    gCBS: TgCBSOutput
    gEstornoCred: TgEstornoCredOutput
    gIBS: TgIBSOutput
    gMono: TgMonoOutput
    vBCIBSCBS: str

class TICMSOutput(TypedDict, total=False):
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
    vBCICMS: str
    vBCICMSST: str
    vICMS: str
    vICMSST: str

class TICMSConsOutput(TypedDict, total=False):
    UFcons: str
    vBCICMSSTCons: str
    vICMSSTCons: str

class TICMSInterOutput(TypedDict, total=False):
    vBCICMSSTDest: str
    vICMSSTDest: str

class TICMSTotOutput(TypedDict, total=False):
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
    vBc: str
    vDespAdu: str
    vII: str
    vIOF: str

class TImpostoOutput(TypedDict, total=False):
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
    infAdFisco: str
    infCpl: str
    obsCont: TobsContCollectionOutput
    obsFisco: TobsFiscoCollectionOutput
    procRef: TprocRefCollectionOutput

class TinfIntermedOutput(TypedDict, total=False):
    CNPJ: str
    idCadIntTran: str

class TinfNFeOutput(TypedDict, total=False):
    ID: str
    Versao: str

class TinfNFeSuplOutput(TypedDict, total=False):
    qrCode: str
    urlChave: str

class TinfPAAOutput(TypedDict, total=False):
    CNPJPAA: str
    Exponent: str
    Modulus: str
    SignatureValue: str

class TinfRespTecOutput(TypedDict, total=False):
    CNPJ: str
    email: str
    fone: str
    hashCSRT: str
    idCSRT: int
    xContato: str

class TIPIOutput(TypedDict, total=False):
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
    vIS: str

class TLacresCollectionItemOutput(TypedDict, total=False):
    nLacre: str

class TMedCollectionItemOutput(TypedDict, total=False):
    cProdANVISA: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str
    vPMC: str
    xMotivoIsencao: str

class TNFeOutput(TypedDict, total=False):
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
    refCTe: str
    RefECF: TRefECFOutput
    RefNF: TRefNFOutput
    refNFe: str
    refNFeSig: str
    RefNFP: TRefNFPOutput

class TNVECollectionItemOutput(TypedDict, total=False):
    NVE: str

class TobsContCollectionItemOutput(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TobsFiscoCollectionItemOutput(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TobsItemOutput(TypedDict, total=False):
    xCampo: str
    xTexto: str

class TorigCombCollectionItemOutput(TypedDict, total=False):
    cUFOrig: int
    indImport: TindImport
    pOrig: str

class TpagCollectionItemOutput(TypedDict, total=False):
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
    CST: TCSTPis
    pPIS: str
    qBCProd: str
    vAliqProd: str
    vBC: str
    vPIS: str

class TPISSTOutput(TypedDict, total=False):
    indSomaPISST: TIndSomaPISST
    pPis: str
    qBCProd: str
    vAliqProd: str
    vBc: str
    vPIS: str

class TProcDFeOutput(TypedDict, total=False):
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
    indProc: TpcnIndicadorProcesso
    nProc: str
    tpAto: TtpAto

class TProdOutput(TypedDict, total=False):
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
    cAgreg: str
    dFab: str
    dVal: str
    nLote: str
    qLote: str

class TReboqueCollectionItemOutput(TypedDict, total=False):
    placa: str
    RNTC: str
    UF: str

class TrefDFePagAntCollectionItemOutput(TypedDict, total=False):
    refDFEChave: str

class TRefECFOutput(TypedDict, total=False):
    modelo: TpcnECFModRef
    nCOO: str
    nECF: str

class TRefNFOutput(TypedDict, total=False):
    AAMM: str
    CNPJ: str
    cUF: int
    modelo: int
    nNF: int
    serie: int

class TRefNFPOutput(TypedDict, total=False):
    AAMM: str
    CNPJCPF: str
    cUF: int
    IE: str
    modelo: str
    nNF: int
    serie: int

class TRetiradaOutput(TypedDict, total=False):
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
    CFOP: str
    cMunFG: int
    pICMSRet: str
    vBCRet: str
    vICMSRet: str
    vServ: str

class TretTribOutput(TypedDict, total=False):
    vBCIRRF: str
    vBCRetPrev: str
    vIRRF: str
    vRetCOFINS: str
    vRetCSLL: str
    vRetPIS: str
    vRetPrev: str

class TSignatureOutput(TypedDict, total=False):
    DigestValue: str
    IdSignature: str
    IdSignatureValue: str
    SignatureValue: str
    URI: str
    X509Certificate: str

class TTotalOutput(TypedDict, total=False):
    IBSCBSTot: TIBSCBSTotOutput
    ICMSTot: TICMSTotOutput
    ISSQNtot: TISSQNtotOutput
    ISTot: TISTotOutput
    retTrib: TretTribOutput
    vNFTot: str

class TTranspOutput(TypedDict, total=False):
    balsa: str
    modFrete: TpcnModalidadeFrete
    Reboque: TReboqueCollectionOutput
    retTransp: TretTranspOutput
    Transporta: TTransportaOutput
    vagao: str
    veicTransp: TveicTranspOutput
    Vol: TVolCollectionOutput

class TTransportaOutput(TypedDict, total=False):
    CNPJCPF: str
    IE: str
    UF: str
    xEnder: str
    xMun: str
    xNome: str

class TveicProdOutput(TypedDict, total=False):
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
    placa: str
    RNTC: str
    UF: str

class TVolCollectionItemOutput(TypedDict, total=False):
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
