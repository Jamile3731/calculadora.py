import tkinter as tk

# Função para atualizar a expressão
def clicar(botao):
    atual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, atual + botao)

# Função para limpar a tela
def limpar():
    entrada.delete(0, tk.END)

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# Botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 15),
                  command=calcular).grid(row=linha, column=coluna, padx=5, pady=5)
    else:
        tk.Button(janela, text=texto, width=5, height=2, font=("Arial", 15),
                  command=lambda t=texto: clicar(t)).grid(row=linha, column=coluna, padx=5, pady=5)

# Botão "C" (limpar)
tk.Button(janela, text="C", width=23, height=2, font=("Arial", 15),
          command=limpar).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Executar a janela
janela.mainloop()
