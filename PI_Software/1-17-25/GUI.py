import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk

import vlc

import time

import pyautogui
import subprocess

import os
import RPi.GPIO as GPIO

from PIL import Image, ImageTk


def start_vlc(*args):
    #StatusEntry.delete(0,END)
    #StatusEntry.insert(0, "starting VLC")
    print("Thread:1  Start")
    #Controls for VLC
    #media_player = vlc.MediaPlayer()
    #media = vlc.Media("v4l2://")
    #media_player.set_media(media)
    #media_player.play()
    #media_player.toggle_fullscreen()
    #media_player.toggle_fullscreen()
    #media_player.video_set_scale(2)

    time.sleep(1)
    #windowmove()    
    
    shape = ShapeEntry.get()
    seconds = shapetimeindx(shape)
    time.sleep(100000)
    
    StatusEntry.delete(0, END)
    StatusEntry.insert(0, "closing VLC")
    
    #media_player.stop()
    
    StatusEntry.delete(0, END)
    StatusEntry.insert(0, "Idle")
    
def windowmove():
    pyautogui.moveTo(100,10)
    pyautogui.click()
    
    time.sleep(0.5)
    pyautogui.dragTo(100,100,duration=1)
    pyautogui.moveTo(300,300)
    pyautogui.dragRel(500,400, duration  =1)
    
def Sub(*args):
    modname = NameEntry.get()
    informat = True;
    print(len(modname));
    if len(modname) < 12 or len(modname) > 15:
        informat = False;
        print("#1")
    else:
        if modname[0] != "M" and modname[0] != "m":
            informat = False;
            print("#2")
    
    if informat == False:  #if in-format is true the function is fine
        StatusEntry.delete(0,END)
        StatusEntry.insert(0, "Naming Error");
    else:
        ModNameEntry.delete(0, END)
        ModNameEntry.insert(0, modname)
                
        ModShape = resindx(modname[1]) + " " + shapeindx(modname[2]);
        
        ShapeEntry.delete(0, END)
        ShapeEntry.insert(0, ModShape)
        
        StatusEntry.delete(0,END)
        StatusEntry.insert(0, "opening VLC")
        
        sub = threading.Thread(target = start_vlc)
        sub.daemon = True;
        sub.start()
        
        #StatusEntry.delete(0, END)
        #StatusEntry.insert(0, "VLC idle")
        
            
        #StatusEntry.delete(0, END)
        #StatusEntry.insert(0, "Initializing... ")
        countersub = threading.Thread(target = init)
        countersub.daemon = True;
        countersub.start()
    


def Cells(length, Array):
    """for photo in range(length):
        source = "home/pi/Desktop/WireBondPhotos/photo" + str(photo) + ".png";
        cells1 = Array[photo][5]; cells2 = Array[photo][6]; cells3 = Array[photo][7];
        named = "Hole_" + str(photo) + "_Cells_" + str(cells1) + "_" + str(cells2) + "_" + str(cells3);
        #named = "Hole_"+ photo +"_Cells_"+cells1+"_"+cells2+"_"+cells3;
                
        dest = '/home/pi/Desktop/WireBondPhotos/'+str(named)+'.png';
        os.rename(source,dest)"""
        
    #for photo in range(length):
    photo = 0; notdone = True;
    while notdone == True:
        if Array[photo][5] == 'notch':
            notdone = False;
        source = "/home/hep/Desktop/WireBondPhotos/photo" + str(photo) + ".png";
        cell1 = Array[photo][5];
        cell2 = Array[photo][6];
        cell3 = Array[photo][7];
        named = str(cell1) + "_" + str(cell2) + "_" + str(cell3) + ".png";
        #dest = "/home/hep/Desktop/WireBondPhotos/" + named + ".png"
        dest_directory = '/home/hep/Pictures/'
        dest = os.path.join(dest_directory, named)
        print("Destination:", dest)
        try:
            os.rename(source, dest)
            print("Photo Moved")
        except FileNotFoundError as e:
            print(f'Error: {e}')
        except PermisssionErrror as e:
            print(f'permission error: {e}')
        photo = photo + 1;
        
    print('Done Moving Photos')

