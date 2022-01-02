
import requests
from bs4 import BeautifulSoup

cod = [
        "UPSS34",
        "LMTB34",
        "FDXB34",
        "CATP34",
        "BOEI34",
        "NFLX34",
        "NIKE34",
        "MCDC34",
        "HOME34",
        "FDMO34",
        "CMCS34",
        "AMZO34",
        "SBUB34",
        "WALM34",
        "PEPB34",
        "COLG34",
        "COCA34",
        "VISA34",
        "MSBR34",
        "MSCD34",
        "JPMC34",
        "HONB34",
        "GEOO34",
        "GSGI34",
        "CTGP34",
        "BOAC34",
        "MMMC34",
        "FCXO34",
        "SLBG34",
        "HALI34",
        "COPH34",
        "CHVX34",
        "PFIZ34",
        "MRCK34",
        "GBIO33",
        "XRXB34",
        "QCOM34",
        "ORCL34",
        "MSFT34",
        "IBMB34",
        "ITLC34",
        "HPQB34",
        "CSCO34",
        "AAPL34",
        "VERZ34",
        "ATTB34",
]


for i in range(0, len(cod)):
    url = f'https://statusinvest.com.br/bdrs/{cod[i]}'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    #para saber o Div. Yield
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    soup2 = str(soup)
    Div_Yield = soup2.find('D.Y')  # Div. Yield</span></td><td class="data"><span class="txt">
    Div2 = Div_Yield + 215
    Div3 = Div2 + 7
    print(soup2[Div2:Div3])


"""url = f'https://statusinvest.com.br/bdrs/fdxb34'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
# para saber o Div. Yield
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
soup2 = str(soup)
Div_Yield = soup2.find('D.Y')  # Div. Yield</span></td><td class="data"><span class="txt">
Div2 = Div_Yield + 217
Div3 = Div2 + 4
print(soup2[Div2:Div3])"""


'''
for i in range(0, len(cod)):
    url = f'https://www.fundamentus.com.br/detalhes.php?papel={cod[i]}'
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    # para saber o P/VP
    site = requests.get(url, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    soup2 = str(soup)
    P_VP = soup2.find('P/VP')  # Div. Yield</span></td><td class="data"><span class="txt">
    P_VP2 = P_VP + 55
    P_VP3 = P_VP2 + 4
    print(soup2[P_VP2:P_VP3])
'''
'''
url = 'https://statusinvest.com.br/bdrs/fdxb34'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
# para saber o P/L NÂO FUNCIONOU
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
soup2 = str(soup)
P_L = soup2.find('Div Br/ Patrim')  # Div. Yield</span></td><td class="data"><span class="txt">
P_L2 = P_L + 55
P_L3 = P_L + 5
print(soup2[P_L2:P_L3])
'''

'''
for i in range(1,int(ultima_pagina)):
    url_pag = f'https://www.pichau.com.br/hardware/placa-de-video?page={i}'
    site = requests.get(url_pag, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    placas = soup.find_all('div', class_='product details product-item-details')

    with open('precos_placas.csv', 'a', newline='', encoding='UTF-8') as f:
        for placa in placas:
            marca = placa.find('a', class_='product-item-link').get_text().strip()

            try:
                preco = placa.find('span', class_='price').get_text().stip()
                num_preco = preco[2:]
                num_preco = num_preco[:-3]
            except:
                num_preco = '0'

            try:
                preco_boleto = placa.find('span', class_='price-boleto').get_text.strip()
                index = preco_boleto.find(',')
                num_preco_boleto = preco_boleto[10:index]
            except:
                num_preco_boleto = '0'

            linha = marca + ';' + num_preco + ';' + num_preco_boleto + '\n'
            print(linha)
            f.write(linha)
    print(url_pag)
'''