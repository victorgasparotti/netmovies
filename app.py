from flask import Flask, render_template, request
import requests
import os 
from dotenv import load_dotenv

load_dotenv()

chave_api=os.getenv('API_KEY')

def buscar_filmes(titulo):
    try:
        url='https://api.themoviedb.org/3/search/movie'
        parametros={'api_key':chave_api,'query':titulo, 'language': 'pt-BR'}
        resposta=requests.get(url, params=parametros, timeout=10)
        dados=resposta.json()
        return dados
    except requests.exceptions.RequestException:
        return {'results':[]}

app = Flask(__name__, static_folder='public', static_url_path='')

@app.route('/', methods=['GET','POST'])
def inicio():
    if request.method == 'POST':
        titulo = request.form['titulo']
        buscar = buscar_filmes(titulo)
        if buscar['results']:
            return render_template('index.html', filmes=buscar['results'])
        else:
            return render_template('index.html', erro='ERRO AO BUSCAR FILME')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)