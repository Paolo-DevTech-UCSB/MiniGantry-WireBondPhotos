# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:33:21 2023

@author: hep
"""

import os
import numpy as np

def main():
    OpenFile = 'AletheasLD5.txt';
    minigantryscript(OpenFile);
    
##dont forget to edit in the initialization manually, or code it


#this will write mini gantry script (leave be)
def minigantryscript(OpenFile):
    importF = open(OpenFile);
    flines = importF.readlines();
    #x = len(flines); 
    z = 0; z2 = 1;
    total = 0; p = 0; u = 0;
    
    writefile =  open("programoutput.txt", "w");

    for line in flines:

        templ = line.split('\t');
        #print(templ);
        p1xi = templ[0];  p1yi = templ[1]; #beegh = templ[0];
        if z2 == 1:
            writefile.write('<?xml version="1.0" encoding="utf-8"?>\n')
            writefile.write('<DTRobot>\n');
            writefile.write('<ProgramParameterInfo ProgramNumber="87" ProgramName="WBPhotosV01" XYMoveSpeed="350" ZMoveSpeed="120" DeBugSpeed="10" BackHome="False" SoftX="0" SoftY="0" SoftZ="0" SoftU="0" SoftV="0" SoftW="0" AdjustX="0" AdjustY="0" AdjustZ="0" AutoPurgeTime="0" AutoPurgeWaitTime="0" TempCommand1="0" TempCommand2="0" TempX1="0" TempY1="0" TempZ1="0" TempX2="0" TempY2="0" TempZ2="0" ZLimit="100" EMG="False" Quickstep="False" QuickstepType="Normal" DefaultLIO="0" Password="" Lock="False" Beep="True" DisplayRunCount="True" DefineRunCount="0" RunCount="0" PausePosition="Stand" RunnProgramNumbers="87" IsRecordPick="True" PickIndex="1" StepsIndex="" IsRecordStep="False" TipFinderType="1" TipFinderLoop="1" TipFinderAction="2" TipFinderCenterX="0" TipFinderCenterY="0" TipFinderCenterZ="0" TipFinderStandardX="0" TipFinderStandardY="0" TipFinderStandardZ="0" />\n')
            writefile.write('  <CommandInfo Index="1" Function="Line_Speed" Values="45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="2" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="3" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="4" Function="Dispense_End_Setup" Values="15,20,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="5" Function="Z_Clearance" Values="1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="6" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="7" Function="Wait_Point" Values="10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
            z2 = 8;
            u = 7;
        yvalue = p1yi.replace('\n','')
        xvalue = p1xi;
        #print(xvalue, ",", yvalue)
        xoffset = -0.36;
        yoffset = -0.46;
        XWithOff = float(xvalue) + yoffset;
        YWithOff = float(yvalue) + xoffset;
        #print("this is xvalue's type: " , type(xvalue));
        ######################## OFFSETS 
        ####yvalue = yvalue*-1;    yvalue = yvalue + 388.89;     xvalue = xvalue + 107.92;
        
        
        
        writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Dummy_Point" Values="' + str((XWithOff)) + "," + str((YWithOff)) + ",40.51" + ',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+1) + '" Function="Set_IO" Values="2,8,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+2) + '" Function="Wait_Point" Values="2,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+3) + '" Function="Set_IO" Values="2,8,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>"""\n')
        #print("og coords: " + str((p1xi)) + " , " + str((yvalue)))
        p = p + 1;
        z = z + 1;
        u = u + 4;
        z2 = z2 + 4;
    
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="End_Program" Values="-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    writefile.write('</DTRobot>\n');
    u = u + 3;
    print("lines:", u)
    print("offsets aren't done in this program!!\n  adjustments are!")
    print("output in text file in folder")
    writefile.close();
   
main()