import requests
import random 

def sugere_filme(i):
    api_key = 'c585c325aabfd4e3d16539e628332769'
    genero = acha_genero(i)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genero}&vote_count.gte=4"
    resposta = requests.get(url).json()
    if resposta['results']:
        # Embaralhe aleatoriamente os resultados
        resultados_embaralhados = random.sample(resposta['results'], min(3, len(resposta['results'])))
        
        titulos = [resultado['title'] for resultado in resultados_embaralhados]
        datas = [resultado['release_date'] for resultado in resultados_embaralhados]
        notas = [resultado['vote_average'] for resultado in resultados_embaralhados]
        
        caminho = 'https://www.themoviedb.org/t/p/w220_and_h330_face/'
        caminho_capas = [caminho + resultado['poster_path'].strip('/') for resultado in resultados_embaralhados]
        
        return [titulos, caminho_capas, datas, notas]

def acha_genero(i):
    if i == 'DRAMA':
        genero = "18"  
    elif i == 'COMEDIA':
        genero = "35" 
    elif i  == 'ACAO':
        genero = "28"  
    elif i == 'TERROR':
        genero = "27" 
    return genero

