#READ THIS DOCUMENT TO SETUP WIREBOND PHOTOS ON THE MINIGANTRY

#1 Materials: Mini Gantry, Rasberry Pi, Solid State Relay, USB Microscope, Microscope Arm for the Minigantry (3D Printable)(Made in Steel at UCSB), Mouse, Keyboard, Monitor, D-Sub Connector
  # USB MICROSOPE: https://www.amazon.com/dp/B07DQM237K?ref=fed_asin_title
  # Solid State Replay: https://www.amazon.com/dp/B00B888WVC?ref=fed_asin_title
  # Rasberry Pi (3 or Higher) (With Rasbian)
  # Microscope Arm for Mini Gantry (Email, Susanne or Paolo from UCSB for STL or CAD file)
  # 25 Pin D-Sub Connector (male) (makes it easier to remove setup from minigantry) (bought at UCSB Physics's lab supply room)
  # MicroSD Card Reader: For getting a fresh install of rasbian
  
#2 How to build (Hardware):
  # -1- Set Up your RasberryPI with the monitor and mouse/keyboard next to your minigantry. 
  # -2- Attach the microscope arm for the minigantry.
  # -3- Plug USB microscope into RasberryPI. (optional: place into Microscope Arm)
  # -4- (Easier With 25 D-Sub Connector) Connect the MiniGantry's GPIO OUTPUT pin #8 to the negative channel on the input of the Relay.  (WIRE #1)
  # -5- (Easier With 25 D-Sub Connector) Connect the MiniGantry's GPIO 24V Power pin the to the Positive Channel on the input of the Relay. (WIRE #2)
  # -6- Connect Relay's Positive Output to 3V Power (Pin 1)  (WIRE #3)
  # -7- Connect Relay's Negative output to RasberryPi's GPIO26 (Pin 27) (WIRE #4)

#3 How to Install (Software): 
  #Start With a New Installation of Rasbian on Your RasberryPi, Old Versions are hard to fix, fresh os is best
      -This is done by removing the SD Card, and reformatting it on a PC, then Using the Rasbian Install Tool, from thier website.
  #Next, preparing a virtual environement on the raspberyPi. 
      -Go Through OS setup steps
      -Create a folder on the desktop named 'WBENV'
      -Open Terminal and Type: sudo apt-get update
      -and then: sudo apt-get upgrade
      -and then: cd ~/Desktop
      -After that: python3 -m venv WBENV  
      -After that: source Desktop/WBENV/bin/activate
      -After that: pip install pillow python-vlc pyautogui subprocess os RPi.GPIO 
  #Next, the Installation
      -Move onto the desktop: GUI.pi, The Indexs, StartWBPhotos.sh, and the two lab images
      -In Terminal Type: chmod +x Desktop/StartWBPhotos.sh
      This will allow you to start the program by typing this into a fresh terminal:
        "Desktop/StartWBPhotos.sh"


#4 How to run: 
    1. Open Terminal
    2. Type Into Terminal: Desktop/StartWBPhotos.sh

        or
         
    1. Right Click on GUI.py
    2. Click Thonny (if needed: change interpreter to desktop environment)
    3. Press the Green Start Button