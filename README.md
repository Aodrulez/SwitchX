# SwitchX

Project that adds XBOX360 controller support to Nintendo Switch using Raspberry Pi Zero W

### Demo (Youtube):
[XBOX360 wireless controller + Raspberry Pi Zero W = DIY Nintendo Switch Pro Controller](https://www.youtube.com/watch?v=2AfX-11PWtA "XBOX360 wireless controller + Raspberry Pi Zero W = DIY Nintendo Switch Pro Controller")

### Description
This project uses Raspberry Pi Zero W to act as a proxy between XBOX360's controller & Nintendo Switch. It essentially makes the Raspberry Pi connect to Switch as a Bluetooth controller & translates XBOX360 controller's input to the format expected by Nintendo Switch. It should work with both Wireless & Wired versions of the controller. XBOX360 controllers use proprietary wireless protocol to communicate & requires a special driver to work. Since Nintendo Switch lacks this driver, it won't detect the controller when connected via USB port directly & requires some contraption to work. 

### Requirements:

-  XBOX360 Controller (Wired/Wireless)
- XBOX360 Controllers' USB wireless receiver (Only for wireless model)
- Raspberry Pi Zero W
- OTG Cable Micro USB

### Setup:
- Install Raspbian (Lite) on your Raspberry Pi Zero W
- Clone this repository to your user account's home directory
- Execute "sudo python setup.py"
- Reboot your Raspberry Pi Zero W
- Connect XBOX360 Controller/USB Wireless receiver to Raspberry Pi Zero w's Micro-USB  data port
- Connect power to Raspberry Pi Zero W's Micro-USB power port

This is should automatically install all of the dependencies as well as setup the environment.

### Usage:
- Once setup is ready, Raspberry Pi Zero should automatically connect to Nintendo Switch when you enter pairing screen (Home -> Controllers -> Change Grip/Order)
- Once paired, the controller should work exactly like the Pro Wireless Controller.
- Pairing should only be required the first time. Henceforth, you'll only need to wake up the Switch console & SwitchX should automatically reconnect.

### Key Mapping
XBOX360 Controller's keys are mapped as follows: 
(XBOX360 on the left & Switch on the right)
- X = Y
- Y = X
- A = B
- B = A
- Guide = Home
- Long press Guide = Capture
- Back = Minus
- Start = Plus
- Dpad = Dpad
- Analog sticks = Analog sticks
- Triggers = Triggers



### Credits:
This project wouldn't have been possible without "Martino's" Joycontrol Project as well as Steven Jacobs' script to interface with xboxdrv using Python. Links:
- https://github.com/mart1nro
- https://github.com/FRC4564/Xbox

### End
