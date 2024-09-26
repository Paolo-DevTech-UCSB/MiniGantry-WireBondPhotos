# -*- coding: utf-8 -*-
"""
This Orderer Functions Similarly to the others, It takes a list of X and Y values as points, 
This List of Points is REORDERED and output into a separate text file.

 the reason it's called High Comp Ordering is becuase it has recursive methods (NOT GREAT RESULTS) (BEST LD5 ~ 6800)
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
    dismat = []; 
    flinesmat = [];
    orderedmat = [];
    
    for line in flines:
        templ = line.split('\t');
        x = float(templ[0]); y = float(templ[1]);
        flinesmat.append([x , y]);
    flinesmat2 = flinesmat;
    newflinesmat = flinesmat;
        
    for r in range(v):
        
        #print(len(newflinesmat))

        flinesmat = newflinesmat;
        flinesmat2 = newflinesmat; 
            

        dismat = [];
        for point in flinesmat:
            for point2 in flinesmat:
                if point != point2:
                    #print(point, point2)
                    X = point[0] - point2[0];
                    Y = point[1] - point2[1]; 
                    distance = np.sqrt(X**2 + Y**2);
                    dismat.append([distance, point[0], point[1], point2[0], point2[1]])
        lowest = 1000;
        
        
        
        for data in dismat:
            if data[0] < lowest:
                lowest = data[0]; lx = data[1]; ly = data[2];
        print(lowest)
        orderedmat.append([lowest, lx, ly]);
        
        #print(len(newflinesmat), len(flinesmat))
        newflinesmat = []
        for line in flinesmat:
            if line != [orderedmat[-1][1],orderedmat[-1][2]]:
                newflinesmat.append(line)
         
        #flinesmat = [];
        
    #print(orderedmat);

    writefile =  open("OUTPUT.txt", "w");
    x = 0; y = 0; pointnum = 0; 
    usedlist = []; done = False;
    
    for point in orderedmat:
        x = point[1]; y = point[2];
        writefile.write(str(x) + '\t' + str(y) +'\n')

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
                mat[n,z] = 0;
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
    plt.show()
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
    
    

tk.Button(checkbox, text="plot",command=checkref).grid(column=1, row=1, sticky=W)
tk.Button(checkbox, text="reorder",command=reorder).grid(column=2, row=1, sticky=W)
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