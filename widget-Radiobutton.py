import tkinter as tk
janela = tk.Tk()
v = tk.IntVar()
tk.Label(janela, text="""Escolha uma linguagem de programação:""", justify=tk.LEFT,padx=20,).pack()
# É instanciado um componente “label” com a parametrização das propriedades “text”, “justify” e “padx” que correspondem, 
# respectivamente, ao texto, como vai ser justificado e qual a largura em pixels do componente.

tk.Radiobutton(janela, text="Python", padx=25, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text="C++", padx=25, variable=v, value=2).pack(anchor=tk.W)
# São instanciados os componentes “radiobuttons”. Cabe destacar a propriedade “variable”, que recebe o valor “v”, 
# que indica que o componente será colocado na vertical.
janela.mainloop()

