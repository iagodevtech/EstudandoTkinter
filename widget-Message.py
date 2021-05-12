import tkinter as tk
from tkinter import font
janela = tk.Tk()
mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
#É instanciado um componente “Message” com uma mensagem para o usuário.
msg = tk.Message(janela, text = mensagem_para_usuario)
msg.config(bg='lightgreen', font=('times', '24', 'italic'))
#O componente é configurado, determinando a cor do “background” e detalhes sobre a fonte da mensagem.
msg.pack()
janela.mainloop()