"""def Photos():
    GPIO.setup(26, GPIO.OUT)
    GPIO.setmode(GPIO.BCM)
    PhoNum = 331;  PCount = 0; Chk1 = False; Chk2 = False;
    while PCount < 331:
        time.sleep(0.2)
        state = GPIO.input(26);
        if state: Chk1 = True; 
        else: Chk2 = True; Chk1 = False;
        if Chk1 and Chk2:
            print("take a photo, Number:" + str(PCount));
            #StatusEntry.delete(0, END)
            StatusEntry.insert(0, "Running Photos..." + str(PCount))
            
            #HoleNumEntry.delete(0, END)
            HoleNumEntry.insert(0, "Hole No." + str(PCount))
            
            #CellsEntry.delete(0, END)
            CellsEntry.insert(0, "The cells next to Hole No." + str(PCount))
            
            time. sleep(1.6)
            os.system('scrot -u /home/pi/Desktop/WireBondPhotos/photo'+str(PCount)+'.png')
            Chk1 = False; Chk2 = False;
            PCount += 1;
    Cells(PCount);"""
    
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    print("Starting Captures");
    
    StatusEntry.delete(0, END)
    StatusEntry.insert(0, "Waiting for Initialization... ")
    
    if ShapeEntry.get() == "HD Full":
        openfile = 'HD_Index.txt'
        StatusEntry.delete(0, END)
        StatusEntry.insert(0, "Please Start Mini-Gantry Program #87")
        
        
    elif ShapeEntry.get() == "LD Right":
        openfile = 'LD_Right_Index.txt'
        StatusEntry.delete(0, END)
        StatusEntry.insert(0, "Please Start Mini-Gantry Program #72")
        NameEntry.delete(0, END)
        NameEntry.insert(0, "MLR1CX-SB###")
        
    elif ShapeEntry.get() == "LD Five":
        openfile = 'LD_Five_Index.txt'
        StatusEntry.delete(0, END)
        StatusEntry.insert(0, "Please Start Mini-Gantry Program #73")
        NameEntry.delete(0, END)
        NameEntry.insert(0, "ML51CX-SB###")
        
    elif ShapeEntry.get() == "LD Full":
        openfile = 'LD_Full_Index.txt'
        StatusEntry.delete(0, END)
        StatusEntry.insert(0, "Please Start Mini-Gantry Program #90")
        NameEntry.delete(0, END)
        NameEntry.insert(0, "MLF1CX-SB###")    
        

        
        
    else:
        openfile = '';
        
    cimp = open(openfile);
    lines = cimp.readlines();
    Array = []; Aline = [];
    for line in lines:
        pline = line.split('\t')
        for data in pline:
            ndata = data.replace("\n","")
            Aline.append(ndata)
        Array.append(Aline)
        Aline = [];
    
    endprocess = False; counter = 0; LastState = True;
    state = False;  contin = False;
    while endprocess == False:
        LastState = state;
        state = GPIO.input(26);
        if LastState != state:
            counter = 0;
            print("reset");
        if state: counter += 1;
        if counter >= 5:
            endprocess = True;
            print("initialized")
            StatusEntry.delete(0, END)
            StatusEntry.insert(0, "Initialization Compelete.")
            
            contin = True; 
        time.sleep(2)
    #GPIO.cleanup()
    if contin:
        PhoNum = 331;  PCount = 0; Chk1 = False; Chk2 = False; idlecycles = 0; tot = 0;
        while PCount < 331:
            time.sleep(0.1)
            state = GPIO.input(26);
            print(state);
            if state == 1:
                #first_on = False;
                #while first_on == False:
                #    state = GPIO.input(26); 
                #    if state == 1:
                #        first_on == True;
                    
                    
                print('startpic')
                print(PCount)
                #print("take a photo, Number:" + str(PCount));
                StatusEntry.delete(0, END)
                StatusEntry.insert(0, "Running Photos...")
            
                HoleNumEntry.delete(0, END)
                HoleNumEntry.insert(0, "Hole No." + str(PCount) + "  PrgLine:" + Array[PCount][1])
                
                #print(Array[PCount])
                
                
                CellsEntry.delete(0, END)
                CellsEntry.insert(0, Array[PCount][5:8])  ##BUGFIX 1
                
                time. sleep(1.5) ###CHAGED TO SEE EFFECT WAS 1.6
                #os.system('gnome-screenshot -f /home/hep/Desktop/WireBondPhotos/photo'+str(PCount)+'.png')
                #screenshot = pyautogui.screenshot()
                save_location = ' /home/hep/Desktop/WireBondPhotos/'
                filename = 'photo'+str(PCount)+'.png'
                filepath = save_location + filename;
                tot = tot + 1;
                idlecycles = 0;
                
                cmd = str('grim' + filepath)
                os.system(cmd)
                print('taken')
                
                while state == 1:
                    state = GPIO.input(26)
                    if state == 0:
                        break
                    else: #print(state)
                        time.sleep(0.1);
                #print(cmd)
                #subprocess.run[(cmd)]
                
                #screenshot.save('/home/hep/Desktop/WireBondPhotos/photo'+str(PCount)+'.png')
                #pyautogui.press('alt','printscreen')
                #Chk1 = False; Chk2 = False;
                PCount += 1;
                #idlecycles = 0;
                #donezo = False;
                #while donezo == False:
                #    state = GPIO.input(26);
                #    if state == 0:
                #        time.sleep(0.05)
                #        donezo = True;
                #    else: donezo = True;
                #    
                #    print('finished loop')
                
            else:
                idlecycles = idlecycles + 1;
                if idlecycles == 50 or idlecycles == 25:
                    print(f'idle cycles: {idlecycles}')
            if idlecycles >= 300:
                PCount = 100000;

        Cells(tot, Array);
        #Turned OFF WHILE FIXING SCROT
        
        CellsEntry.delete(0, END);
        HoleNumEntry.delete(0, END);
        StatusEntry.delete(0, END);
        StatusEntry.insert(0, "Finished...")
        

