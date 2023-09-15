#Código feito por Mateus Cristiano Razini Biancato
import tkinter as tk
from tkinter import messagebox
from tkinter import *

def enviar_mensagem():
    nome = entry_nome.get()
    mensagem = entry_mensagem.get()

    if nome and mensagem:
        messagebox.showinfo("Mensagem Enviada", f"Nome: {nome}\nMensagem: {mensagem}")
    else:
        messagebox.showerror("Erro", "Por favor, preencha ambos os campos!")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Enviar Mensagem")
janela.geometry("280x180")

# Rótulos e campos de entrada
label_nome = tk.Label(janela, text="Nome:")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

label_mensagem = tk.Label(janela, text="Mensagem:")
label_mensagem.pack()
entry_mensagem = tk.Entry(janela)
entry_mensagem.pack()

# Botão de envio
botao_enviar = tk.Button(janela, text="Enviar", command=enviar_mensagem)
botao_enviar.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()