# cam_servo.py
import RPi.GPIO as GPIO

class Servo:
    def __init__(self, pin, frequency=50, range_degrees=180):
        self.pin = pin
        self.frequency = frequency
        
        assert range_degrees in range(0,360)
        
        # assume servo is 180* unless otherwise specified
        self.range = range_degrees
        
        GPIO.setup(self.pin, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.pin, self.frequency)
        self.pwm.start(0)

    def move_to(self, duty_cycle):
        self.pwm.ChangeDutyCycle(duty_cycle)

    def stop(self):
        self.pwm.ChangeDutyCycle(0)
        self.pwm.stop()

    def change_frequency(self, freq:int) -> None:
        self.frequency = freq
        self.pwm = GPIO.PWM(self.pin, self.frequency)
    # Add any other servo-related methods here
    
class ServoDebugMode(Servo):
    def __init__(self, pin:int, frequency=50, range_degrees=180):
        #super().__init__(self, pin, frequency, range_degrees)
        
        while True: 
            input_list = self.get_input()
            
            if input_list[0] == 'q': 
                break
            elif input_list[0] == 'h': 
                self.print_help()
                continue
            elif len(input_list) == 3:
                cmd = input_list[0]
                servo = input_list[1]
                value = input_list[2]
            else: 
                print('bad entry, try again')
                continue
            
            if cmd == 'move': 
                print(f'moving {servo} to {value}')
                super().move_to(value)
            if cmd == 'set':
                print(f'changing frequency on {servo} to {value}')
                self.change_frequency(value)
        
        
    def get_input(self) -> list:
        user_input = input("Enter servo command (enter h for help) ")
        parsed_input = user_input.split(' ')
        print(parsed_input)
        return parsed_input
        
    def print_help(self) -> None:
        print("Current supported commands: \n"
        'move [pan/tilt] [angle]\n' 
        'set [pan/tilt] freq [new freq value]\n' 
        '"q" to quit debug mode')
        

            