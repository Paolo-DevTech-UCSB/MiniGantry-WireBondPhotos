# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:59:55 2023

@author: hep
"""

#import graphics as g
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines
import numpy as np
from matplotlib.colors import LinearSegmentedColormap 


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
        mat = np.empty((8,v), dtype = float)
        for n in range(8):
            if 8 > len(templ):
                templ.append(0);
            elif templ[n] is str:
                mat[n,z] = 0;
            elif float(templ[n]) < 0.000001 and float(templ[n]) > 0:
                mat[n,z] = 0;
            elif float(templ[n]) > -0.000001 and float(templ[n]) < 0:
                mat[n,z] = 0;
            else:
                mat[n,z] = templ[n];
        p1xi = mat[4,z];  p1yi = mat[5,z]; p2xi = mat[6,z];  p2yi = mat[7,z];
    
        p1xi = p1xi; p1yi = p1yi;
        p2xi = p2xi; p2yi = p2yi;
    
        #p1xi = (p1xi/100) -1.47; p1yi = (p1yi/100)*-1 + 3.85;
        #p2xi = (p2xi/100) -1.47; p2yi = (p2yi/100)*-1 + 3.85;
        #x2.append(p1xi); y2.append(p1yi);
        #z = z + 1;
        x2 = [p1xi,p1xi+0.3]; y2 = [p1yi,p1yi+0.3];
        #print(x2, y2);
        if b == 0:              color='red';    b = 1;
        elif b == 1:            color='orange';    b = 2;
        elif b == 2:            color='yellow';    b = 3;
        elif b == 3:            color='green';    b = 4;
        elif b == 4:            color='blue';    b = 5;
        elif b == 5:            color='purple';    b = 6;
        elif b == 6:            color='pink';    b = 0;
        plt.plot(x2, y2, 'blue');
        total = total + np.sqrt((p2yi-p1xi)**2+(p2yi-p1yi)**2);
    plt.savefig('temp.png') 
    plt.show()
    return total;
    #plt.show()

#saveplot('ref26.txt');
#x = [0,-0.5,0,1,1.5,1,0];
#y = [0,0.866,1.73,1.73,0.866,0,0];
#x2 = [0];
#y2 = [0];
#plt.plot(x, y, 'black')
#plt.plot(x2, y2, 'Green')
