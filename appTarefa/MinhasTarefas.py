import tkinter as tk
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage

# CRIANDO JANELA
janela = tk.Tk()
janela.title('Minhas Tarefas')
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

frame_em_edicao = None

# FUNÇÃO ADICIONAR TAREFA
def adicionar_tarefa():
    global frame_em_edicao

    tarefa = entrada_tarefa.get().strip()
    if tarefa and tarefa != "Escreva sua tarefa aqui":
        if frame_em_edicao is not None:
            atualizar_tarefa(tarefa)
            frame_em_edicao = None
        else:
            adicionar_item_tarefa(tarefa)
            entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Inválida", "Por Favor, Insira uma tarefa")

def adicionar_item_tarefa(tarefa):
    frame_tarefa = tk.Frame(canvas_interior, bg="white", bd=1, relief=tk.SOLID)

    label_tarefa = tk.Label(frame_tarefa, text=tarefa, font=("Garamond", 16), bg="white", width=25, height=2, anchor="w")
    label_tarefa.pack(side=tk.LEFT, fill=tk.X, padx=10, pady=5)

    botao_editar = tk.Button(frame_tarefa, image=icon_editar, command=lambda f=frame_tarefa, l=label_tarefa: preparar_edicao(f, l), bg="white", relief=tk.FLAT)
    botao_editar.pack(side=tk.RIGHT, padx=5)

    botao_apagar = tk.Button(frame_tarefa, image=icon_delete, command=lambda f=frame_tarefa: deletar_tarefa(f), bg="white", relief=tk.FLAT)
    botao_apagar.pack(side=tk.RIGHT, padx=5)

    frame_tarefa.pack(fill=tk.X, padx=5, pady=5)
    
    checkbutton = ttk.Checkbutton(frame_tarefa, command=lambda label=label_tarefa: alterar_sublinhado(label))
    checkbutton.pack(side=tk.RIGHT, padx=5)

    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def preparar_edicao(frame_tarefa, label_tarefa):
    global frame_em_edicao
    frame_em_edicao = frame_tarefa
    entrada_tarefa.delete(0, tk.END)
    entrada_tarefa.insert(0, label_tarefa.cget("text"))

def atualizar_tarefa(nova_tarefa):
    global frame_em_edicao
    for widget in frame_em_edicao.winfo_children():
        if isinstance(widget, tk.Label):
            widget.config(text=nova_tarefa)

def deletar_tarefa(frame_tarefa):
    frame_tarefa.destroy()
    canvas_interior.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def alterar_sublinhado(label):
    fonte_atual = label.cget("font")
    if "overstrike" in fonte_atual:
        nova_fonte = fonte_atual.replace(" overstrike", "")
    else:
        nova_fonte = fonte_atual + " overstrike" 
    label.config(font=nova_fonte)


# CAMINHO DOS ICONES
icon_editar = PhotoImage(file=r"C:\Users\arian\OneDrive\Área de Trabalho\Programacao\projetos\projetosBasicosPython\appTarefa\edit.png").subsample(18, 18)
icon_delete = PhotoImage(file=r"C:\Users\arian\OneDrive\Área de Trabalho\Programacao\projetos\projetosBasicosPython\appTarefa\delete.png").subsample(18, 18)

fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela, text="Tarefas", font=fonte_cabecalho, bg="#F0F0F0", fg="#333").pack(pady=20)

frame = tk.Frame(janela, bg="#F0F0F0")
frame.pack(pady=10)

entrada_tarefa = tk.Entry(frame, font=("Garamond", 14), relief=tk.FLAT, bg="white", fg="gray", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar = tk.Button(frame, command=adicionar_tarefa, text="Adicionar Tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11), relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

# CRIAR UM FRAME PARA A LISTA DE TAREFAS COM SCROLL
frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0, 0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

janela.mainloop()