import requests
import random 

def sugere_filme(i, nota_minima=7.0):
    api_key = 'c585c325aabfd4e3d16539e628332769'
    genero = acha_genero(i)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genero}&vote_average.gte={nota_minima}"
    resposta = requests.get(url).json()
    if resposta['results']:
        # Embaralhe aleatoriamente os resultados
        resultados_embaralhados = random.sample(resposta['results'], min(3, len(resposta['results'])-1))
        
        titulos = [resultado['title'] for resultado in resultados_embaralhados]
        datas = [resultado['release_date'] for resultado in resultados_embaralhados]
        notas = [resultado['vote_average'] for resultado in resultados_embaralhados]
        
        caminho = 'https://www.themoviedb.org/t/p/w220_and_h330_face/'
        caminho_capas = [caminho + resultado['poster_path'].strip('/') for resultado in resultados_embaralhados]
        
        return [titulos, caminho_capas, datas, notas]

def acha_genero(i):
    if i == 'drama':
        genero = "18"  
    elif i == 'comedia':
        genero = "35" 
    elif i  == 'acao':
        genero = "28"  
    elif i == 'terror':
        genero = "27" 
    elif i == 'sci-fi':
        genero = '878'
    elif i == 'suspense':
        genero = '9648'
    elif i == 'romance':
        genero = '10749'
    elif i == 'doc':
        genero = '99'
    return genero

