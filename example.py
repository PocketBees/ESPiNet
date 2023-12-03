import RPi.GPIO as GPIO
import time
import smbus2
import bme280
import subprocess
import sys
import cam_servo

# Sleep time in uS
sleep_time = 1

# Servo_pins
pin_pan = 17
pin_tilt = 18
# Servo_range = np.linspace(5, 10, servo_total_positions)
servo_range = [5,6,7,8,9,10]
# Servo Debugging mode (manual servo control via terminal)
debug_pan_servo = True
debug_tilt_servo = True


# BCM pin numbering, disable warnings 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)

# Initialize servos
servos = {
'pan' : cam_servo.Servo(pin_pan, 50),# Pan servo
'tilt' : cam_servo.Servo(pin_tilt, 50) # Pan servo
}
# I2C setup for BME280
port = 1
address = 0x76  # BME280 address (could be 0x77)
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)
    
# Test Servos
# TODO: I want to use Servo class to create servo info, then debug mode
#   stems from that. Not sure I should be using child class
if debug_pan_servo == True:
    cam_servo.ServoDebugMode(pin_pan)
    
# try:
for servo in servos.values():
    for position in servo_range:
        print(f"moving {servo} to {position}")
        servo.move_to(position)
        time.sleep(sleep_time)
    servo.stop()
# except:
#     print("Exception occured while attempting to move servo(s)")
#     for servo in servos.values():
#         servo.stop()
#     print("Disabled servos...")
#     sys.exit()
        

# Test BME280 sensor
print("Testing BME280 sensor.")
data = bme280.sample(bus, address)
print(f"Temperature: {data.temperature} C")
print(f"Humidity: {data.humidity} %")
print(f"Pressure: {data.pressure} hPa")

# Test Camera with libcamera command-line tools
print("Testing Arducam v3 with libcamera.")
# The command below is an example and will vary based on your needs
# This example captures an image and saves it to a file
try:
    subprocess.run(["libcamera-still", "-o", "test.jpg"], check=True)
    print("Captured image with libcamera.")
except subprocess.CalledProcessError as e:
    print(f"Failed to capture image: {e}")

# Cleanup
GPIO.cleanup()
print("Hardware test completed.")