def shapeindx(letter):
    if letter == "R" or letter == "r":
        shape = "Right"
    elif letter == "F" or letter == "f":
        shape = "Full"
    elif letter == "T" or letter == "t":
        shape = "Top"
    elif letter == "B" or letter == "b":
        shape = "Bottom"
    elif letter == "L" or letter == "l":
        shape = "Left"
    elif letter == "5":
        shape = "Five"
    return shape;

def resindx(letter):
    if letter == "H" or letter == "h":
        shape = "HD"
    elif letter == "L" or letter == "l":
        shape = "LD"
    return shape

def shapetimeindx(shape):
    if shape == "LD Right":
        sec = 800;
    elif shape == "HD Full":
        sec = 1000;
    else:
        sec = 1;
    return time;

def setRIGHTPARTIAL():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Right")
    NameEntry.delete(0, END)
    NameEntry.insert(0, "MLR3CX-SB###")
    
def setFIVEPARTIAL():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Five")
    NameEntry.delete(0, END)
    NameEntry.insert(0, "ML53CX-SB###")
    
def setLEFTPARTIAL():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Left")
    
def setTOPPARTIAL():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Top")
    
def setBOTTOMPARTIAL():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Bottom")
    
def setFULLLD():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "LD Full")
    NameEntry.delete(0, END)
    NameEntry.insert(0, "MLF1CX-SB###")
        
def setTOPHD():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "HD TOP")
    
def setFULLHD():
    ShapeEntry.delete(0, END)
    ShapeEntry.insert(0, "HD Full")
    NameEntry.delete(0, END)
    NameEntry.insert(0, "MHF1CX-SB###")
    

window = tk.Tk()
window.title("WB Photos")
window.minsize(width=500, height=150)
window.geometry("1600x1150")


Upps = tk.Frame(padx = 535, pady = 20, bg = "#013660")
UR1 = tk.Frame(padx = 25)
MidR = tk.Frame()
Mids = tk.Frame()

#
#tk.Frame.__init__(self, parent)
vlc_frame = tk.Frame(window, width=1600, height = 900)
#vlc_frame.grid(row=4, column=1)


# Create VLC player instance
Instance = vlc.Instance()
player = Instance.media_player_new()

