import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

chave_api=os.getenv("API_KEY")



url = 'https://www.omdbapi.com/'
parametros = {'apikey':chave_api, 's': 'Star Wars'}
resposta = requests.get(url, params=parametros)
dados = resposta.json()

for dado in dados['Search']:
    print(dado['Title'], dado['Year'], dado['Poster'])