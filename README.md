# ESPiNet
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
