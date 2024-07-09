from tkinter import *

#Definindo a janela
root = Tk()
root.title("Calculadora")
root.geometry("500x500")
root.resizable(False,False)

# Criando a variavel global para criar a expressão
expressao = ""

#Criando as funções click para criar as expressões
# Passo a passo
"""
1 - Ao clicar em um botão ele será adicionado a expressão 
2 - Se esse botão for um numero ele será adicionado a sequência numérica já existente
3 - Se ele for uma conta(+,-,x,/), ele deixará a sequência numérica e irá adicionar o simbolo da conta e logo depois
o numero
4 - Esse processo irá se repetir até o usuário clicar no botão de igual.
"""
equacao = StringVar()
def click(num):
    global expressao
    expressao = expressao + str(num) 
    equacao.set(expressao)
def LimparConta():
    global expressao
    expressao = ""
    equacao.set(expressao)
def clickIgual():
    global expressao
    try:
        total = eval(expressao)
        expressao = str(total)
        equacao.set(total)
    except:
        erro = Tk()
        erro.geometry("100x100")
        erro.resizable(False,False)
        MensagemErro = Label(erro,text="Não foi possivel realizar a conta!")    
        MensagemErro.pack()


#Criando Frames para contas

frame_conta = Entry(root,bg="blue",fg="white",textvariable=equacao,font=(15))
frame_conta.pack(pady=10, ipadx=100,ipady=30)

#Frame para juntar tanto o grid de numeros e o grid das contas onde ambos ficaram separados por um frame
frame_inferior = Frame(root,bg="cyan",width=500,height=400)
frame_inferior.pack()


frame_numeros = Frame(frame_inferior,bg="black",width=400,height=400)
frame_numeros.grid(row=0,column=0)
frame_numeros.grid_propagate(False)

frame_contas = Frame(frame_inferior,bg="red", width=100,height=400)
frame_contas.grid(row=0,column=1)
frame_contas.pack_propagate(False)
#Criando os botões de numeros
b1 = Button(frame_numeros,text="1",width=11,height=3, font=(15), command=lambda: click(1))
b2 = Button(frame_numeros,text="2",width=11,height=3, font=(15),command=lambda: click(2))
b3 = Button(frame_numeros,text="3",width=11,height=3, font=(15),command=lambda: click(3))
b4 = Button(frame_numeros,text="4",width=11,height=3, font=(15),command=lambda: click(4))
b5 = Button(frame_numeros,text="5",width=11,height=3, font=(15),command=lambda: click(5))
b6 = Button(frame_numeros,text="6",width=11,height=3, font=(15),command=lambda: click(6))
b7 = Button(frame_numeros,text="7",width=11,height=3, font=(15),command=lambda: click(7))
b8 = Button(frame_numeros,text="8",width=11,height=3, font=(15),command=lambda: click(8))
b9 = Button(frame_numeros,text="9",width=11,height=3, font=(15),command=lambda: click(9))
b0 = Button(frame_numeros,text="0",width=11,height=3, font=(15),command=lambda: click(0))
b_ponto = Button(frame_numeros,text=".",width=11,height=3, font=(12),command=lambda: click("."))
b_mais = Button(frame_contas,text="+",width=6,height=3,command=lambda: click("+"))
b_menos = Button(frame_contas,text="-",width=6,height=3,command=lambda: click("-"))
b_vezes = Button(frame_contas,text="x",width=6,height=3,command=lambda: click("*"))
b_div = Button(frame_contas,text="/",width=6,height=3,command=lambda: click("/"))
b_igual = Button(frame_contas,text="=",width=6,height=3,command=lambda: clickIgual())
b_limpar = Button(frame_numeros,text="C",width=11,height=3, font=(12),command=lambda: LimparConta())

#Posicionando em grid 4x3 os botões no Frame dos numeros

b7.grid(row=0,column=0,pady=10)
b8.grid(row=0,column=1,padx=10,pady=10)
b9.grid(row=0,column=2,pady=10)
b4.grid(row=1,column=0,pady=10)
b5.grid(row=1,column=1,padx=10,pady=10)
b6.grid(row=1,column=2,pady=10)
b1.grid(row=2,column=0,pady=10)
b2.grid(row=2,column=1,padx=10,pady=10)
b3.grid(row=2,column=2,pady=10)
b_limpar.grid(row=3,column=0,padx=10,pady=(10,0))
b0.grid(row=3,column=1,padx=10,pady=(10,0))
b_ponto.grid(row=3,column=2,padx=10,pady=(10,0))

#Posicionando as contas e o botão de igual no frame ao lado

b_mais.pack(padx=10,pady=10)
b_menos.pack(padx=10,pady=10)
b_vezes.pack(padx=10,pady=10)
b_div.pack(padx=10,pady=10)
b_igual.pack(padx=10,pady=10)



#Rodando a janela em loop
root.mainloop()