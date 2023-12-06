#!/usr/bin/env python3
"""
Script that serves as a tool where the user can send manual servo control commands.
The purpose is to allow the user to debug their servos, or even just play around with them.
I found it useful to figure out the correct frequency of some unknown servos I had laying 
around. I also wanted some experience creating a child class, so I created ServoDebugMode()
in cam_servo.py

This must be ran on the Raspberry Pi with the servo(s) properly connected. You will likely
also need to change permissions of this file with:
    
    sudo chmod +x run_servo_debug.py
"""

from cam_servo import ServoDebugMode
import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BCM)  # Set the GPIO mode
    pan_pin = 17  # Replace with the GPIO pin for the pan servo
    tilt_pin = 18  # Replace with the GPIO pin for the tilt servo
    debug_servo = ServoDebugMode(pan_pin, tilt_pin)  # Initialize the debug servo
    try:
        debug_servo.debug_mode()  # Enter debug mode
    finally:
        debug_servo.stop_all()
        GPIO.cleanup()

if __name__ == "__main__":
    main()