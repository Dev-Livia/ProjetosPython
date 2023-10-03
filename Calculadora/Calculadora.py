from asyncio import events
from tkinter import * 
from tkinter import ttk

cor1 = "#505254"
cor2 = "#f7f3f2"
cor3 = "#3171b0"
cor4 = "#636669"
cor5 = "#f77102" 

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")

janela.config(bg=cor1)

#CRIANDO FRAMES

frame_Tela = Frame(janela, width = 235, height = 50, bg=cor3 )
frame_Tela.grid(row = 0, column = 0 )

frame_Corpo = Frame(janela, width=235 , height=268)
frame_Corpo.grid(row=1, column=0)

#DECLARANDO VARIAVEIS

todos_Valores = ''

#CRIANDO LABEL
valor_texto = StringVar()
app_lab = Label(frame_Tela, textvariable= valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18 '),bg=cor3)
app_lab.place(x=0,y=0)

# CRIANDO FUNÇÃO 
def entrada_Valores(event):
    global todos_Valores
    todos_Valores = todos_Valores + str(event)
    #passando valor para tela
    valor_texto.set(todos_Valores)

# FUNÇÃO PARA CALCULAR
def calcular():
    global todos_Valores
    try:
        resultado = eval(todos_Valores)
        valor_texto.set(resultado)
        todos_Valores = str(resultado)  # Atualiza todos_Valores com o resultado para cálculos subsequentes
    except Exception as e:
        valor_texto.set("Erro")
        todos_Valores = ""

# FUNÇÃO LIMPAR TELA
def limpar_tela():
    global todos_Valores
    todos_Valores = ""
    valor_texto.set("")
#CRIANDO BOTÕES

#PRIMEIRA LINHA
botão01 = Button(frame_Corpo, command= limpar_tela, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão01.place(x=0, y=0)

botão02 = Button(frame_Corpo, command= lambda: entrada_Valores('%'), text='%', width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão02.place(x=118, y=0)
botão03 = Button(frame_Corpo, command= lambda: entrada_Valores('/'), text="/", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão03.place(x=177, y=0)
#SEGUNDA LINHA 
botão04 = Button(frame_Corpo, command= lambda: entrada_Valores('7'), text="7", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão04.place(x=0, y=52)
botão05 = Button(frame_Corpo, command= lambda: entrada_Valores('8'), text="8", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão05.place(x=59, y=52)
botão06 = Button(frame_Corpo, command= lambda: entrada_Valores('9'), text="9", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão06.place(x=118, y=52)
botão07 = Button(frame_Corpo, command= lambda: entrada_Valores('*'), text="*", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão07.place(x=177, y=52)
#TERCEIRA LINHA    
botão08 = Button(frame_Corpo, command= lambda: entrada_Valores('4'), text="4", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão08.place(x=0, y=104)
botão09 = Button(frame_Corpo, command= lambda: entrada_Valores('5'), text="5", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão09.place(x=59, y=104)
botão10 = Button(frame_Corpo, command= lambda: entrada_Valores('6'), text="6", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão10.place(x=118, y=104)
botão11 = Button(frame_Corpo, command= lambda: entrada_Valores('-'), text="-", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão11.place(x=177, y=104)
#QUARTA LINHA
botão12 = Button(frame_Corpo, command= lambda: entrada_Valores('1'), text="1", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão12.place(x=0, y=156)
botão13 = Button(frame_Corpo, command= lambda: entrada_Valores('2'), text="2", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão13.place(x=59, y=156)
botão14 = Button(frame_Corpo, command= lambda: entrada_Valores('3'), text="3", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão14.place(x=118, y=156)
botão15 = Button(frame_Corpo, command= lambda: entrada_Valores('+'), text="+", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão15.place(x=177, y=156)
#QUINTA LINHA
botão16 = Button(frame_Corpo, command= lambda: entrada_Valores('0'), text="0", width=11, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão16.place(x=0, y=208)
botão17 = Button(frame_Corpo, command= lambda: entrada_Valores('.'), text=".", width=5, height=2, bg=cor4, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão17.place(x=118, y=208)
botão18 = Button(frame_Corpo, command= calcular, text="=", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
botão18.place(x=177, y=208)

janela.mainloop()
