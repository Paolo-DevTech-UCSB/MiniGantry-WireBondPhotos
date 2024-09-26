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
import numpy as np
import matplotlib.pyplot as plt

#Main() Checks to See what type of script you would Like to generate
def main():
    CodexName = 'Codex\HD_Full_Codex.txt'
    CoImport = open(CodexName);
    lines = CoImport.readlines();
    Codex = []; CodexLine = [];
    for line in lines:
        PreCodex = line.split('\t');
        for data in PreCodex:
            ndata = data.replace("\n","")
            CodexLine.append(ndata)
        Codex.append(CodexLine)
        #print("Feature:" , CodexLine)
        CodexLine = [];
        
    TranslatedCodex = [];
    #xoff = 108; yoff = 232;
    for L in Codex:
        x = float(L[3]); y = float(L[2]);
        if (x*-1 + 376.82) > -100:
            if (y + 154) < 400:
                TranslatedCodex.append([L[0], float(L[1])+107.92,((float(L[2])*-1))+388.9,L[3],L[4],L[5]])
                #TranslatedCodex.append([L[0],L[1],(float(L[2])+xoff),(float(L[3])*1) + yoff,L[4],L[5]])
    #for line in TranslatedCodex:
        #print("Feature: " , line);
        
    OpenFile = 'Scripts\87.txt';
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
    
    lineno = 0; dots = []; dotno = 0
    for line in CleanLines:
        #print(line[16:40])
        if lineno == 0:
            lastline = line;
        else:
            if line[16:22] == "Set_IO" and line[36] == "1":
                numbs = (lastline[37:-1].split(','))
                dots.append([lastline[1:4], dotno, numbs[0], numbs[1], numbs[2]])
                dotno = dotno + 1;
            lastline = line;
        lineno = lineno + 1;
    
    eventno = 0;
    for line in dots:
        #print("IO on Event:" , line);
        eventno = eventno + 1;
    
        
    #THE POINT OF THIS IS TO MATCH 100% OF THE IO ON EVENTS TO CELLS
    matches = 0; matchlist = [];
    for event in dots:
        x = event[2];
        y = event[3];
        for feature in TranslatedCodex:
            if int(round(float(x))) == int(round(float(feature[1]))):
                if int(round(float(y))) == int(round(float(feature[2]))):
                    
                    #print(event[2], "=", feature[1], "& ", event[3], "=", feature[2])
                    #feature is from the codex, event is from the program
                    matches = matches + 1;
                    matchlist.append([event[1], event[0], feature[0], round(feature[1],2), round(feature[2],2), feature[3] ,feature[4], feature[5]])
                    ## Program Order No, 
    #Cells and Point Number Have Been Mapped to Coordinates 
    # now to extract the order from an "xml" txt file
    print(matches, "/", eventno, " Matched")
    
    
    """largeX = 0; largeY = 0;
    for line in TranslatedCodex:
        if largeX < float(line[1]):
            largeX = float(line[1]);
        if largeY < float(line[2]):
            largeY = float(line[2]);
    print("From Cells vs Points: ", largeX, largeY)
    #    print(line[1],"\t", line[2])
    #print("-_________________")
    for line in dots:
        if largeX < float(line[2]):
            largeX = float(line[2]);
        if largeY < float(line[3]):
            largeY = float(line[3]);
    print("From Programs: ", largeX, largeY)"""
    #    print(line[2],"\t", line[3])
    
    writefile =  open("decode.txt", "w");
    for thing in matchlist:
        print(thing);
        l = [];
        for data in thing:
            templ = str(data);
            l.append(templ)
        writefile.write(l[0] + "\t" + l[1] + "\t" + l[2] + "\t" + l[3] + "\t" + l[4] + "\t" + l[5] + "\t" + l[6] + "\t" + l[7] + "\n");
    writefile.close();
        
    
    
    #saveplot(TranslatedCodex, dots)
    #minigantryscript(OpenFile, TransCodex);
def saveplot(Codex, dots):
    color = []
    x = []
    y = []
    for line in Codex:
        x.append(line[1])
        y.append(line[2])
        color.append('blue')
    plt.scatter(x, y, color = 'blue')    
    ####blue is codex, from a custom list
    
    
    for line in dots:
        x.append(line[2])
        y.append(line[3])
        color.append('orange')
        #print(line[1], line[2])
        #np.append(x,float(line[1]))
        #np.append(y,float(line[2]))
    ####Orange is from the program pulled off the gantry, dots
    #print(x, y)
    #print(len(color), len(x), len(y))
    plt.axis([50, 275, 220, 400])
    plt.scatter(x, y, color = 'orange', s = 2)
    plt.show()
    
    
    
    
    
    """plt.axis('equal')
    Features = []; dotlist = []; FX = []; FY = []; DX = []; DY = [];
    for line in Codex:
        Features.append([line[1], line[2]])
        FX.append(float(line[1]))
        FY.append(float(line[2]))
        
    for line in dots:
        dotlist.append([line[2],line[3]])
        DX.append(line[2])
        DY.append(line[3])
        
    #print(Features, dotlist)
    plt.scatter(FX,FY)
    plt.scatter(DX,DY)"""
    
main();