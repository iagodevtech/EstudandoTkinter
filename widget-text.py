import tkinter as tk
janela = tk.Tk()
T = tk.Text(janela, height=2, width=30)
#É feita uma instância do componente “Text”.
T.pack()
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
#É inserido um texto na instância do componente “text”, que vai ser exibido na tela. 
# Observe que o texto é separado em duas linhas com o uso do “\n”.
tk.mainloop()
