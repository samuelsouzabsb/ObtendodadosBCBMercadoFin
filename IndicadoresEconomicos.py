"""

    Objetivo: Indicadores econômicos para análises financeiras
    Horário recomendado: 01hs ('Madrugada')
    Frequência: Diário
    O que Faz??: Realiza conexão em algumas API's (Banco Central e Yahoo) e realiza uma raspagem de dados buscando um tabela dentro de um site.

    Bibliotecas: pandas, yfinance, datetime

"""
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
caminhosaida = 'Saída do sue arquivo'
DataFim = datetime.today()
DataInicio = datetime.today()-timedelta(3660)
DataIBC = DataInicio.strftime('%m%d%Y')
DataFBC = DataFim.strftime('%m%d%Y')
DataFim = DataFim.strftime('%Y-%m-%d')
DataInicio = DataInicio.strftime('%Y-%m-%d')

basebc = {'IE - Cotação Dólar':'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@dataInicial=\''+DataIBC+'\'&@dataFinalCotacao=\''+DataFBC+'\'&$top=10000&$format=text/csv&$select=cotacaoCompra,cotacaoVenda,dataHoraCotacao',
'IE - IVVV - DF - Mercados':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.1573/dados?formato=csv','IE - IPCA - CO':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.13951/dados?formato=csv','IE - INPC - CO':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.13952/dados?formato=csv',
'IE - SELIC - DIÁRIA':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=csv','IE - CDI - DIÁRIO':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=csv','IE - SELIC - MENSAL':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=csv',
'IE - CDI - MENSAL':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.4391/dados?formato=csv','IE - IVVV - DF - Alimentos e Bebidas':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.1508/dados?formato=csv','IE - IVVV - DF':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.1482/dados?formato=csv',
'IE - INPC - DF':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.13250/dados?formato=csv','IE - IPCA - DF':'http://api.bcb.gov.br/dados/serie/bcdata.sgs.13248/dados?formato=csv'
    }
BuscaYahoo = {
    'KO':'AC - CocaColaNA','ABEV':'AC - AbevNA','COCA34.SA':'AC - CocaColaSA','ABEV3.SA':'AC - AbevSA','PEP':'AC - PepsiCoNA','PEPB34.SA':'AC - PepsiCoSA','^BVSP':'IN - IBOVESPA','NQ=F':'IN - NASDAQ','^N225':'IN - NIKKEI','^HSI':'IN - HANG SENG',
    '^FTSE':'IN - FTSE 100','^NYA':'IN - NYSE','^GSPC':'IN - S&P 500','CL=F':'COM - Petróleo Bruto','RB=F':'COM - Gasolina','ZC=F':'COM - Milho','CC=F':'COM - Cacau','KC=F':'COM - Café','SB=F':'COM - Açúcar','ZS=F':'COM - Soja','ZR=F':'COM - Arroz',
    'KE=F':'COM - Trigo','BZ=F':'COM - Petróleo Bruto Brent Financ'
    
    }

for salvarnome, urlbc in basebc.items():
    if salvarnome == 'IE - Cotação Dólar':
        Manipular = pd.read_csv(urlbc)
    else:
        Manipular = pd.read_csv(urlbc,sep=';')
    Manipular.to_excel(caminhosaida+salvarnome+".xlsx")

for idyahoo,nomesalvar in BuscaYahoo.items():
    Manipular = yf.download(idyahoo, start=DataInicio, end=DataFim)
    Manipular.to_excel(caminhosaida+nomesalvar+".xlsx")
    
Manipular = pd.read_html('http://www.yahii.com.br/igpm.html',match='JAN')
Manipular = Manipular[0]
Manipular = Manipular.drop(Manipular.index[0])
Manipular = Manipular.drop(Manipular.index[37])
Manipular = Manipular.drop(Manipular.index[36])
Manipular = Manipular.drop(Manipular.index[35])
Manipular = Manipular.drop(Manipular.index[34])
Manipular = Manipular.drop(columns=[13])
Manipular = pd.melt(Manipular,id_vars=[0],var_name='Mês',value_name='IGPM')
Manipular.columns=['Ano','Mês','IGPM']
Manipular = Manipular[Manipular['IGPM'].notna()]
Manipular.to_excel(caminhosaida+"IE - IGPM.xlsx")
