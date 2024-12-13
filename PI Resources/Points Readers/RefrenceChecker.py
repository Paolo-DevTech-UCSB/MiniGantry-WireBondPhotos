# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:34:40 2023

@author: hep
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk 
import os
import glueplotsimple as gps
import glueplotsimple_points
import glueplotsimple_black
import glob
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Encapsulant Refrence Txt Previewer")

RefSelect = tk.Frame()
checkbox = tk.Frame()
report = tk.Frame()
photobox = tk.Frame()

def buttonL(*args):
    match = False; 
    reflist = glob.glob("*.txt")
    for i in range(len(reflist)-1): 
        if match == False:
            #print('run:', i, match, reflist[i], entry.get())
            if entry.get() == reflist[i]:
                #print('case1')
                entry.delete(0,len(entry.get()))
                entry.insert(0, reflist[i-1])
                match = True;
            elif entry.get() == reflist[0]:
                #print('case2')
                entry.delete(0,len(entry.get()))
                entry.insert(0, reflist[-1])
                match = True;
    if match == False:
        #print('case3')
        entry.delete(0,len(entry.get()))
        entry.insert(0, reflist[i])
        match = True;
    
def buttonR(*args):
    match = False; 
    reflist = glob.glob("*.txt")
    for i in range(len(reflist)-1): 
        if match == False:
            #print('run:', i, match, reflist[i], entry.get())
            if entry.get() == reflist[i]:
                #print('case1')
                entry.delete(0,len(entry.get()))
                entry.insert(0, reflist[i+1])
                match = True;
            elif entry.get() == reflist[-1]:
                #print('case2')
                entry.delete(0,len(entry.get()))
                entry.insert(0, reflist[0])
                match = True;
    if match == False:
        #print('case3')
        entry.delete(0,len(reflist)+4)
        entry.insert(0, reflist[i])
        match = True;
    
def checkref(*args):
    pathlength = gps.saveplot(entry.get())
    photo = PhotoImage(file = 'temp.png')
    photo = photo.subsample(1)
    lbl = Label(photobox,image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=3)
    tk.Label(report, text=pathlength).grid(column=2, row=1, sticky=W)
    report.pack()
    
def checkref_points(*args):
    pathlength = glueplotsimple_points.saveplot(entry.get())
    photo = PhotoImage(file = 'temp.png')
    photo = photo.subsample(1)
    lbl = Label(photobox,image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=3)
    tk.Label(report, text=pathlength).grid(column=2, row=1, sticky=W)
    report.pack()
    
def checkref_black(*args):
    pathlength = glueplotsimple_black.saveplot(entry.get())
    photo = PhotoImage(file = 'temp.png')
    photo = photo.subsample(1)
    lbl = Label(photobox,image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=3)
    tk.Label(report, text=pathlength).grid(column=2, row=1, sticky=W)
    report.pack()
    

label = tk.Label(text="Name")
entry = tk.Entry(RefSelect)
name = entry.get()
tk.Button(RefSelect, text="<",command=buttonL).grid(column=1, row=1, sticky=W)
entry.grid(column=2, row=1, sticky=W)
tk.Button(RefSelect, text=">",command=buttonR).grid(column=3, row=1, sticky=W)

tk.Button(checkbox, text="check (Points)",command=checkref_points).grid(column=1, row=1, sticky=W)
tk.Button(checkbox, text="check",command=checkref).grid(column=2, row=1, sticky=W)
tk.Button(checkbox, text="check (Black)",command=checkref_black).grid(column=3, row=1, sticky=W)
tk.Label(report, text="Pathlength: ").grid(column=1, row=1, sticky=W)
tk.Label(report, text="").grid(column=2, row=1, sticky=W)

photo = PhotoImage(file = 'temp.png')
photo = photo.subsample(1)
lbl = Label(photobox,image = photo)
lbl.image = photo
lbl.grid(column=0, row=3)

label.pack()
RefSelect.pack()
checkbox.pack()
photobox.pack()
report.pack()

window.mainloop()