# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:33:21 2023

@author: hep
"""

import os
import numpy as np

#Main() Checks to See what type of script you would Like to generate
def main():
    #OpenFile = input("Open What File: ")
    OpenFile = 'LD5input.txt';
    #OutputFormat = 'mini';
    minigantryscript(OpenFile);
    

#this will write mini gantry script (leave be)
def minigantryscript(OpenFile):
    importF = open(OpenFile);
    flines = importF.readlines();
    x = len(flines); 
    z = 0; z2 = 1;
    total = 0; p = 0; u = 0;
    
    writefile =  open("LD5output.txt", "w");
    #writefile.write("----first line----")

    for line in flines:

        #print(line)
        templ = line.split('\t');
        #print(templ)
        mat = np.empty((8,x), dtype = float)
        #print(mat)
        #print('row:'+ str(z+1))
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
                mat[n,z] = templ[n];  #print(mat[:,z]);"""
        p1xi = mat[4,z];  p1yi = mat[5,z]; beegh = mat[0,z]; p2xi = mat[6,z];  p2yi = mat[7,z]; 
        #p1xi = templ[2];  p1yi = templ[3]; beegh = templ[0];
        #print(mat)
        #print(str((p1xi)) + "," + str((p1yi)));
        
        if beegh == 1:
            #print('  <CommandInfo Index="'+ str(z2) + '" Function="Point_Dispense_Setup" Values="1.1,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />');
            writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Point_Dispense_Setup" Values="1.1,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            
            z2 = z2 + 1;
            u = u + 1;
        #elif beegh != 0:
        #    print('error in getting dispense size'); 
        if z2 == 1:
            #print('<?xml version="1.0" encoding="utf-8"?>');
            writefile.write('<?xml version="1.0" encoding="utf-8"?>\n')
            #print('<DTRobot>');
            writefile.write('<DTRobot>\n')
            #print('<ProgramParameterInfo ProgramNumber="83" ProgramName="DummyBoard" XYMoveSpeed="350" ZMoveSpeed="120" DeBugSpeed="10" BackHome="False" SoftX="0" SoftY="0" SoftZ="0" SoftU="0" SoftV="0" SoftW="0" AdjustX="0" AdjustY="0" AdjustZ="0" AutoPurgeTime="0" AutoPurgeWaitTime="0" TempCommand1="0" TempCommand2="0" TempX1="0" TempY1="0" TempZ1="0" TempX2="0" TempY2="0" TempZ2="0" ZLimit="100" EMG="False" Quickstep="False" QuickstepType="Normal" DefaultLIO="0" Password="" Lock="False" Beep="True" DisplayRunCount="True" DefineRunCount="0" RunCount="0" PausePosition="Stand" RunnProgramNumbers="83" IsRecordPick="True" PickIndex="1" StepsIndex="" IsRecordStep="False" TipFinderType="1" TipFinderLoop="1" TipFinderAction="2" TipFinderCenterX="0" TipFinderCenterY="0" TipFinderCenterZ="0" TipFinderStandardX="0" TipFinderStandardY="0" TipFinderStandardZ="0" />');
            writefile.write('<ProgramParameterInfo ProgramNumber="83" ProgramName="DummyBoard" XYMoveSpeed="350" ZMoveSpeed="120" DeBugSpeed="10" BackHome="False" SoftX="0" SoftY="0" SoftZ="0" SoftU="0" SoftV="0" SoftW="0" AdjustX="0" AdjustY="0" AdjustZ="0" AutoPurgeTime="0" AutoPurgeWaitTime="0" TempCommand1="0" TempCommand2="0" TempX1="0" TempY1="0" TempZ1="0" TempX2="0" TempY2="0" TempZ2="0" ZLimit="100" EMG="False" Quickstep="False" QuickstepType="Normal" DefaultLIO="0" Password="" Lock="False" Beep="True" DisplayRunCount="True" DefineRunCount="0" RunCount="0" PausePosition="Stand" RunnProgramNumbers="83" IsRecordPick="True" PickIndex="1" StepsIndex="" IsRecordStep="False" TipFinderType="1" TipFinderLoop="1" TipFinderAction="2" TipFinderCenterX="0" TipFinderCenterY="0" TipFinderCenterZ="0" TipFinderStandardX="0" TipFinderStandardY="0" TipFinderStandardZ="0" />\n')
            #print('  <CommandInfo Index="1" Function="Line_Speed" Values="45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />');
            writefile.write('  <CommandInfo Index="1" Function="Line_Speed" Values="45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #print('  <CommandInfo Index="2" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />')
            writefile.write('  <CommandInfo Index="2" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #print('  <CommandInfo Index="3" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />');
            writefile.write('  <CommandInfo Index="3" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #print('  <CommandInfo Index="4" Function="Dispense_End_Setup" Values="15,20,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />') 
            writefile.write('  <CommandInfo Index="5" Function="Z_Clearance" Values="1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            z2 = 6;
            u = 5;
        
        #
        #print('  <CommandInfo Index="'+ str(z2) + '" Function="Dispense_Dot" Values="' + str((p1xi)) + "," + str((p1yi)) + ","+ "45.24" + ',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />')
        yvalue = str(p1yi).replace('\n','')
        #print(p1yi, yvalue)
        writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Dispense_Dot" Values="' + str((p1xi)) + "," + str((yvalue)) + ", 45.24" + ',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
        p = p + 1; #z2 = z
        #z2 = z2 + 1;

        if beegh == 1:
            #print('  <CommandInfo Index="'+ str(z2) + '" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />');
            writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            u = u + 1;
      
        #print("in graphics terms: " + str(p1xi) + "," + str(p1yi) + " to "+ str(p2xi) + "," + str(p2yi) );    
        z = z + 1;
        z2 = z2 + 1;
    #print('  <CommandInfo Index="'+ str(z2) + '" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />'); z2 = z2 + 1;
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    #print('  <CommandInfo Index="'+ str(z2) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />'); z2 = z2 + 1;
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    #print('  <CommandInfo Index="'+ str(z2) + '" Function="End_Program" Values="-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />'); z2 = z2 + 1;
    writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="End_Program" Values="-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n'); z2 = z2 + 1;
    #print('<DTRobot>\n');
    writefile.write('<DTRobot>\n');
    u = u + 3;
    #print(total);
    writefile.close();
   
main()