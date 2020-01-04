#!/usr/bin/env 
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 13:02:56 2019
@author: Ing. Luis Hermoso
Empresa: GP System, Media & Games
"""
from tkinter import *
from tkinter import filedialog
from time import sleep
import math
import csv
global fond
global grupo
global tert
global cero
fond = "#969CBF"

def actualizar(etiqueta):
    etiqueta.update()

def reescribir(dato, nota, grupo, agrega):
    f = open("{}.csv".format(grupo), "r")
    linea = f.readlines()
    f.close()
    f = open("{}.csv".format(grupo), "w")
    for i in linea:
        if dato in i:
            note = '{},\n'.format(i[:-1] + nota)
            #fech = '{},\n'.format((linea[0])[:-1] + fecha)
            #linea[0] = fech
            linea[linea.index(i)]= note
            #print(linea)
    f.writelines(linea)
    f.close()
    enter4.delete(0,len(nota))
    agrega.destroy()
    
    

def AgregarNota(dato, grupo):
            global enter4
            nota = StringVar()
            
            #print(dato)
            agrega =Toplevel(fp)
            agrega.geometry('300x300+{}+{}'.format(equis+40,ye+200))
            agrega.configure(pady=10, padx=10)
            agrega.resizable(width=0, height=0)
            fren = Frame(agrega, bg=fond, borderwidth=2, relief='groove')
            fren.pack(fill='both', expand='True')
            
            labis4 = LabelFrame(fren, text='Nota', bg=fond)
            labis4.pack(fill='x', expand='True')
            
            
            enter4 = Entry(labis4, justify='center', textvariable=nota)
            enter4.pack()
            
            
            but2 = Button(fren, text='Agregar', command=lambda:reescribir((dat[1])[2:-1], enter4.get(), grupo, agrega))
            but2.pack()
            
class CrearUnBoton(object):
    
    def __init__(self, root, tert, command, grupo, cero):
        global b
        global cer
        global lista
        cer = cero
        b = Button(root, 
                   text='{}  {}'.format(tert, (dat[cero.index(tert)])[2:-1]),
                   justify="left",bg=fond,
                   command= lambda: AgregarNota((dat[1])[2:-1], grupo))
        b.pack(side= "top", fill='x')
        
        prom = []
        for i in dat[5:-1]:
            prom.append(i)
            #print((dat[5])[1:-1])
        
def promedio(note):
    #print('esto es note', note)
    b = []
    a = 0
    #print(len(note)-1)
    for i in note[:-1]:
        #print(i[2:-1])
        if i[2:-1] in ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):
            b.append(i)
        else:
            next
        print(b)
    for j in b:
        print(j[2:-1])
        a = int(a) + int(j[2:-1])
        #print(a)
    if len(b)==0:
        res = a
    else:
        #print(len(b))
        res = a/(len(b))
    return res
        
class Ficha_Personal(object):
    global grupo
    
    def __init__(self, padre, command, grupo, cero):
        global dat
        global fp
        global equis
        global ye
        global frank3
        global lib2

        equis = 300
        ye = 0
        fp = Toplevel(padre,
                      bg=fond,
                      padx=10,
                      pady=10)
        fp.geometry('600x690+{}+{}'.format(equis,ye))
        fp.resizable(width=0, height=0)
        frank1 = Frame(fp,
                       height=480,
                       width=480)
        frank1.pack(fill='both')
        
        frank2 = Frame(fp,
                       height=480,
                       width=480)
        frank2.pack(fill='both', expand='True', side='left')
        
        dat=[]
        for i in (command[1:-1].split(',')):
            dat.append(i)
        #print(type(dat))
        labe1 = Label(frank1,
                    bg=fond,
                    padx=10,
                    pady=10,
                    justify='left')
        labe1.pack(side='left', fill='both', expand='True')
        
        
        lib1 = Label(labe1,
                     text = str.title('Apellidos: {}\n\nNombres: {}\n\nCedula: {}\n\nMencion: {}\n\nDireccion: {}').format((dat[0])[1:-1],
                                     (dat[1])[2:-1],(dat[2])[2:-1],(dat[3])[2:-1],str(dat[4])[2:-1]),
                     justify='left',
                     relief='groove',
                     borderwidth=2,
                     bg=fond,
                     height=10)
        lib1.pack(side='left')
        
        
        lib2 = Label(labe1,
                     text =str.title('Promedio'),
                     justify='left',
                     relief='groove',
                     borderwidth=2,
                     bg=fond,
                     height=8,
                     width=200,
                     font=('Bold',12))
        lib2.pack(side='right')
        
        
        #print(len(dat))
        if len(dat)>6:
            lib2['text'] = '{}\n\n{} = {}'.format('Promedio: ',promedio(dat[5:]), (promedio(dat[5:]))/2.5)
        else:
            pass
        
        frank3 = Frame(frank2,
                       bg='',
                       height=50, borderwidth=2, relief='groove')
        frank3.pack(fill='both', side='left', expand='True')
        cero = cero.split(',')
        cero =tuple(cero)
        if len(cero) > 6:
            #print(cero)
            for i in range(5, len(cero)-1):
                CrearUnBoton(frank3, cero[i], cero[i], grupo, cero)
                

                
        
     
