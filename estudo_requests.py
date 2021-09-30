import requests

# Apenas para entender um pouco mais sobre requisições em Python

cabecalho = {'User-agent': 'Windows 14',
             'Referer': 'Vim da Parvi'
             }

try:
    requisicao = requests.post('https://putsreq.com/8c0JPTRU08WU885hpGgT', headers=cabecalho)
except Exception as e:
    print('Fail requests ', e)
    
print(requisicao.text)