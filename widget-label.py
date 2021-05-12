import tkinter as tk
from tkinter import ttk
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget label")
ttk.Label(janela, text="Componente Label").grid(column=0, row=0) 
# Na linha 5, é feito o posicionamento do componente “label” na “janela” com o gerenciador de layout “grid”.
janela.mainloop()