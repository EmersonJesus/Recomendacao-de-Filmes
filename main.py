import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sugere_filme(api_key):
    sentimento = input('Como você está se sentindo hoje? ')
    emocao = analyzer.polarity_scores(sentimento)['compound']
    genero = acha_genero(emocao)

    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genero}&vote_count.gte=4"
    resposta = requests.get(url).json()
    
    if resposta['results']:
        titulo = [resultado['title'] for resultado in resposta['results'][:5]]
        print("Recomendo os seguintes filmes para você:")
        for titulo in titulo:
           print(f"- {titulo}")
    else:
        print("Não encontrei nenhuma sugestão de filme para você.")

def acha_genero(emocao):
    if emocao <= -0.5:
        genero = "18"  # Drama
    elif emocao < 0:
        genero = "35"  # Comédia
    elif emocao < 0.5:
        genero = "10749"  # Romance
    else:
        genero = "27"  # Horror
    return genero

def chatbot(api_key):
    print("Olá! Sou um chatbot de sugestões de filmes. Como posso te ajudar hoje?")
    while True:
        try:
            resposta = input().lower()
            if 'filme' in resposta:
                sugere_filme(api_key)
            elif 'tchau' in resposta or 'adeus' in resposta:
                print("Adeus! Vejo você na próxima vez.")
                break
            else:
                print("Desculpe, não entendi o que você quis dizer.")
        except KeyboardInterrupt:
            break

api_key = 'c585c325aabfd4e3d16539e628332769'
analyzer = SentimentIntensityAnalyzer()
chatbot(api_key)