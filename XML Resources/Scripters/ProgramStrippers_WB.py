# -*- coding: utf-8 -*-
"""
THIS CODE WAS CREATED TO FACILITATE REMOVAL OF COORDINATE INFORMATION FROM A MINIGANTRY PROGRAM
WILL EXPORT TO Input.txt 
"""

import os
import numpy as np

def main():
    path = os.getcwd();
    path = path.replace('Scripters','')
    OpenFile = path + '\\\XML Resources\\Scripters\\' + 'CurrentXML.txt'
    print(OpenFile);
    #OpenFile = 'Script Readers\\CurrentXML.txt';
    minigantryscript(OpenFile);

def minigantryscript(OpenFile):

    importF = open(OpenFile); LineList = []; 
    flines = importF.readlines();
    for line in flines:
        if 'Dummy_Point' in line:
            print(line)
            templine = line;
            templine = templine.replace('<CommandInfo Index="','')
            templine = templine.replace('" Function="Dummy_Point" Values="',',')
            templine = templine.replace(',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>','')
            templine = templine.replace("\n","")
            print(templine)
            linearray = templine.split(",")
            LineList.append(linearray)
            #print(linearray) 

        #print(line)
    #print(LineList)
    path = os.getcwd();
    path = path.replace('Scripters','')
    writeFilePath = path + '\\XML Resources\\Scripters\\' + 'Input.txt'
    writefile =  open(writeFilePath, "w");    

    for Array in LineList: 
        #print(Array[1] + "\t" + Array[2]+ "\n")
        print(Array[0] + ",")
        writefile.write(Array[1] + "\t" + Array[2]+ "\n")
        #writefile.write(Array[0] + "\t" + Array[1] + "\t" + Array[2] + "\t" + Array[3]+ "\n")
 
main()