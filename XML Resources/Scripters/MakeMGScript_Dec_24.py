
import os
import numpy as np

def main():
    path = os.getcwd();
    #path = path.replace('Scripters','')
    #OpenFile = path + 'Script Readers\\' + 'OUTPUT1.txt'
    #print(OpenFile);
    OpenFile = 'XML Resources\Scripters\Input.txt';
    minigantryscript(OpenFile);
    
##dont forget to edit in the initialization manually, or code it


#this will write mini gantry script (leave be)
def minigantryscript(OpenFile):
    importF = open(OpenFile);
    flines = importF.readlines();
    #x = len(flines); 
    z = 0; z2 = 1;
    total = 0; p = 0; u = 0;
    LineList = []
    for line in flines:
        
        linetemp = line.replace("\n","")
        linearray = linetemp.split("\t")
        LineList.append(linearray)
        print(line)
    
    path = os.getcwd();
    path = path.replace('Scripters','')
    writeFilePath = path + '\\XML Resources\\Scripters\\' + 'Output.txt'
    writefile =  open(writeFilePath, "w");

    for array in LineList:

        #templ = line.split('\t');
        templ = array;
        #print(templ);
        p1xi = templ[0];  p1yi = templ[1]; #beegh = templ[0];
        if z2 == 1:
            writefile.write('<?xml version="1.0" encoding="utf-8"?>\n')
            writefile.write('<DTRobot>\n');
            writefile.write('<ProgramParameterInfo ProgramNumber="87" ProgramName="WBPhotosV01" XYMoveSpeed="350" ZMoveSpeed="120" DeBugSpeed="10" BackHome="False" SoftX="0" SoftY="0" SoftZ="0" SoftU="0" SoftV="0" SoftW="0" AdjustX="0" AdjustY="0" AdjustZ="0" AutoPurgeTime="0" AutoPurgeWaitTime="0" TempCommand1="0" TempCommand2="0" TempX1="0" TempY1="0" TempZ1="0" TempX2="0" TempY2="0" TempZ2="0" ZLimit="100" EMG="False" Quickstep="False" QuickstepType="Normal" DefaultLIO="0" Password="" Lock="False" Beep="True" DisplayRunCount="True" DefineRunCount="0" RunCount="0" PausePosition="Stand" RunnProgramNumbers="87" IsRecordPick="True" PickIndex="1" StepsIndex="" IsRecordStep="False" TipFinderType="1" TipFinderLoop="1" TipFinderAction="2" TipFinderCenterX="0" TipFinderCenterY="0" TipFinderCenterZ="0" TipFinderStandardX="0" TipFinderStandardY="0" TipFinderStandardZ="0" />\n')
            writefile.write('  <CommandInfo Index="1" Function="Line_Speed" Values="45,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #writefile.write('  <CommandInfo Index="2" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="2" Function="Point_Dispense_Setup" Values="0.9,0.4,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="3" Function="Dispense_End_Setup" Values="15,20,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            writefile.write('  <CommandInfo Index="4" Function="Z_Clearance" Values="1,15,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #writefile.write('  <CommandInfo Index="6" Function="Dummy_Point" Values="194.27,0.2,0.72,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
            #writefile.write('  <CommandInfo Index="7" Function="Wait_Point" Values="10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
            z2 = 5;
            u = 4;
        yvalue = p1yi.replace('\n','')
        xvalue = p1xi;
        #print(xvalue, ",", yvalue)
        #xoffset = -0.36;
        #yoffset = -0.46;
        #XWithOff = float(xvalue) + yoffset;
        #YWithOff = float(yvalue) + xoffset;
        #print("this is xvalue's type: " , type(xvalue));
        ######################## OFFSETS 
        ####yvalue = yvalue*-1;    yvalue = yvalue + 388.89;     xvalue = xvalue + 107.92;
        
        
        
        writefile.write('  <CommandInfo Index="'+ str(z2) + '" Function="Dummy_Point" Values="' + str((p1xi)) + "," + str((p1yi)) + ",40.51" + ',-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues="" />\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+1) + '" Function="Wait_Point" Values="3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+2) + '" Function="Set_IO" Values="2,8,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+3) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+4) + '" Function="Set_IO" Values="2,8,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>"""\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+5) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+6) + '" Function="Set_IO" Values="2,8,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+7) + '" Function="Wait_Point" Values="1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        writefile.write('  <CommandInfo Index="'+ str(z2+8) + '" Function="Set_IO" Values="2,8,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1" TempValues=""/>\n')
        
        p = p + 1;
        z = z + 1;
        u = u + 9;
        z2 = z2 + 9;
    
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