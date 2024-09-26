# -*- coding: utf-8 -*-
"""
This Orderer Functions In a reletivley complex way, It does a sweep of a number of possible orientations of the S shaped algorithm

This orderer does preform well, however. More Custom Methods are out there to makemore efficient paths (BEST LD5 ~ 2100)
@author: hep
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk 
import os
import glob
from PIL import Image, ImageTk

import matplotlib.pyplot as plt
import matplotlib.patches as matches
import matplotlib.lines as mlines
import numpy as np
from matplotlib.colors import LinearSegmentedColormap 

window = tk.Tk()
window.title("Ecapsulant Point Ordering Tool")

options = tk.Frame()
checkbox = tk.Frame()
report = tk.Frame()
photobox = tk.Frame()

def sweep():
    n=100; pathlist = []
    entry2.delete(0, "end")
    entry2.insert(0, 1)
    
    for i in range(2):
        for x in range(n):
            entry.delete(0,"end")
            entry.insert(0, x+1)
            reorder()
            v = pathlength()
            pathlist.append([x,v])
        print(pathlist);

        
        plt.axis()
        p1x = 0; p1y = 0; lowest = 1000000; lown = 0;
        for datum in pathlist:
            if datum[1] < lowest:
                lowest = datum[1]; lown = datum[0];
            p2x = datum[0]; p2y = datum[1];
            x2 = [p1x,p2x]; y2 = [p1y,p2y]
            if x2 != [n-1, 0]:
                if int(entry2.get()) == 1: 
                    plt.plot(x2, y2, 'blue');
                elif int(entry2.get()) == 2:
                    plt.plot(x2, y2, 'red');
                #print(x2,y2)
                
            p1x = p2x; p1y = p2y; 
        #print(entry2.get(), n, lowest)
        #p1x = 0; p1y = 0;
        #plt.annotate('(%s,' %lowest, xy=(int(lown),int(lowest)), xytext=(int(lown),int(lowest)))
        entry2.delete(0, "end")
        entry2.insert(0, i+2)
        #plt.plot([lown,lown], [0, lowest], 'black');   
        
    plt.legend(['Sin Sector Algorithm'])
    plt.savefig('temp.png');
    

def getscore(x, y, line):
    if entry.get() == '':
        column = 1;
    else:
        column = round(float(entry.get()));
    var1 = int((x+50)/column);
    if var1 % 2 == 0:  var2 = 1;
    else: var2 = -1;

    prescore = var1*1000 + var2*(y+100);
    score = int(prescore);
    #print(var1, var2)
    return (score);

def getscore2(x, y, line):
    if entry.get() == '':
        column = 1;
    else:
        column = round(float(entry.get()));
    var1 = int((y+50)/column);    
    if var1 % 2 == 0:  var2 = 1;
    else: var2 = -1;

    prescore = var1*1000 + var2*(x+100);
    score = int(prescore);
    #print(var1, var2)
    return (score);

def pathlength():
    length = 0;
    importF = open('OUTPUT.txt');
    flines = importF.readlines();
    v = len(flines); lz = 0;
    for line in flines:
        templ = line.split('\t');
        x = float(templ[0]); y = float(templ[1]);
        if lz != 0:
            dis = np.sqrt((lastx - x)**2+(lasty - y)**2)
        else: dis = 0;
        lz += 1; lastx = x; lasty = y;
        length += dis; 
    #print(scorelist)
    return length;
    
def reorder():
    importF = open('INPUT.txt');
    flines = importF.readlines();
    v = len(flines); lz = 0;
    mat = []; scorelist = []
    scoretype = int(entry2.get());
    
    for line in flines:
        templ = line.split('\t');
        x = float(templ[0]); y = float(templ[1]);
        if scoretype == 1: 
            score = getscore(x,y,lz); 
        elif scoretype == 2:
            score = getscore2(x,y,lz); 
        else:
            score = getscore(x,y,lz);
        
        #print(x, y, score);
        mat.append([x,y,score])
        #print(mat)
        scorelist.append(score)
        lz += 1;
    #print(scorelist)
    orderedlist = [];
    size = len(scorelist)

    for x in range(size):
        smallest = min(scorelist)
        orderedlist.append(smallest)
        scorelist.remove(smallest)
    #print(size, len(orderedlist))
    #print(orderedlist)    
    
    writefile =  open("OUTPUT.txt", "w");
    x = 0; y = 0; pointnum = 0; 
    usedlist = []; done = False;
    
    for score in orderedlist:
        for point in mat:
            if [point[0],point[1]] not in usedlist:
                if round(score) == round(point[2]):
                    if done == False:
                        usedlist.append([point[0],point[1]])
                        #print(point);
                        x = point[0]; y = point[1];
                        writefile.write(str(x) + '\t' + str(y) +'\n')
                        #print( str(pointnum+1) +': '+ str(x) + '\t' + str(y));
                        done = True;
            else: 
                if round(score) == round(point[2]):
                    #print('parity')
                    b = point[0]; u = point[1];
                    #writefile.write(str(x) + '\t' + str(y) +'\n')
                    #print( str(pointnum+1) +': '+ str(x) + '\t' + str(y));
                
        #print(score)            
        pointnum += 1;
        done = False;
    #print('this is len usedlist, ', len(usedlist))
    #print('this is len of mat', pointnum)
    writefile.close();
    return;

def saveplot(filename):
    plt.axis('equal')
    #plt.axis('off')
    
    importF = open(filename);
    flines = importF.readlines();
    v = len(flines);
    z = 0;
    total = 0;
    b = 0;
    for line in flines:
        templ = line.split('\t');
        mat = np.empty((2,v), dtype = float)
        for n in range(2):
            if 2 > len(templ):
                templ.append(0);
            elif templ[n] is str:
                mat[n,z] = 0;s
            elif float(templ[n]) < 0.000001 and float(templ[n]) > 0:
                mat[n,z] = (0);
            elif float(templ[n]) > -0.000001 and float(templ[n]) < 0:
                mat[n,z] = 0;
            else:
                mat[n,z] = templ[n];
        p1xi = mat[0,z];  p1yi = mat[1,z]; 
        if z == 0:
            p2xi = mat[0,z];  p2yi = mat[1,z];
    
        p1xi = p1xi; p1yi = p1yi;
        p2xi = p2xi; p2yi = p2yi;
    
        #p1xi = (p1xi/100) -1.47; p1yi = (p1yi/100)*-1 + 3.85;
        #p2xi = (p2xi/100) -1.47; p2yi = (p2yi/100)*-1 + 3.85;
        #x2.append(p1xi); y2.append(p1yi);
        
        
        z = z + 1;
        x2 = [p1xi,p2xi]; y2 = [p1yi,p2yi];
        #print(x2, y2);
        if b == 0:              color='red';    b = 1;
        elif b == 1:            color='orange';    b = 2;
        elif b == 2:            color='yellow';    b = 3;
        elif b == 3:            color='green';    b = 4;
        elif b == 4:            color='blue';    b = 5;
        elif b == 5:            color='purple';    b = 6;
        elif b == 6:            color='pink';    b = 0;
        plt.plot(x2, y2, color);
        #total = total + np.sqrt((p2xi-p1xi)**2+(p2yi-p1yi)**2);
        
        p2xi = p1xi; p2yi = p1yi;
        #total += np.sqrt((p2xi-p1xi)**2+(p2yi-p2xi)**2)
    
    
    
    plt.savefig('temp.png') 
    plt.close()
    #plt.show()
    return total;
    
    
def checkref(*args):
    saveplot('OUTPUT.txt')
    path = pathlength();
    
    photo = PhotoImage(file = 'temp.png')
    photo = photo.subsample(1)
    lbl = Label(photobox,image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=3)
    tk.Label(report, text=path).grid(column=2, row=1, sticky=W)
    report.pack()
    
def temp(*args):
    path = 'NA'
    photo = PhotoImage(file = 'temp.png')
    photo = photo.subsample(1)
    lbl = Label(photobox,image = photo)
    lbl.image = photo
    lbl.grid(column=0, row=3)
    tk.Label(report, text=path).grid(column=2, row=1, sticky=W)
    report.pack()
    

entry = tk.Entry(options, text="50")
entry.grid(column=1, row=2)
entry2 = tk.Entry(options, text="10")
entry2.grid(column=1, row=3)
tk.Button(checkbox, text="plot",command=checkref).grid(column=1, row=1, sticky=W)
tk.Button(checkbox, text="reorder",command=reorder).grid(column=2, row=1, sticky=W)
tk.Button(checkbox, text="sweep",command=sweep).grid(column=3, row=1, sticky=W)
tk.Button(checkbox, text="temp",command=temp).grid(column=4, row=1, sticky=W)
tk.Label(report, text="Pathlength: ").grid(column=1, row=1, sticky=W)
tk.Label(report, text="").grid(column=2, row=1, sticky=W)

photo = PhotoImage(file = 'temp.png')
photo = photo.subsample(1)
lbl = Label(photobox,image = photo)
lbl.image = photo
lbl.grid(column=0, row=3)

options.pack()
checkbox.pack()
photobox.pack()
report.pack()

window.mainloop()