# Set the media to play (replace with your media stream URL)
media = Instance.media_new("v4l2://")
player.set_media(media)

def set_window_id():
    player.set_xwindow(vlc_frame.winfo_id())
    player.play()

# Play the media
#player.play()
window.after(100, set_window_id)

label = tk.Label(UR1, text="Wirebond Photos Jan 2025").grid(column=1, row=6, sticky=W)
label = tk.Label(UR1, text="Author: Paolo Jordano").grid(column=1, row=7, sticky=W)
tk.Button(UR1, text="Basic Start", command=Sub).grid(column=1, row=5, sticky=W)
#separator = tk.Canvas(Upps, width = 10, height = 80, bg='darkblue')
#separator.grid(row=0, column=0, padx=10, pady=10)

HoleNumEntry = tk.Entry(UR1, width = 35)
HoleNumEntry.grid(row = 1, column =1)
CellsEntry = tk.Entry(UR1, width = 35)
CellsEntry.grid(row = 2, column =1)
ModNameEntry = tk.Entry(UR1, width = 35)
ModNameEntry.grid(row = 3, column =1)
ShapeEntry = tk.Entry(UR1, width = 35)
ShapeEntry.grid(row = 4, column =1)

StatusLabel = tk.Label(MidR, text= "Status:").grid(row = 1, column =1)
StatusEntry = tk.Entry(MidR, width = 35)
StatusEntry.grid(row = 2, column =1)



SettingsLabel = tk.Label(Mids, text= "Settings:").grid(row = 1, column =1)
NameLabel = tk.Label(Mids, text= "Input Name:").grid(row = 2, column = 1)
NameEntry = tk.Entry(Mids, width = 35)
NameEntry.grid(row = 2, column = 2)
tk.Button(Mids, text="LD Right", command=setRIGHTPARTIAL).grid(row = 1, column =5)
tk.Button(Mids, text="LD Five", command=setFIVEPARTIAL).grid(row = 1, column =3)
tk.Button(Mids, text="HD Full", command=setFULLHD).grid(row = 1, column =4)
tk.Button(Mids, text="LD Left", command=setLEFTPARTIAL).grid(row = 1, column =6)
tk.Button(Mids, text="LD Top", command=setTOPPARTIAL).grid(row = 1, column =7)
tk.Button(Mids, text="LD Bottom", command=setBOTTOMPARTIAL).grid(row = 1, column =8)
tk.Button(Mids, text="HD Top", command=setTOPHD).grid(row = 1, column =9)
tk.Button(Mids, text="LD Full", command=setFULLLD).grid(row = 1, column =10)

image_frame = tk.Frame(window, bg = '#013660')
image_frame2 = tk.Frame(window, bg = '#013660')

imagepath = "/home/hep/Desktop/SMALLERCERN.png"
imagepath2 = "/home/hep/Desktop/SMALLERucsb.png"

image = Image.open(imagepath)
image2 = Image.open(imagepath2)

resized_image = image.resize((150, 150))
resized_image2 = image2.resize((375, 150))

photo = ImageTk.PhotoImage(resized_image)
photo2 = ImageTk.PhotoImage(resized_image2)

image_label = tk.Label(Upps, image=photo)
image_label.image = photo
#image_label.grid(column=2, row=1, sticky=W)
image_label.grid(column=4, row=1, sticky=W)

image_label2 = tk.Label(Upps, image=photo2)
image_label2.image = photo2
#image_label2.grid(column=2, row=1, sticky=W)
image_label2.grid(column=5, row=1, sticky=W)


#image_frame.grid(column=3, row=1, sticky=W)
#image_frame2.grid(column=3, row=1, sticky=W)

Upps.grid(column=1, row=1, sticky=W)

image_frame.grid(column=1, row=2, sticky=W)

UR1.grid(column=1, row=1, sticky=W)
MidR.grid(column=1, row=2, sticky=W)
Mids.grid(column=1, row=3, sticky=W)

vlc_frame.grid(column=1, row=4, sticky=W)

StatusEntry.insert(0, "Idle")
NameEntry.insert(0, "MHF1CX-SB0001")

window.mainloop()