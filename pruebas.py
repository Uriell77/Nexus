
#!/usr/bin/env python37

from tkinter import *
from tkinter import messagebox
from tkinter.constants import END, SEL, SEL_FIRST, FIRST, LAST, ALL
import pdb


global ter
global ind
global creat
creat =""
ind = 45
global n

vent = Tk()
vent.geometry("300x300")
entrada = StringVar()


def dale():
    global ind
    global creat
    global n
    n = 0
    dal = entrada.get()
    fr = Frame(ter, relief="groove", borderwidth=1)
    Button(fr, text=dal, wraplength=100, command=lambda:messagebox.showwarning("si","funciona {}".format(dal))).pack(fill="both", side="top", expand="True")
    creat = ter.create_window(140, ind, window=fr, anchor=CENTER, width=270, height=80)
    #print(creat)
    n = creat + 1
    #ter.create_text(80, ind, text=dal, anchor="center")
    #ter.pack()
    ind = ind + 82
    ent.delete(0, len(dal))
    
def borra():
    global ind
    global n
    global creat
    for i in range(1,n):
        #print(n)
        ter.delete(i)
        ind = 45


ent = Entry(vent, textvariable=entrada, relief="groove", borderwidth=3)
ent.pack(side="top", pady=3)

cont = Frame(vent, relief="groove", borderwidth=3, bg="blue")

bot = Button(cont, text="dale", command=dale, width=10)
bot.pack(side="left", padx=3)
bot1 = Button(cont, text="borra", command=borra, width=10)
bot1.pack(side="right", padx=3)

cont.pack(side="top", padx=5)


loop = Scrollbar(vent, )
                 #orient="vertical",
                 #command = ter.yview,
                 #width=200,)
                 #borderwidth=2,
                 #relief="ridge")
loop.pack(side="right", fill="y")

ter = Canvas(vent, 
             yscrollcommand=loop.set,
             scrollregion=(0,0,0,1000),
             #width=270,
             #height=240,
             #borderwidth=2, 
             bg="red") 
             #relief="ridge")
ter.pack(side="left", fill="both", expand="True")

loop.config(command = ter.yview)



#loop.config(command=ter.yview)
vent.mainloop()
