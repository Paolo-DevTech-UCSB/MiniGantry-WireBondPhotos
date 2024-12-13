# -*- coding: utf-8 -*-
"""
This Code reads from a codex,
this codex contains the location, names, and cells of all the stepped holes. 
(WireBond Photo's takes pictures of these holes)

The Point of this code is to used that Codex to OPEN and INTERPRET a Minigantry program, 
And return all the points in the code, as well as the hole number and cells. 

Becuase it take mini ganty code as an input, this is a good program for double checking a minigantry program,
and cross refrencing it to the original data it was created from. 
"""

import os
#import numpy as np
#import matplotlib.pyplot as plt

#Main() Checks to See what type of script you would Like to generate
def main():
    path = os.getcwd();
    path = path.replace('Script Readers','')
    OpenFile = path + 'Scripts\\' + '38.xml'
    print(OpenFile);
    
    #OpenFile = 'Scripts\87.txt';
    ImportF = open(OpenFile);
    
    lines = ImportF.readlines();
    CleanLines = [];
    for line in lines:
        if line[0:10] == "  <Command":
            #print(line[0:60]);
            reline = line;
            if line[23] == '"':
                reline = (line[0:22] + "00" + line[22:-1])
            elif line[24] == '"':
                reline = (line[0:22] + "0" + line[22:-1])
            else: 
                reline = line;
            CleanLines.append(reline[21:-1])
    
    #print(CleanLines[6][16:28])
    #print(CleanLines);
    
    lineno = 0; dots = []; dotno = 0
    for line in CleanLines:
        #print(line[16:40])
        if lineno == 0:
            lastline = line;
        else:
            #if line[16:28] == "Dispense_Dot" and line[36] == "1":
            numbs = (line[37:-1].split(','))
            if line[16:28] == "Dispense_Dot":    
                #print("this says dispense dot: ")
                #print()
                dots.append([lastline[1:4], dotno, numbs[0], numbs[1], numbs[2]])
                dotno = dotno + 1;
            lastline = line;
        lineno = lineno + 1;
    
    eventno = 0;
    for line in dots:
        #print("IO on Event:" , line);
        eventno = eventno + 1;
        
    for line in dots:
        print(line);
    #print(dots)
    
    writefile =  open("OUTPUT1.txt", "w");
    for line in dots:
        print(line);
        l = [];
        for data in line:
            templ = str(data);
            l.append(templ)
        writefile.write(l[2].replace('"','').replace('"','')  + "\t" + l[3] + '\n');
        #writefile.write(l[0] + "\t" + l[1] + "\t" + l[2] + "\t" + l[3] + "\t" + l[4] + "\t" + l[5] + "\t" + l[6] + "\t" + l[7] + "\n");
    writefile.close();

    
main();