import tkinter as tk
def mostrar_nomes(): 
    # É implementada a função “mostrar_nomes”, 
    # que vai exibir na linha de comando os nomes que estão escritos nas 
    # instâncias “e1” e “e2” do componente “entry”.

    print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela, text="Nome").grid(row=0)
tk.Label(janela, text="Sobrenome").grid(row=1)

e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
#São feitas as instâncias “e1” e “e2” do componente entry.

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
#“e1” e “e2” são posicionados na janela.

tk.Button(janela, text='Sair', command=janela.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3, column=1, sticky=tk.W, pady=4)
#São instanciados objetos do componente “botão”. Em especial, na linha 22, 
# a função “mostrar_nomes” é associada ao comportamento do botão.

tk.mainloop()




