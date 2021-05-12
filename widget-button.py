import tkinter as tk
contador = 0
def contador_label(lblRotulo):
 def funcao_contar():
        global contador
        contador = contador +1
        lblRotulo.config(text=str(contador))
        lblRotulo.after(1000, funcao_contar)
 funcao_contar()
janela = tk.Tk()
janela.title("Contagem de Segundos")
lblRotulo = tk.Label(janela, fg="green")
lblRotulo.pack()
contador_label(lblRotulo)
#Chamada para a função “contador_label”, 
#que é a função que faz a contagem dos segundos e a atualização dos dados do componente “label”.

btnAcao = tk.Button(janela, text='Clique aqui para interromper a contagem', width=50, command=janela.destroy)
#Criação de uma instância do componente “botão” com uma mensagem, 
# largura do componente e o estabelecimento de um comportamento, 
# no caso, fechar a janela, quando o usuário pressionar o botão.

btnAcao.pack()
janela.mainloop()

