#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:30:37 2019
Proyecto: Nexus
@author: Luis Hermoso
"""

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext as scr
import funciones

#Variables Globales
global ENombre
global EApellido
global ECedula
global EFecha_de_nacimiento
global ESexo
global EMail
global Lugar_de_Nacimiento
global info_registro2
global EBusca
global info_registro2_2_2
global cont2
global ext
global n
global datos
ext= 480
global fond
fond = "#969CBF"
global root
global imag

#UI
root = Tk()
root.geometry("1366x695+-10+0")
root.title("Proyecto Nexus")
#root.iconbitmap(bitmap='short.ico')

#Variables de Formulario
ID = 1.000000
Nombres = StringVar()
Apellidos = StringVar()
Cedula = StringVar()
Lugar_de_Nacimiento = StringVar()
Fecha_de_Nacimiento = StringVar()
Busca = StringVar()
Email = StringVar()
#Sexo = ESexo.get()

#funcion de ejecucion(llamadas externas)
def ejecutar(*args):
    #toma de datos
    nombres = Nombres.get()
    apellidos = Apellidos.get()
    cedula = Cedula.get()
    fecha_de_nacimiento = Fecha_de_Nacimiento.get()
    sexo = ESexo.get()
    lugar = Lugar_de_Nacimiento.get()
    correo = Email.get()
    nombres = funciones.primermayuscula(nombres)
    apellidos = funciones.primermayuscula(apellidos)
    
    funciones.registro(nombres, 
                       apellidos, 
                       cedula, 
                       fecha_de_nacimiento,
                       lugar,
                       sexo,
                       correo,
                       info_registro2, 
                       ENombre, 
                       EApellido, 
                       ECedula, 
                       EFecha_de_nacimiento,
                       ELNacimiento,
                       ESexo,
                       EMail)
   
def buscar(*args):
    busca = Busca.get()
    funciones.buscador(busca, info_registro2_2_2, EBusca, datos)
    
#plano base   
base = Frame(root, 
             bg=fond, 
             relief="groove", 
             borderwidth=2)
base.pack(fill="both", expand="True", pady=20)

#titulo
texto = ttk.Label(base, 
              text="    Sistema de Administracion Nexus", 
              font=("Impact", 20),
              background=fond, 
              width=50, 
              #height=1, 
              justify="left")
texto.place(x=0, y=0)

#pie de pagina
textopie = Label(base, 
                 text='Hecho por GP System, Media & Games. Ing. Luis Hermoso Copyright 2019', 
                 font=("Arial",7),
                 justify="left",
                 height=2,
                 width=3,
                 bg="#11143d",
                 relief="flat",
                 foreground="white")
textopie.pack(side="bottom", fill='both')

#menu de pestanas
menu = ttk.Notebook(base)
menu.pack(expand=1, fill='both', pady=50, padx=20)

#grupo de pestanas
pestana1 = ttk.Frame(menu)
pestana2 = ttk.Frame(menu)
pestana3 = ttk.Frame(menu)
pestana4 = ttk.Frame(menu)

#asigna las pestanas a el menu
menu.add(pestana1, text=" Registro ")
menu.add(pestana2, text=" Búsqueda ")
menu.add(pestana3, text=" Edición ")
menu.add(pestana4, text=" Ayuda ")

#planos de contenido de cada pestana
#plano pestana 1
cont1 = ttk.Label(pestana1, width=50, relief="groove", text="entonc1")
cont1.pack(expand="True", fill="both")

#plano pestana 2
cont2 = ttk.Label(pestana2, width=50, relief="groove", text="entonc2")
cont2.pack(expand="True", fill="both")

#plano pestana 3
cont3 = ttk.Label(pestana3, width=50, relief="groove", text="entonc3")
cont3.pack(expand="True", fill="both")

#plano pestana 4
cont4 = ttk.Label(pestana4, width=50, relief="groove", text="entonc4")
cont4.pack(expand="True", fill="both")

#plano base del formulario alineado a la izquierda asociado a plano pestana 1
info_registro = Frame(cont1, width=700, height=900, borderwidth=2, relief="groove", bg=fond)
info_registro.pack(side="left")

#plano base del contenido del formulario alineado a la derecha
info_registro2 = Label(cont1, width=700, height=500, borderwidth=2, relief="groove")
info_registro2.pack(side="right")




#texto encabezado del formulario
encabezado = Label(info_registro, bg=fond, text="Registre  los datos del empleado ", font=("Bold")).place(x=4, y=4)

#plano base del formulario alineado a la izquierda asociado a plano pestana 2
info_registro2_2 = Frame(cont2, width=700, height=900, borderwidth=2, relief="groove", bg=fond)
info_registro2_2.pack(side="left")

#plano base del contenido del formulario alineado a la derecha pestana 2
loop = Scrollbar(cont2)
loop.pack(side="right", fill="y")

datos = Label(cont2, text="")
datos.pack(side="top")
info_registro2_2_2 = Canvas(cont2, 
                            width = 520, 
                            yscrollcommand=loop.set)
                            #scrollregion=(0,0,0, 480))

info_registro2_2_2.pack(side="left", fill="y", expand="True")

loop.config(command=info_registro2_2_2.yview)


#textos para los elementos del formulario pestana 1
nombre = Label(info_registro, text="Nombres: ", bg=fond).place(x=4, y=50)
apellido = Label(info_registro, text="Apellidos: ", bg=fond).place(x=280, y=50)
cedula = Label(info_registro, text="Cedula: ", bg=fond).place(x=4, y=100)
lugar_de_nacimiento = Label(info_registro, text="Lugar de\nNacimiento: ",
                            justify="left", bg=fond).place(x=190, y=90)
fecha_de_nacimiento = Label(info_registro, 
                            text="Fecha de\nNacimiento:\n%s"%("(dd/mm/aaaa)"), 
                            justify="left", bg=fond).place(x=4, y=140)
sexo = Label(info_registro, text="Sexo: ", bg=fond).place(x=225, y=150)
email = Label(info_registro, text="EMail: ", bg=fond).place(x=4, y=200)
#entradas del formulario pestana 1
ENombre = Entry(info_registro, textvariable=Nombres, width=30)
ENombre.focus()
ENombre.place(x=78, y=50)

EApellido = Entry(info_registro, textvariable=Apellidos, width=30)
EApellido.place(x=350, y=50)

ECedula = Entry(info_registro, textvariable=Cedula, width=17)
ECedula.place(x=78, y=100)

ELNacimiento = Entry(info_registro, width=43, textvariable=Lugar_de_Nacimiento)
ELNacimiento.place(x=270, y=100)

EFecha_de_nacimiento = Entry(info_registro, textvariable=Fecha_de_Nacimiento, width=17)
EFecha_de_nacimiento.place(x=78, y=150)

ESexo = Spinbox(info_registro, values=("Masculino", "Femenino"), width=15, exportselection="True")
ESexo.place(x=270, y=150)

EMail = Entry(info_registro, textvariable=Email, width=40)
EMail.place(x=78, y=200)

#imag = PhotoImage(file='50hc.png')
#foto = Button(info_registro, image=imag, width=100, height=100, command=lambda :funciones.buscarimagen(imag, foto))
#foto.place(x=580, y=40)

#botones pestana 1
but1 = Button(info_registro, text="Registrar", width=10, underline=0, command=ejecutar)
root.bind("<Alt-r>", ejecutar)
but1.place(x=150, y=400)

but2 = Button(info_registro, text="Salir", width=10, underline=0, command=lambda: root.destroy())
root.bind("<Alt-s>", lambda *args: root.destroy())
but2.place(x=300, y=400)

but3 = Button(info_registro, text="C", command=lambda: funciones.cal(root, EFecha_de_nacimiento))
but3.place(x=185, y=148)

#texto pestana 2
#texto encabezado del formulario 2
encabezado = Label(info_registro2_2, text="Busqueda de Empleados", font=("Bold"), bg=fond).place(x=4, y=4)
Buscar = Label(info_registro2_2, text="Busqueda: ", bg=fond).place(x=4, y=50)
#entrada en pestana 2
EBusca = Entry(info_registro2_2, textvariable=Busca, width=50)
EBusca.focus()
EBusca.place(x=150, y=50)

#boton pestana 2
but1_2 = Button(info_registro2_2, text="Buscar", width=10, underline=0, command=buscar)
root.bind("<Alt-b>", buscar)
but1_2.bind('<Return>', buscar)
but1_2.place(x=150, y=200)

but2_2 = Button(info_registro2_2, text="Salir", width=10, underline=0, command=lambda: root.destroy())
root.bind("<Alt-s>", lambda *args: root.destroy())
but2_2.place(x=400, y=200)


#fin del UI
root.mainloop()