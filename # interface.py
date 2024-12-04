# interface.py

import tkinter as tk
from tkinter import messagebox
import geradsenhas

def gerar():
    # Obtém os valores dos campos da interface
    comprimento = int(entry_comprimento.get())
    incluir_maiusculas = var_maiusculas.get()
    incluir_numeros = var_numeros.get()
    incluir_simbolos = var_simbolos.get()

    # Gera a senha usando a função importada
    senha = geradsenhas.gerar_senha(comprimento=comprimento, 
                                    incluir_maiusculas=incluir_maiusculas, 
                                    incluir_numeros=incluir_numeros, 
                                    incluir_simbolos=incluir_simbolos)
    
    # Exibe a senha gerada
    label_senha.config(text=f"Senha gerada: {senha}")

def validar_comprimento(event):
    # Verifica se o comprimento está dentro do limite
    try:
        comprimento = int(entry_comprimento.get())
        if comprimento > 15:
            messagebox.showwarning("Aviso", "O comprimento máximo da senha é 15 caracteres!")
            entry_comprimento.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido!")

# Criação da janela principal
root = tk.Tk()
root.title("Gerador de Senhas")

# Definição dos elementos da interface
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Comprimento da senha
label_comprimento = tk.Label(frame, text="Comprimento da senha (máximo 15):")
label_comprimento.grid(row=0, column=0, padx=5, pady=5)

entry_comprimento = tk.Entry(frame)
entry_comprimento.grid(row=0, column=1, padx=5, pady=5)
entry_comprimento.bind("<FocusOut>", validar_comprimento)  # Verifica quando o campo perde o foco

# Opções de configuração da senha
var_maiusculas = tk.BooleanVar()
check_maiusculas = tk.Checkbutton(frame, text="Incluir Maiúsculas", variable=var_maiusculas)
check_maiusculas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

var_numeros = tk.BooleanVar()
check_numeros = tk.Checkbutton(frame, text="Incluir Números", variable=var_numeros)
check_numeros.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

var_simbolos = tk.BooleanVar()
check_simbolos = tk.Checkbutton(frame, text="Incluir Símbolos", variable=var_simbolos)
check_simbolos.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Botão para gerar a senha
btn_gerar = tk.Button(frame, text="Gerar Senha", command=gerar)
btn_gerar.grid(row=4, column=0, columnspan=2, padx=5, pady=10)

# Exibição da senha gerada
label_senha = tk.Label(root, text="Senha gerada: ", font=("Arial", 14))
label_senha.pack(padx=10, pady=10)

# Iniciar a interface
root.mainloop()
