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
servo_range = [4,5,6,7,8,9,10]


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
    
 # Function to record a video with the camera
def record_video(filename, duration):
    try:
        # Record a video to a file
        subprocess.run(['libcamera-vid', '-o', filename, '--inline', '--listen', '-t', str(duration)], check=True)
        print(f"Video saved as {filename}")
    except subprocess.CalledProcessError as e:
        print("Failed to record video:", e)   
        
def get_bme280_sample():
    # Test BME280 sensor
    print("Testing BME280 sensor.")
    data = bme280.sample(bus, address)
    print(f"Temperature: {data.temperature} C")
    print(f"Humidity: {data.humidity} %")
    print(f"Pressure: {data.pressure} hPa")
    
def test_servos():
    cam_servo.ServoDebugMode(pin_pan)
    


record_video('video.h264', 10000)  # Record for 10 seconds
get_bme280_sample()
time.sleep(1)
get_bme280_sample()

# Cleanup
GPIO.cleanup()
print("Hardware test completed.")