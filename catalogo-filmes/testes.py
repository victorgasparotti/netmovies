import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

chave_api=os.getenv("API_KEY")

url = 'https://api.themoviedb.org/3/search/movie'
parametros = {'api_key':chave_api, 'query': 'Gdcsd', 'language': 'pt-BR'}
resposta = requests.get(url, params=parametros)
dados = resposta.json()

url_imagem='https://image.tmdb.org/t/p/w500'

for dado in dados['results']:
    endereco_completo = url_imagem+dado['poster_path']
    print(endereco_completo)
print(dados)