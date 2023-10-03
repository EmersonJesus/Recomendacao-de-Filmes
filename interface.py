from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

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
janela.configure(background=preto)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use('clam')

#Frames
frameCima = Frame(janela, width=450, height=50, bg=preto, relief='flat',) 
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
linha = Label(frameCima, width=450, height=1, anchor=NW, font=('Verdana 1'), bg=vermelho, fg=branco)
linha.place(x=0, y=47)

#Pergunta
pergunta = Label(framePergunta, text='Olá, quero te ajudar a escolher um filme! Qual gênero você quer?', 
                 width=45, height=2, wraplength=320, justify='center', compound=CENTER, 
                 padx=5, relief=FLAT, anchor=NW, font=('Verdana 11'), bg=branco, fg=preto)
pergunta.place(x=0, y=7)
linha = Label(framePergunta, width=450, height=1, anchor=NW, font=('Verdana 1'), bg=vermelho, fg=branco)
linha.place(x=0, y=57)

#Frame meio
#Botões
terror = Image.open('image/terror.png')
terror = terror.resize((28, 28))
terror = ImageTk.PhotoImage(terror)

botao = Button(frameMeio, image=terror, compound=LEFT, width=100, text=' Terror', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=0, sticky=NSEW, pady=2, padx=2)

acao = Image.open('image/acao.png')
acao = acao.resize((28, 28))
acao = ImageTk.PhotoImage(acao)

botao = Button(frameMeio, image=acao, compound=LEFT, width=100, text=' Ação', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=1, sticky=NSEW, pady=2, padx=2)

comedia = Image.open('image/comedia.png')
comedia = comedia.resize((28, 28))
comedia = ImageTk.PhotoImage(comedia)

botao = Button(frameMeio, image=comedia, compound=LEFT, width=100, text=' Comédia', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=2, sticky=NSEW, pady=2, padx=2)

drama = Image.open('image/drama.png')
drama = drama.resize((28, 28))
drama = ImageTk.PhotoImage(drama)

botao = Button(frameMeio, image=drama, compound=LEFT, width=100, text=' Drama', 
             bg=branco, fg=preto, font=('Ivy 10'), overrelief=RIDGE)
botao.grid(row=0, column=3, sticky=NSEW, pady=2, padx=2)

janela.mainloop()