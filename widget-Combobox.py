import tkinter as tk
from tkinter import Variable, ttk
from tkinter import font

#criação de janela tkinter
janela = tk.Tk()
janela.title('Combobox')
janela.geometry('500x250')

#componente labels
ttk.Label(janela, text="Combobox Widget", background= 'green', foreground="white", 
    font = ("Times New Romam", 15)).grid(row= 0, column= 1)

#componente label
ttk.Label(janela, text= "Selecione um mês: ", font = ("Times New Roman", 10)).grid(column= 0, row= 5, padx= 10, pady=25)

#componente combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width= 27, textvariable= n)

#adicao de intens no combobox
escolha['values'] = ('Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro')
escolha.grid(column= 1, row= 5)
escolha.current()
janela.mainloop()



        
