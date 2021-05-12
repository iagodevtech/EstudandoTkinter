import tkinter as tk
from tkinter import messagebox as mb
def resposta():
    mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
def verificacao():
    if mb.askyesno('Verificar', 'Realmente quer sair?'):
        mb.showwarning('Yes', 'Ainda não foi implementado')
    else:
        mb.showinfo('No', 'A opcao sair foi cancelada')
    # Nas linhas 4, 6, 7 e 9, são instanciados componentes “messageDialog”.

tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
tk.mainloop()


# Esse exemplo é bastante interessante, pois, apesar de pouca implementação, 
# é possível que o usuário tenha bastante interação com o sistema.