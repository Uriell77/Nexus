#!/usr/bin/env python37
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 11:41:15 2019

@author: Luis Hermoso
"""

from tkinter import *
from tkinter import ttk as teka
from tkinter import messagebox
import string as st
import time
from tkinter.constants import END, SEL, SEL_FIRST, FIRST, LAST, ALL
from ClaseCarnet import *

global ID 
ID = 1.000000
global info_registro2
global info_registro2_2_2
global ENombre 
global EApellidos
global ECedula
global EFecha_de_Nacimiento
global ESexo
global EBusca
global datos
global EFecha_de_nacimiento
global EMail
global Lugar_de_Nacimiento
#global ind
global ext
global cont2
#ind = 70
global creat
creat = 2
global cant
cant = 0
global n
n=0
global es

global but
global fer
global fond
fond = "#969CBF"
global imag


def ultimo():
    with open("archivo.txt", "r") as f:
        try:
            ult = f.readlines()[-1][0:6]
            res= float("1." + ult)
        except:
            res = ID
        return res

def identidad():
    global ID
    ID = ultimo()
    ID = ID + 0.000001
    return "{:.6f}".format(ID)


def archivar(resultado):
    with open("archivo.txt", "a") as f:
        f.write(resultado + " " + "\n")
        
def primermayuscula(nom):
    nombre=""
    nomlist= nom.split(" ")
    for i in nomlist:
        nombre = nombre + " " + st.capwords(i)    
    return nombre[1:]

def validar_solo_texto(s):
    car = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for i in s:
        if i in car:
            pass
        elif i not in car:
            return False
        
def validar_solo_numeros(s):
    car = "0123456789"
    for i in s:
        if i in car:
            pass
        elif i not in car:
            return False
        
def validafecha(a):
    import datetime
    anoactual = str(datetime.date.today())[0:4]
    if (str.isdigit(a[0:2])==True 
        and len(a[0:2])==2 
        and int(a[0:2])<= 31 
        and a[2]== "/" 
        and str.isdigit(a[3:5])==True 
        and len(a[3:5])==2 
        and int(a[3:5])<= 12 
        and a[5]=="/" 
        and str.isdigit(a[6:10])==True 
        and len(a[6:10])==4 
        and int(a[6:10])>=1900
        and int(anoactual) - int(a[6:10])>= 18):
        return True
    else:
        messagebox.showwarning("Alerta de formato de datos", 
                            "no computa")
        return False
    
def registro(nombres,
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
             EMail, 
             *args):
    #validaciones y creacion de nuevo empleado en la BD
    if nombres == "" or validar_solo_texto(nombres) == False or nombres.isspace() == True:
        messagebox.showwarning("Alerta de formato de datos", 
                               'El campo Nombres no puede estar vacio\ny debe ser solo texto')
        return
    if apellidos == "" or validar_solo_texto(apellidos) == False or apellidos.isspace() == True:
        messagebox.showwarning("Alerta de formato de datos", 
                            "El campo Apellidos no puede estar vacio\ny debe ser solo texto")
        return
    if cedula == "" or validar_solo_numeros(cedula) == False or cedula.isspace() == True:
        messagebox.showwarning("Alerta de formato de datos", 
                            "El campo Cedula no puede estar vacio\ny debe ser solo numeros sin espacios")
        return
    if fecha_de_nacimiento == "" or fecha_de_nacimiento.isspace() == True or validafecha(fecha_de_nacimiento)==False:
        messagebox.showwarning("Alerta de formato de datos", 
                            "El campo Fecha de Nacimiento no puede estar vacio")
        return
    if sexo =="":
        messagebox.showwarning("Alerta de formato de datos", 
                            "El campo sexo no puede estar vacio")
        return
    id = identidad()
    info_registro2.configure(text="%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s"%(id[2:], 
                                                        nombres, 
                                                        apellidos, 
                                                        cedula, 
                                                        fecha_de_nacimiento,
                                                        lugar,
                                                        sexo,
                                                        correo))
    ENombre.delete(0, len(nombres))
    EApellido.delete(0, len(apellidos))
    ECedula.delete(0, len(cedula))
    EFecha_de_nacimiento.delete(0, len(fecha_de_nacimiento))
    ELNacimiento.delete(0, len(lugar))
    ESexo.configure(text="Masculino")
    EMail.delete(0, len(correo))
    
    res = "%s %s %s %s %s %s %s %s" %(id[2:], 
                                nombres, 
                                apellidos, 
                                cedula, 
                                fecha_de_nacimiento,
                                lugar,
                                sexo,
                                correo)
    try:
        archivar(res)
        messagebox.showinfo("Confirmacion de Registro", 
                            "Empleado Registrado con Exito\n %s"%(res))
    except:
        messagebox.showwarning("Confirmacion de Registro", 
                            "Registro Fallido\n %s"%(nombres))
    #apellido.delete(0, len(apellidos))
    #cedula.delete(0, len(cedula))
    ENombre.focus()
    
def carnet(root, es, *args):
    #Genera el archivo completo del empleado
    global but
    global text
    #global es
    global n
    #messagebox.showwarning("{}".format(es[2:8]),
     #                      "{}".format(es))
    a = Ficha_Personal(root, es)
# =============================================================================
# #clase para crear cada boton como un objeto diferente
# =============================================================================
class CrearUnBoton(object):
    
    def __init__(self, root, text, command):
        b = Button(root, 
                   text=text[0:5], 
                   justify="left",
                   bg=fond,
                   command= lambda: carnet(root, "{}".format(command)))
        b.pack(side= "top", fill="both", expand="True")
#==============================================================================
        
def buscador(s, lab, ent, datos):
    #busca coincidencias de s en la BD
    #s = palabra a buscar
    #lab = es el canvas
    #ent = el entry para borrarlo
    global n
    m = 0
    ind =50
    s = primermayuscula(s)
    for i in range(1,n+1):
        lab.delete(i)
    with open("archivo.txt", "r") as f:
        tup = []
        for i in f.readlines():
            a = i.split(" ")
            if s in a or s in a[6]:
                tup.append(a)
    for j in tup:
        a = b = c = str(j)
        a = Frame(lab, relief="groove", borderwidth=1)
        b = CrearUnBoton(a, j, j[0:len(j)-1])
        c = lab.create_window(260, 
                              ind, 
                              window=a, 
                              anchor=CENTER, 
                              width=500, 
                              height=105)
        ind += 106
        n += 1
        m += 1

#para que el scrollbar cresca con el contenido del canvas
    lab.configure(scrollregion=lab.bbox('all'))
#================================================================
    
    ent.delete(0,len(s))
    datos.configure(text="total encontrado: {}".title().format(m))
    
    
    
    
# =============================================================================
# calendario
# =============================================================================
import calendar
global diad
global mesd
global anod
global flag
flag = 'x'
diad =0
mesd = 0
anod = 0
    
    
def calendardar():
    import time
    anoactual=""
    anoactual = time.asctime()[-4:]
    datos=()
    anos=[]
    global numes
    meses=('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre')
    dias=('01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
          '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
    numes = {'Enero':'01', 'Febrero':'02', 'Marzo':'03', 'Abril':'04', 'Mayo':'05', 'Junio':'06', 'Julio':'07', 'Agosto':'08', 'Septiembre':'09', 'Octubre':'10', 'Noviembre':'11', 'Diciembre':'12'}
    for i in range(1959,(int(anoactual) - 18)):
        anos.append(i)
        
    can = calendar.Calendar(6)
    cale = calendar.Calendar.monthdayscalendar(can,1982,1)
    
    datos=[list(meses), list(dias), anos, numes]
    
    return datos

adias = calendardar()[1]
ames = calendardar()[0]
aano = calendardar()[2]

def ddiassum(flag):
    global bdias
    global bmes
    global bano
    global adias
    global diad
    global ames
    global mesd
    global aano
    global anod
    
    if flag == 'A':
       if diad < len(adias)-1:
            diad = diad + 1
            bdias = adias[diad]
            l1['text'] = bdias
       elif diad >=len(adias)-1:
            diad = 0
            bdias = adias[diad]
            l1['text'] = bdias
            
    elif flag == 'B':
        if mesd < len(ames)-1:
            mesd = mesd + 1
            bmes = ames[mesd]
            l2['text'] = bmes
        elif mesd >= len(ames)-1:
            mesd = 0
            bmes = ames[mesd]
            l2['text'] = bmes
        
    elif flag == 'C':
        if anod < len(aano)-1:
            anod = anod + 1
            bano = aano[anod]
            l3['text'] = bano
        elif anod >= len(aano)-1:
            anod = 0
            bano = aano[anod]
            l3['text'] = bano
            
    elif flag == 'D':
        diad = diad - 1
        adias = calendardar()[1]
        if diad == -1:
            diad = 30
        bdias = adias[diad]
        l1['text'] = bdias
    elif flag == 'E':
        mesd = mesd - 1
        ames = calendardar()[0]
        if mesd == -1:
            mesd = 11
        bmes = ames[mesd]
        l2['text'] = bmes
    
    elif flag == 'F':
        if anod == 0:
            anod = len(aano)-1
            bano = aano[anod]
            l3['text'] = bano
        elif anod > 0:
            anod = anod - 1
            bano = aano[anod]
            l3['text'] = bano
   # elif flag =='x':
    #    bdias = '01'
     #   bmes = 0,
      #  bano = '1959'
        
    
def colocar(entrada):
    bdias = adias[diad]
    bmes = ames[mesd]
    bano = aano[anod]
    entrada.delete(0,len("{}/{}/{}".format(bdias,numes[bmes],bano)))
    entrada.insert(0,"{}/{}/{}".format(bdias,numes[bmes],bano))
    calcu.destroy()
    

def cal(root, entrada):
    global calcu
    global l1
    global l2
    global l3
    global ent
    
    calcu = Toplevel(root)
    calcu.geometry('200x160+200+270')
    calcu.resizable(width='False', height='False')
    calcu.title('SelecCalendar')
    calcu.iconbitmap(bitmap='sdsdsdsd.ico')
    calcu.focus()

    master = Frame(calcu,bg=fond)
    master.pack(fill='both', expand='True')
    
    f1 = Frame(master, bg=fond)
    
    f11 = Frame(f1, bg=fond, pady=2, padx=2)
    b1 = Button(f11, text='▲', relief='flat', command=lambda: ddiassum('A'))
    b1.pack(fill='both')
    b1.focus()
    f11.pack(side='left', fill='both', expand='True')
    f12 = Frame(f1, bg=fond, pady=2, padx=2)
    b2 = Button(f12, text='▲', relief='flat', command=lambda: ddiassum('B'))
    b2.pack(fill='both')
    f12.pack(side='left', fill='both', expand='True')
    f13 = Frame(f1, bg=fond, pady=2, padx=2)
    b3 = Button(f13, text='▲', relief='flat', command=lambda: ddiassum('C'))
    b3.pack(fill='both')
    f13.pack(side='left', fill='both', expand='True')
    
    f1.pack(side='top', fill='both', expand='True')
    
    
    f2 = Frame(master, bg=fond)
    global adias
    global ames
    global aano
    
    f21 = Frame(f2, bg=fond, padx=2, pady=2)
    l1 = Label(f21, height=4, bg=fond, text=adias[diad])
    l1.pack(fill='x', expand='True')
    f21.pack(side='left', fill='both', expand='True')
    
    f22 = Frame(f2, bg=fond, padx=2, pady=2)
    l2 = Label(f22, height=4, bg=fond, text=ames[mesd])
    l2.pack(fill='x', expand='True')
    f22.pack(side='left', fill='both', expand='True')
    
    f23 = Frame(f2, bg=fond, padx=2, pady=2)
    l3 = Label(f23, height=4, bg=fond, text=aano[anod])
    l3.pack(fill='x', expand='True')
    f23.pack(side='left', fill='both', expand='True')
    
    f2.pack(side='top', fill='both', expand='True')
    
    f3 = Frame(master, bg=fond)
    
    f31 = Frame(f3, bg=fond, pady=2, padx=2)
    b3 = Button(f31, text='▼', relief='flat', command=lambda: ddiassum('D'))
    b3.pack(side='bottom',fill='both')
    f31.pack(side='left', fill='both', expand='True')
    f32 = Frame(f3, bg=fond, pady=2, padx=2)
    b32 = Button(f32, text='▼', relief='flat', command=lambda: ddiassum('E'))
    b32.pack(side='bottom',fill='both')
    f32.pack(side='left', fill='both', expand='True')
    f33 = Frame(f3, bg=fond, pady=2, padx=2)
    b33 = Button(f33, text='▼', relief='flat', command=lambda: ddiassum('F'))
    b33.pack(side='bottom',fill='both')
    f33.pack(side='left', fill='both', expand='True')
    
    f3.pack(side='top', fill='both', expand='True')
    
    f4 = Frame(master, bg=fond,  borderwidth=2, height=4)
    b4 = Button(f4, text='Select', relief='flat', height=4, command=lambda *args: colocar(entrada))
    b4.pack(side='bottom',fill='both')
    f4.pack(side='top', fill='both', expand='True')
    
    
    
    
def buscarimagen(imag, foto):
    
    
    from tkinter import filedialog
 
    filep = filedialog.askopenfilename()
    filep =str(filep)
    filep = filep.replace('/', '\\')
    filep = filep.replace('C:\\', 'C:\\\\')
    filep = filep.replace('\s', '\\\\s')
    imagen =PhotoImage(file='{}'.format(filep), width=100, height=100)
    imag = imagen
    foto.config(image=imag)
