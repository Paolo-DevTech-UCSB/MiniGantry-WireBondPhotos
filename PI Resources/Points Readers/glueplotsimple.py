# -*- coding: utf-8 -*-
"""
This Code takes an ordered list of points as it's input, and returns a plot of the path.
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
    g = 0;
    for line in flines:
        templ = line.split('\t');
        #print(templ)
        mat = np.empty((2,v), dtype = float)
        for n in range(2):
                mat[n,z] = templ[n];
                       
        
        if g == 0:
            p1xi = mat[0,z];  p1yi = mat[1,z]; p2xi = mat[0,z];  p2yi = mat[1,z];
        else: 
            p1xi = mat[0,z];  p1yi = mat[1,z];
        
        g = g + 1;
        
        p1xi = p1xi; p1yi = p1yi;
        p2xi = p2xi; p2yi = p2yi;
    
        #p1xi = (p1xi/100) -1.47; p1yi = (p1yi/100)*-1 + 3.85;
        #p2xi = (p2xi/100) -1.47; p2yi = (p2yi/100)*-1 + 3.85;
        #x2.append(p1xi); y2.append(p1yi);
        #z = z + 1;
        x2 = [p1xi,p2xi]; y2 = [p1yi,p2yi];
        print(x2, y2);
        if b == 0:              color='red';    b = 1;
        elif b == 1:            color='orange';    b = 2;
        elif b == 2:            color='yellow';    b = 3;
        elif b == 3:            color='green';    b = 4;
        elif b == 4:            color='blue';    b = 5;
        elif b == 5:            color='purple';    b = 6;
        elif b == 6:            color='pink';    b = 0;
        plt.plot(x2, y2, color);
        #print(x2, y2)
        #total = total + np.sqrt((p2yi-p1xi)**2+(p2yi-p1yi)**2);
        p2xi = mat[0,z];  p2yi = mat[1,z];
    print(mat) 
    plt.savefig('temp.png') 
    #plt.show()
    return total;
    plt.show()

saveplot('OUTPUT.txt');
#x = [0,-0.5,0,1,1.5,1,0];
#y = [0,0.866,1.73,1.73,0.866,0,0];
#x2 = [0];
#y2 = [0];
#plt.plot(x, y, 'black')
#plt.plot(x2, y2, 'Green')
