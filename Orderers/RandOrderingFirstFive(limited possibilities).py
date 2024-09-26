# -*- coding: utf-8 -*-
"""
This Orderer MAKES RANDOM ORDERS (FOR FINDING AVERAGE PATHLENGTH)
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

from random import randrange

window = tk.Tk()
window.title("Ecapsulant Point Ordering Tool")

options = tk.Frame()
checkbox = tk.Frame()
report = tk.Frame()
photobox = tk.Frame()

def sweep():
    n=80; g = 10000; pathlist = []; mat = [];
    importF = open('INPUT.txt');
    flines = importF.readlines();
    v = len(flines); iD = 0;
    for line in flines:
        templ = line.split('\t');
        x = float(templ[0]); y = float(templ[1]); 
        mat.append([x,y,iD])
        iD += 1;
    
    data = {1000:0, 900:0, 800:0, 700:0, 600:0, 500:0,
            400:0, 300:0, 200:0, 100:0, 0:0};
    
    p25 = False; p50 = False; p75 = False;
    for i in range(g):
        
        #progress (:
            
        if i >= g/4 and p25 == False:
            print("25% Done..")
            p25 = True;
        elif i >= g/2 and p50 == False:
            print("50% Done..")
            p50 = True;
        elif i >= g*3/4 and p75 == False:
            print("75% Done..")
            p75 = True;
        
        #checking first five points without writing to file 
        
        orderedpairs = [];
        usedplaces = [];
        for x in range(v):
            goodrand = False;
            while goodrand == False:
                place = randrange(v);
                if place in usedplaces:
                    goodrand = False;
                else: 
                    orderedpairs.append([place,x]);
                    usedplaces.append(place)
                    goodrand = True;

        orderedmat = [];
        for pair in orderedpairs:
            for point in mat:
                if pair[0] == point[2]:
                    orderedmat.append([point[0],point[1],pair[0]])
        
        x1 = orderedmat[0][0]; x2 = orderedmat[1][0];
        x3 = orderedmat[2][0]; x4 = orderedmat[3][0];
        x5 = orderedmat[4][0]; x6 = orderedmat[5][0];
        y1 = orderedmat[0][1]; y2 = orderedmat[1][1];
        y3 = orderedmat[2][1]; y4 = orderedmat[3][1];
        y5 = orderedmat[4][1]; y6 = orderedmat[5][1];
        fivepairs = [[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5]]
        
        dis1 = np.sqrt((x1-x2)**2+(y1-y2)**2);
        dis2 = np.sqrt((x2-x3)**2+(y2-y3)**2);
        dis3 = np.sqrt((x3-x4)**2+(y3-y4)**2);
        dis4 = np.sqrt((x4-x5)**2+(y4-y5)**2);
        
        total = dis1 + dis2 + dis3 + dis4;
        if total <= 100:
            key = 0;
            while key < total:
                key = key + 100;
            val = data[key] + 1;
            data[key] = val;
            print(fivepairs)
            
            
        
        
        #pathlist.append(round(v))
        #print(pathlist);
    groups = list(data.keys())
    values = list(data.values())
    #print(groups, values);
      
    fig = plt.figure() #figsize = (10, 5)
     
    # creating the bar plot
    plt.bar(groups, values, color ='r', width = 100);
     
    plt.xlabel("Pathlength")
    plt.ylabel("Number of Rand() Paths")
    plt.title("Distribution of Pathlengths in rand()")
    #plt.show()    
        
        


    #plt.legend(['Sin Sector Algorithm'])
    plt.savefig('temp.png');
    

def getscore(x, y, line):
    if entry.get() == '':
        column = 1;
    else:
        column = round(float(entry.get()));
    
    if entry2.get() == '':
        rot = 1;
    else:
        rot = round(float(entry2.get()));
    Dang = (rot*15)/360;
    x = x + 100
    y = y + 40
    
    r = np.sqrt(x**2 + y**2)
    if x != 0:
        Iang = np.arctan(y/x)
    else:
        Iang = np.arctan(y/(x+0.001))
    Nang = Iang + Dang;

    X = r*np.cos(Nang); Y = r*np.sin(Nang);
    
    #ang = (30*rot)/360;
    #X = x+(y*ang); Y = y-(x*ang);    
 
    var1 = int((X+50)/column);
    if var1 % 2 == 0:  var2 = 1;
    else: var2 = -1;

    prescore = var1*1000 + var2*(Y+100);
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
    v = len(flines); iD = 0;
    mat = []; scorelist = []
    scoretype = int(entry2.get());
    
    for line in flines:
        templ = line.split('\t');
        x = float(templ[0]); y = float(templ[1]); 
        mat.append([x,y,iD])
        #print(mat)

        iD += 1;
        
    #ID match to Rand()( in size )
    orderedpairs = []
    usedplaces = [];
    for x in range(v):
        goodrand = False;
        while goodrand == False:
            place = randrange(v);
            if place in usedplaces:
                goodrand = False;
            else: 
                orderedpairs.append([place,x]);
                usedplaces.append(place)
                goodrand = True;
                
    #print(orderedpairs);
    #print(mat[0], mat[1])
    #print(mat[0][2], mat[0][2], mat[1][0])
    orderedmat = [];
    for pair in orderedpairs:
        for point in mat:
            if pair[0] == point[2]:
                orderedmat.append([point[0],point[1],pair[0]])
    
    
    
    writefile =  open("OUTPUT.txt", "w");
    x = 0; y = 0; pointnum = 0; 
    usedlist = []; done = False;
    
    for point in orderedmat:
        #print(point);
        x = point[0]; y = point[1];
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
entry.insert(0,'1');
entry2 = tk.Entry(options, text="10")
entry2.grid(column=1, row=3)
entry2.insert(0,'1')
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