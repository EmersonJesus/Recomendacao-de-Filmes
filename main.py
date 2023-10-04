from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from sistema import *
from datetime import datetime
import requests
from io import BytesIO

#Cores
preto = '#2e2d2b'
branco = '#feffff'
verde = '#4fa882'
azul = '#03091f'
vermelho = '#f50707'


#Criando Janela
janela = Tk()
janela.title('')
janela.geometry('460x560')
janela.configure(background=branco)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

#Frames
frameCima = Frame(janela, width=480, height=50, bg=preto, relief='flat',) 
frameCima.grid(row=0, column=0)

framePergunta = Frame(janela, width=450, height=60, bg=branco, relief='solid',)
framePergunta.grid(row=1, column=0, padx=5, sticky=NSEW)

frameMeio = Frame(janela, width=450, height=90, bg=branco, relief='solid')
frameMeio.grid(row=2, column=0, padx=5, sticky=NSEW)

frameBaixo = Frame(janela, width=300, height=460, bg=branco, relief='raised')
frameBaixo.grid(row=3, column=0, sticky=NSEW)

#Logo
img = Image.open('image/icon.png')
img = img.resize((40, 40))
img = ImageTk.PhotoImage(img)

logo = Label(frameCima, image=img, width=900, compound=LEFT, padx=5, 
             relief=FLAT, anchor=NW, bg=preto, fg=branco)
logo.place(x=5, y=0)
nome = Label(frameCima, text='Recomendações de Filmes', compound=LEFT, padx=5, 
             relief=FLAT, anchor=NW, font=('Verdana 15'), bg=preto, fg=branco)
nome.place(x=60, y=7)
linha = Label(frameCima, width=500, height=1, anchor=NW, font=('Verdana 1'), bg=vermelho, fg=branco)
linha.place(x=0, y=47)

#Pergunta
pergunta = Label(framePergunta, text='Olá, quero te ajudar a escolher um filme! Qual gênero você quer?', 
                 width=45, height=2, wraplength=320, justify='center', compound=CENTER, 
                 padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'), bg=branco, fg=preto)
pergunta.place(x=0, y=7)
linha = Label(framePergunta, width=500, height=1, anchor=NW, font=('Verdana 1'), bg=vermelho, fg=branco)
linha.place(x=0, y=57)

#funcao resultado
def resultado(i):
    global capa1, capa2, capa3
    capa1 = capa2 = capa3 = None
    
    # Filmes Sugeridos
    sugeridos = sugere_filme(i)
    
    titulos = sugeridos[0]
    poster = sugeridos[1]
    data = sugeridos[2]
    nota = sugeridos[3]
    
    # Limpando frame baixo
    for widget in frameBaixo.winfo_children():
        widget.destroy()
        
    # Criar frames e widgets para os filmes
    criar_frame_filme(frameBaixo, titulos[0], data[0], nota[0], poster[0])
    criar_frame_filme(frameBaixo, titulos[1], data[1], nota[1], poster[1])
    criar_frame_filme(frameBaixo, titulos[2], data[2], nota[2], poster[2])


def criar_frame_filme(frame, titulo, data, nota, poster_url):
    global capa1, capa2, capa3

    filme = Frame(frame, width=150, height=400, bg=branco)
    filme.grid(row=0, column=frame.grid_size()[0], sticky=NSEW, pady=5)

    # Nome
    filme_nome = Label(filme, text=titulo, height=2, padx=10, pady=5,
                       wraplength=100, justify='left', relief=SOLID, anchor=NW,
                       font=('Ivy 9'), bg=branco, fg=preto, bd=1, highlightbackground='white')
    filme_nome.place(x=7, y=260)

    # Data
    data_string = f'{data}'
    data_obj = datetime.strptime(data_string, '%Y-%m-%d')
    data_formatada = data_obj.strftime('%Y')
    l_data = Label(filme, text=f'Lançamento: {data_formatada}', anchor=NW, font=('Ivy 8'), bg=branco, fg=preto)
    l_data.place(x=5, y=310)

    # Nota
    l_nota = Label(filme, text=f'Média: {nota}/10', anchor=NW, font=('Ivy 8'), bg=branco, fg=preto)
    l_nota.place(x=5, y=330)

    # Obtendo a imagem
    pedido = requests.get(poster_url)
    poster_url = pedido.url

    # Carregando a imagem
    poster = Image.open(BytesIO(pedido.content))
    capa = poster.resize((150, 250))
    capa = ImageTk.PhotoImage(capa)

    # Poster
    l_capa = Label(filme, image=capa, padx=5, bg=branco, fg=preto)
    l_capa.place(x=5, y=0)

    # Atribuir a imagem à variável global correspondente
    if capa1 is None:
        capa1 = capa
    elif capa2 is None:
        capa2 = capa
    elif capa3 is None:
        capa3 = capa
 
#Frame meio
#Botões
terror = Image.open('image/terror.png')
terror = terror.resize((28, 28))
terror = ImageTk.PhotoImage(terror)

botao = Button(frameMeio, command=lambda:resultado('TERROR'), image=terror, compound=LEFT, width=120, text=' Terror', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

acao = Image.open('image/acao.png')
acao = acao.resize((28, 28))
acao = ImageTk.PhotoImage(acao)

botao = Button(frameMeio, command=lambda:resultado('ACAO'), image=acao, compound=LEFT, width=120, text=' Ação', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)

comedia = Image.open('image/comedia.png')
comedia = comedia.resize((28, 28))
comedia = ImageTk.PhotoImage(comedia)

botao = Button(frameMeio, command=lambda:resultado('COMEDIA'), image=comedia, compound=LEFT, width=120, text=' Comédia', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)

drama = Image.open('image/drama.png')
drama = drama.resize((28, 28))
drama = ImageTk.PhotoImage(drama)

botao = Button(frameMeio, command=lambda:resultado('DRAMA'), image=drama, compound=LEFT, width=120, text=' Drama', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=1, column=0, sticky=NSEW, pady=2, padx=2)

janela.mainloop()