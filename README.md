# ==================================================
# ----------------- ESPiNet ------------------------
# ==================================================
# ESP-32Cam

# Introduction

New home camera network project. I call it "EsPiNet" (Es-Pie-Net)

EsP = esp32-cam
Pi = Raspberry Pi
iNet = lan/internet

A clumsy portmanteau for a very inexpensive, powerful, private, feature-rich DIY home-security system that will also have plenty of home-automation support. 
Low cost, no subscription, and no piping of private/personal data to any cloud to be exploited. Totally open-source, and you can build it yourself.

I am planning on making a well-structured repository/library containing the software, firmware, enclosure models (.stl & .step), and how-to documentation that should be able to get the average (somewhat computer-savvy) person up and running.

The core system hardware consists of a Raspberry Pi main-hub (master), and ESP32 'nodes' (slaves).

The RPi master will have a super nifty 12 megapixel wide-angle camera, which will be mounted on a 2-servo pan/tilt platform, which can be controlled by both the user, or automated in conjunction with computer-vision object tracking. It will also serve as the isolated wifi host for the ESP32-cam boards, and server for the browser-based graphic interface and camera-streams. I intend to use this as LAN only, but may add support for making the system accessable remotely.

You could use only Pis if desired (if you wanted AI object tracking, or high resolutions with high frame rates)
However the Esp32-Cams are VERY inexpensive, and perform decently well -- great for security purposes.
	- The controller/camera cost about 10-15 dollars each, which is a rediculously good price, especially when purchased in multipacks. 
	- You could put up 5x esp32-cams to capture all angles of your home for just around ~$50.
	- These also support 

Other functions I'd like to eventually integrate/support:
	- Various types of sensors, such as environmental sensors (temperature/humidity/barometric-pressure/'air-quality'), door/window sensors, and more. 
	- Other use-cases/variants of the Pi/cam, like one that's specialized for tracking/spotting neat stuff in the night sky, or one that uses 2x 180 degree cameras for full 360 view that you can stick up on a long pole, etc.

Library will consist of: 
- Python code for Rpi
- A shell script for automatically installing dependencies 
	- I may include a docker file so people can install dependencies in a container/virtual-environment if they are only wanting to experiment
- Arduino code (possibly Python instead) for the ESP32s
	- I may try to come up with a way to flash the ESP32s with the Raspberry Pi. 
		- This would be ideal since Pi could update and flash certain fields itself is using, such as network credentials
		- You wouldn't need a seperate computer to flash the esp32s, outside of imaging the Pi OS. 
			- Even then, you could purchase a Pi with the OS already flashed to an SD, eliminating the need for a seperate computer. (you would still need keyboard/mouse/monitor or a touchscreen)
- 3D print .stl/steps
- Build documentation
- List of stuff to buy
- I may also include the entire Pi linux image so people don't have to figure out how to use linux and install a bunch of stuff
- I'm probably forgetting some things, and will likely get more ideas to add later

When I get a stable build going that covers basic functionality of the RPi with ESP32 camera streams on a browser, I will release the github repo, so other can start playing with it. If you also have some thoughts/ideas, let's jam.

I will post more updates as I make progress. 

#####################################################################################################################################################################################################################
#
pi camera master with esp32 cam nodes

This Repository is for a home security project that includes using esp32-cams for camera nodes,
and a raspberry pi orchestrator.

The pi in this particular project will also have a cam (ArducamV3).
I have also put together a dual-servo pan/tilt mount for the pi/arducam -- but that's further down the road.

The Pi 'orchestrator' will broadcast a wifi hotspot for the esp32-cams to connect to, while also being 
connected to the home network. This will either use it's internal wifi and a wifi dongle, or ethernet. 
  This will allow the home security network to be on a seperated network of it's own. Easing congestion
  and making the static ip process easier.

Required Hardware:
  Raspberry Pi (I'm using a Rpi 4)
  Wifi Dongle or Ethernet cable
  ESP32-cam(s) (you can easily pick these up for about $10-15ea on amazon. Multipacks = better)
  Device for viewing webpages
Optional Hardware:
  Raspberry Pi Camera (I am using Arducam v3)
  Arducam pan/tilt platform, or Pan/Tilt servos and your own mounting 
    https://a.co/d/2lyy3tC I recieved this without the unneeded i2c->pwm board. RPi can PWM already.
  Enclosures of your choice

Dependencies for this project (subject to change)
  libcamera
  opencv
  flask

Setup
- This guide assumes you understand hardware connections.
- Update RPi: (https://www.raspberrypi.com/documentation/computers/os.html#updating-and-upgrading-raspberry-pi-os)
    sudo apt update
    sudo apt full-upgrade
- Install Dependencies:
    sudo apt-get install python3-flask


# Creating a virtual environment (optional)
## Create a new environment using venv (this assumes you have python3 installed)
### Navigate to desired directory to create/store new venv
python3 -m venv venv-espinet
### This creates a new controlled, isolated instance of python3 and its dependencies
### You will need to activate the new venv and make it your currently active environment (runtime environment)
