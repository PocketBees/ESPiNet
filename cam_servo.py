# cam_servo.py
import RPi.GPIO as GPIO
import time

class Servo:
    def __init__(self, pin, frequency=50, range_degrees=180):
        """ 
        Eventually structure servo data into  a dict like this after parson the config.json with import json: 
        
                servos = { 
            pan: 
            {
                safe_range: 
                { 
                    min : value, 
                    max: value
                },
                duty_cycle : value
                }
            ,
            tilt: 
            {
                safe_range: 
                { 
                    min : value, 
                    max: value
                },
                duty_cycle : value
                }
            } 
        """
        
        self.pin = pin
        self.frequency = frequency
        assert 0 <= range_degrees <= 360, "Range degrees must be between 0 and 360"
        self.range = range_degrees
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)

    def move_to(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)
        time.sleep(0.5)
        self.pwm.ChangeDutyCycle(0)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()

    def change_frequency(self, freq):
        assert freq > 0, "Frequency must be greater than 0"
        self.frequency = freq
        self.pwm.ChangeFrequency(freq)

class ServoDebugMode:
    def __init__(self, pan_pin, tilt_pin, frequency=50):
        self.servos = {
            'pan': Servo(pan_pin, frequency),
            'tilt': Servo(tilt_pin, frequency)
        }

    def debug_mode(self):
        print("Entering servo debug mode. Type 'h' for help or 'q' to quit.")
        while True:
            user_input = input("> ").split()
            if len(user_input) < 3 or user_input[0] not in ['move', 'set-freq']:
                if user_input and user_input[0] == 'q':
                    break
                self.print_help()
                continue
            
            cmd, servo_name, value = user_input
            if servo_name not in self.servos:
                print("Invalid servo name. Valid names are 'pan' or 'tilt'.")
                continue

            if cmd == 'move':
                self.servos[servo_name].move_to(float(value))
            elif cmd == 'set-freq':
                self.servos[servo_name].change_frequency(int(value))
            else:
                print("Invalid command.")
        
    def set_range(self):
        """        
        allow user to enter debug mode, move servos manually to certain points,
        and enter a command to 'save range' for servo. 
        """
        return
            
  

    
    def print_help(self):
        print("Commands:")
        print("  move [pan/tilt] [duty_cycle] - Move specified servo")
        print("  set-freq [pan/tilt] [frequency] - Set frequency of specified servo")
        print("")
        print("Example Usages:")
        print("     move pan 7        -- moves pan servo to 7 (usually nuetral position)")
        print("     set-freq tilt 50  -- changes pwm frequency on tilt")
        print("")
        print("q - Quit debug mode")
        print("")

    def stop_all(self):
        for servo in self.servos.values():
            servo.stop()
