# 🎬 NetMovies

O **NetMovies** é um catálogo de filmes desenvolvido em Python. Com ele, é possível pesquisar títulos e visualizar informações como pôster, ano de lançamento, avaliação e sinopse. Os dados são obtidos pela API do [The Movie Database (TMDB)](https://www.themoviedb.org/).

## ✨ Funcionalidades

- Pesquisa de filmes pelo título.
- Resultados com pôster, ano de lançamento, nota e sinopse.
- Conteúdo dos filmes em português (quando disponível na API).
- Interface responsiva em tema escuro.
- Tratamento básico para quando a busca não retorna resultados ou ocorre um erro de conexão.

## 🛠️ Tecnologias utilizadas

- **Python** — lógica da aplicação e comunicação com a API.
- **Flask** — servidor web e renderização da página.
- **Requests** — envio de requisições HTTP para a API do TMDB.
- **python-dotenv** — leitura da chave da API a partir de uma variável de ambiente.
- **TMDB API** — fonte dos dados e imagens dos filmes.
- HTML e CSS — estrutura e apresentação da interface.

## ⚙️ Como o projeto funciona

A parte principal da aplicação fica em `app.py`:

1. O Flask disponibiliza a rota principal (`/`), que aceita acesso por navegador e envio do formulário de pesquisa.
2. Quando o usuário envia um título, a função `buscar_filmes(titulo)` monta uma requisição para o endpoint de pesquisa de filmes do TMDB.
3. A biblioteca Requests envia a requisição com a chave da API, o título pesquisado e o idioma `pt-BR`.
4. A resposta JSON é processada e os resultados são enviados ao template `templates/index.html`.
5. O template apresenta os dados de cada filme, enquanto o CSS em `public/style.css` controla a aparência da página.

A chave da API é carregada com `python-dotenv` a partir de um arquivo local `.env`. Assim, ela não precisa ficar escrita diretamente no código-fonte.

## 🚀 Como executar localmente

### 1. Pré-requisitos

- Python 3 instalado.
- Uma chave de API do TMDB. Você pode consultar as opções de acesso na [documentação oficial do TMDB](https://developer.themoviedb.org/docs).

### 2. Baixe o projeto

Clone o repositório e entre na pasta:

```bash
git clone https://github.com/victorgasparotti/netmovies.git
cd netmovies
```

### 3. Crie e ative um ambiente virtual (recomendado)

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure a chave da API

Crie um arquivo chamado `.env` na pasta principal do projeto e adicione sua chave:

```env
API_KEY=sua_chave_do_tmdb
```

Substitua `sua_chave_do_tmdb` pela sua chave real. Não compartilhe esse arquivo nem envie sua chave para o GitHub. O arquivo `.env` já está listado no `.gitignore`.

### 6. Inicie a aplicação

```bash
python app.py
```

Abra no navegador o endereço local exibido pelo Flask, normalmente:

```
http://127.0.0.1:5000
```

> O modo de depuração está habilitado no código para desenvolvimento local. Antes de publicar a aplicação em produção, desative o `debug`.

## 🌐 Acesse o projeto

Você pode testar a versão publicada do NetMovies aqui:

**[Abrir NetMovies](https://netmovies-henna.vercel.app)**

## 💡 Ideias para futuras melhorias

Algumas funcionalidades que podem ser adicionadas em próximas versões:

- **Filmes favoritos:** permitir que o usuário salve títulos para consultar depois.
- **Filtros e ordenação:** filtrar por gênero, ano de lançamento e nota, além de ordenar os resultados.
- **Página de detalhes:** exibir informações mais completas sobre cada filme, elenco, duração e gêneros.
- **Paginação:** permitir navegar por mais resultados de pesquisa.
- **Busca por categorias:** explorar filmes populares, mais bem avaliados e lançamentos.
- **Melhorias de acessibilidade:** aprimorar a navegação por teclado, os rótulos e o contraste.
- **Testes automatizados:** criar testes para a busca, o tratamento de erros e as rotas da aplicação.
- **Configuração de produção:** revisar variáveis de ambiente e desativar o modo de depuração em ambiente publicado.

Essas ideias são possibilidades para evoluir o projeto; elas ainda não fazem parte necessariamente da versão atual.

## 🧭 Como usar o site

1. Abra o NetMovies no navegador.
2. Digite o nome do filme na barra de pesquisa.
3. Clique em **Buscar filmes**.
4. Confira os resultados, incluindo pôster, ano, avaliação e sinopse.
5. Se nenhum resultado aparecer, tente outro título ou confira a grafia. A disponibilidade de sinopses e imagens depende dos dados fornecidos pelo TMDB.

## 📁 Estrutura do projeto

```text
netmovies/
├── app.py                  # Aplicação Flask e busca na API
├── requirements.txt        # Dependências Python
├── .env                    # Chave da API (criado localmente)
├── .gitignore              # Arquivos que não devem ser versionados
├── templates/
│   └── index.html          # Página renderizada pelo Flask/Jinja
├── public/
│   └── style.css           # Estilos da interface
└── catalogo-filmes/
    └── testes.py           # Arquivo de testes/experimentos do projeto
```

## 📚 Aprendizados

Neste projeto, pratiquei conceitos importantes de desenvolvimento com Python, como:

- criação de uma aplicação web com Flask;
- definição de rotas e tratamento de formulários;
- criação de funções para separar responsabilidades;
- consumo de uma API REST usando requisições HTTP;
- leitura e utilização de respostas no formato JSON;
- uso de variáveis de ambiente para manter credenciais fora do código;
- integração entre a lógica Python e templates HTML.

## 🔗 Créditos

Os dados de filmes e as imagens são fornecidos pelo [The Movie Database (TMDB)](https://www.themoviedb.org/). Este projeto utiliza a API do TMDB e não é endossado nem certificado por ele.

---

Desenvolvido como projeto de estudo para praticar Python, integração com APIs e desenvolvimento web.
