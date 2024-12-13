#READ THIS DOCUMENT TO SETUP WIREBOND PHOTOS ON THE MINIGANTRY

#1 Materials: Mini Gantry, Rasberry Pi, Solid State Relay, USB Microscope, Microscope Arm for the Minigantry (3D Printable)(Made in Steel at UCSB), Mouse, Keyboard, Monitor, D-Sub Connector
  # USB MICROSOPE: https://www.amazon.com/dp/B07DQM237K?ref=fed_asin_title
  # Solid State Replay: https://www.amazon.com/dp/B00B888WVC?ref=fed_asin_title
  # Rasberry Pi (3 or Higher) (With Rasbian)
  # Microscope Arm for Mini Gantry (Email, Susanne or Paolo from UCSB for STL or CAD file)
  # 25 Pin D-Sub Connector (male) (makes it easier to remove setup from minigantry) (bought at UCSB Physics's lab supply room)

#2 How to build (Hardware):
  # -1- Set Up your RasberryPI with the monitor and mouse/keyboard next to your minigantry. 
  # -2- Attach the microscope arm for the minigantry.
  # -3- Plug USB microscope into RasberryPI. (optional: place into Microscope Arm)
  # -4- (Easier With 25 D-Sub Connector) Connect the MiniGantry's GPIO OUTPUT pin #8 to the negative channel on the input of the Relay.  (WIRE #1)
  # -5- (Easier With 25 D-Sub Connector) Connect the MiniGantry's GPIO 24V Power pin the to the Positive Channel on the input of the Relay. (WIRE #2)
  # -6- Connect Relay's Positive Output to 3V Power (Pin 1)  (WIRE #3)
  # -7- Connect Relay's Negative output to RasberryPi's GPIO26 (Pin 27) (WIRE #4)

#3 How to Install (Software): 
  # Install Rasbian on Rasberry PI:
  # Download or USB the GUI.py Code, Place on desktop. 
  # Download Appropriate Indexs and Place on desktop.
  # on Desktop create folder called 'WireBondPhotos'
  # (if missing) pip install 'threading', 'vlc', 'tkinter'

#4 How to run: 
  # Right click on GUI.py and open in ThonnyIDE. 
  # Click Run
  # Select shape using buttons, then click basic start
  # follow instructions on GUI, Start the Minigantry program that the GUI says is correct. 
  # wait
  # Move Picture to Desired Location & Clean up 'WireBondPhotos' folder

  




