import tkinter as tk  # É feita a importação da biblioteca Tkinter.

janela = tk.Tk()  # É criada uma instância da classe Tk no objeto “janela”.

#janela.title("Aplicação GUI") # O método “title” é usado para definir um título que aparece no topo da janela, no caso, “Aplicação GUI”.
janela.title("Aplicação GUI NÃO Dimensionável")
janela.resizable(False, False)
janela.mainloop() # A aplicação inicia o loop de evento principal da janela.

# Bem, a janela da aplicação anterior é redimensionável, ou seja, 
# o usuário pode alterar as dimensões da janela, se ele clicar com o cursor do mouse na janela e arrastá-la.