# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 16:16:10 2019

@author: Luis Hermoso
"""

from tkinter import *

root = Tk()
root.geometry("300x290+0+0")
root.configure()
root.title("formato")

a = ['000029', 'Marcos', 'Carlos', 'Barrientos', 'Barragan', '56465465', '05/06/1982', 'Masculino']

es = '''ID: {}
Nombres: {} {}
Apellidos: {} {}
C.I: {}
Fecha de Nacimiento: {}
Sexo: {}'''.format(a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
fr = Frame(root, bg="red")

bot = Button(fr, width=40, height=8, justify="left", text=es.title())
bot.pack(anchor="center", expand="True")

fr.pack(fill="both", expand="True", anchor="center")

root.mainloop()