# 1 - Instalar as bibliotecas que serão utilizadas
# Iremos utilizar o requests e beautifulsoup4. Se o Python já estiver instalado, basta executar o comando
# pip install requests beautifulsoup4 no terminal. Caso contrário, instale o Python primeiro no próprio site python.org

# 2 - Importar as bibliotecas que serão utilizadas
import requests
from bs4 import BeautifulSoup

# 3 - Criar uma variável com a URL que queremos buscar as informações
url = "https://coinmarketcap.com/"

# 4 - Fazer uma requisição para o site
response = requests.get(url)

# 5 - Fazer uma verificação para conferir se está pegando as informações corretamente
if response.status_code == 200:

    # 6 - Transformar o conteúdo da resposta em um objeto BeautifulSoup para facilitar a extração
    soup = BeautifulSoup(response.text, "html.parser")

    # 7 - Definir os elementos que queremos extrair. No caso, o nome e preço das criptomoedas
    precoCripto = soup.find_all('div', class_='sc-142c02c-0')  # Classe dos preços no site
    nomeCripto = soup.find_all('p', class_='sc-65e7f566-0 byYAWx coin-item-symbol')  # Classe dos nomes no site

    # 8 - Criar um laço para exibir o nome e o preço das criptomoedas por ordem
    for i, (nome, preco) in enumerate(zip(nomeCripto[:10], precoCripto[:10])):
        print(f'{i+1}. Nome: {nome.get_text()} | Preço: {preco.get_text()}')
else:
    print("Erro ao acessar a página")
