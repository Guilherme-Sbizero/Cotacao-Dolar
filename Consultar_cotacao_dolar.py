# Use o comando pip install requests para fazer o download do requests

import requests

#Link publico com valor atual da cotação do Dólar
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

# Busca os dados
response = requests.get(url)

# Se a busca funcionou, mostrar o valor
if response.status_code == 200:
    dolar_value = response.json() ['USD'] ['low']
    print(f'O valor do Dólar é R${dolar_value}')
else:
    print('Erro ao buscar valor do Dólar!')