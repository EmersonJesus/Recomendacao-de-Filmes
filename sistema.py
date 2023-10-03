import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sugere_filme(i):
    genero = acha_genero(i)
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genero}&vote_count.gte=4"
    resposta = requests.get(url).json()
    
    if resposta['results']:
        titulo = [resultado['title'] for resultado in resposta['results'][:5]]
        print("Recomendo os seguintes filmes para você:")
        for titulo in titulo:
           print(f"- {titulo}")
    else:
        print("Não encontrei nenhuma sugestão de filme para você.")

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

api_key = 'c585c325aabfd4e3d16539e628332769'
analyzer = SentimentIntensityAnalyzer()