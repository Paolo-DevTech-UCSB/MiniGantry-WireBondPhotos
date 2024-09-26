# -*- coding: utf-8 -*-
"""
Made to Read ordered list of points off of a txt file, and return the total pathlength of the list + order. 
"""

import numpy as np

def pathlength():
    length = 0;
    importF = open('AletheasLD5.txt');
    flines = importF.readlines();
    #print(flines)
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

print(pathlength())
