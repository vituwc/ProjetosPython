import tkinter
from tkinter import *
from tkinter import ttk
import random
from PIL import Image, ImageTk
from timeit import default_timer
import difflib

# cores ----------------------
co0 = "#1E1E1E"  # Fundo escuro suave
co1 = "#F1F1F1"  # Texto claro
co2 = "#66BB6A"  # Verde suave para resultados
co3 = "#546E7A"  # Cinza escuro para textos secundários
co4 = "#42A5F5"  # Azul suave para destaque

# CONFIGURANDO JANELA
janela = Tk()
janela.title('Velocidade De Digitação')
janela.geometry('390x310')
janela.configure(bg=co0)

# DIVIDINDO A JANELA
frame_logo = Frame(janela, width=390, height=60, bg=co0, relief=RAISED)
frame_logo.grid(row=0, column=0)

frame_tela = Frame(janela, width=390, height=60, bg=co0, relief=RAISED)
frame_tela.grid(row=1, column=0)

frame_corpo = Frame(janela, width=390, height=190, bg=co0, relief=FLAT)
frame_corpo.grid(row=2, column=0)

# CONFIGURANDO O FRAME LOGO
imagem = Image.open('../Programacao/projetosBasicosPython/velocidadeDeDigitacao/typing.png')
imagem = imagem.resize((50, 50), Image.Resampling.LANCZOS)
imagem = ImageTk.PhotoImage(imagem)

l_logo = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, bg=co0, fg=co3)
l_logo.place(x=10, y=5)

l_nome = Label(frame_logo, text='Teste de Velocidade de Digitação', font=('Arial 15 bold'), anchor='nw', justify='left', bg=co0, fg=co1)
l_nome.place(x=65, y=20)

# CONFIGURANDO FRAME TELA
l_tela = Label(frame_tela, text='Frase a ser Digitada', width=32, height=3, font=('Ivy 12 bold'), justify='left', wraplength=300, bg=co0, fg=co2)
l_tela.grid(row=0, column=0, padx=50, pady=6)

frases = [
    "Cada passo dado é uma chance de recomeçar de novo.",
    "A verdadeira felicidade não depende do que você tem, mas do que você sente.",
    "Não importa quantos obstáculos você enfrente, o importante é continuar caminhando.",
    "O segredo da vida está em encontrar beleza nas pequenas coisas.",
    "Nada é impossível quando você acredita em si mesmo.",
    "A mudança começa de dentro para fora.",
    "A gratidão transforma o que temos em suficiente.",
    "A paciência é a chave para alcançar grandes conquistas.",
    "A felicidade não é algo pronto, ela vem das suas próprias ações.",
    "Quem não arrisca, não petisca.",
    "A coragem é a resistência ao medo, não a ausência dele.",
    "A vida é curta demais para esperar o momento perfeito.",
    "Sorrir é a maneira mais simples de ser feliz.",
    "A amizade verdadeira não tem fim, apenas mudanças.",
    "A jornada é tão importante quanto o destino."
]

# FUNÇÃO INICIAR
def iniciar():
    global frase
    global frase_digitada
    global b_verify
    global l_digita
    global e_digita
    global comecar

    # REMOVENDO BOTAO
    b_iniciar.destroy()

    frase = random.choice(frases)

    # LABEL PARA A FRASE A SER DIGITADA
    l_tela.config(text=frase) 
    # DIGITE A FRASE
    l_digita = Button(frame_corpo, text='Digite a frase acima', font=('Arial 10'), bg=co3, fg=co4, relief=FLAT, width=30, height=2, borderwidth=0, bd=0)
    l_digita.grid(row=0, column=0, padx=5, pady=10)

    # FRASE DIGITADA
    frase_digitada = StringVar()
    e_digita = Entry(frame_corpo, textvariable=frase_digitada, width=42, relief=SOLID, font=('Arial 12'), bg=co3, fg=co4, bd=0, highlightthickness=2, highlightcolor=co4)
    e_digita.grid(row=1, column=0, padx=5, pady=5)

    # BOTÃO VERIFICAR
    b_verify = Button(frame_corpo, command=verificar, text='Começar', font=('Arial 10 bold'), bg=co3, fg=co4, relief=FLAT, width=15, height=2, bd=0, highlightthickness=2, highlightcolor=co4)
    b_verify.grid(row=2, column=0, padx=5, pady=15)

# FUNÇÃO VERIFICAR
def verificar():
    global frase
    global frase_digitada
    global b_verify
    global l_digita
    global e_digita
    global comecar

    # REMOVENDO OS ELEMENTOS ANTERIORES
    l_digita.destroy()
    e_digita.destroy()
    b_verify.destroy()

    # CALCULANDO O TEMPO
    string = f"{frase_digitada.get()}"
    termino = default_timer()
    tempo = round(termino - comecar, 2)

    # CÁLCULO DE VELOCIDADE E PRECISÃO
    speed = round(len(frase.split()) * 60 / tempo, 2)

    if string == frase:
        precisao = 100
    else:
        precisao = difflib.SequenceMatcher(None, frase, string).ratio() * 100
        precisao = round(precisao, 2)

    f_tempo = "Tempo = " + str(tempo) + " segundos"
    f_precisao = f"Precisão = {precisao}%"
    f_velocidade = "Velocidade = " + str(speed) + " ppm"

    # RESULTADOS
    l_tempo.config(text=f_tempo)
    l_precisao.config(text=f_precisao)
    l_velocidade.config(text=f_velocidade)

# INICIANDO O TESTE
b_iniciar = Button(frame_corpo, command=iniciar, text='Começar o Teste de Digitação', font=('Arial 12 bold'), bg=co2, fg=co1, relief=FLAT, width=25, height=2, bd=0, highlightthickness=2, highlightcolor=co2)
b_iniciar.grid(row=2, column=0, padx=50, pady=40)

# RESULTADOS
l_tempo = Label(frame_corpo, text='Tempo: 0', width=32, height=3, font=('Arial 12 bold'), anchor='nw', justify='left', bg=co0, fg=co1)
l_tempo.grid(row=3, column=0, padx=2, pady=5)

l_precisao = Label(frame_corpo, text='Precisão: 0%', width=32, height=3, font=('Arial 12 bold'), anchor='nw', justify='left', bg=co0, fg=co1)
l_precisao.grid(row=4, column=0, padx=2, pady=5)

l_velocidade = Label(frame_corpo, text='Velocidade: 0 ppm', width=32, height=3, font=('Arial 12 bold'), anchor='nw', justify='left', bg=co0, fg=co1)
l_velocidade.grid(row=5, column=0, padx=2, pady=5)

# TEMPO INICIAL
comecar = default_timer()

janela.mainloop()
