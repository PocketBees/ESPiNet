from flask import Flask, render_template
from cam_servo import Servo  # Replace with your actual import

app = Flask(__name__)

# Initialize your servos (replace pins with your actual GPIO pins)
pan = Servo(17)
tilt = Servo(18)

# both home servos and store position
home_position = 7
pan_position = tilt_position = home_position
# move amount for each button press
increment = 0.5  # Define how much you want to move the servo on each button press

pan.move_to(pan_position)
tilt.move_to(tilt_position)

@app.route('/')
def index():
    return render_template('index.html')  # We will create this HTML file next

@app.route('/move/<direction>')
def move_servo(direction):
    global pan_position, tilt_position, increment
    print(f'move {direction}')
    if direction == 'up':
        assert 3 < pan_position + increment < 11
        tilt_position += increment
        tilt.move_to(tilt_position)
        pass
    elif direction == 'left':
        assert 3 < pan_position - increment < 11
        pan_position -= increment
        pan.move_to(pan_position)
        pass
    elif direction == 'right':
        assert 3 < pan_position + increment < 11
        pan_position += increment
        pan.move_to(pan_position)
        pass
    elif direction == 'down':
        assert 3 < tilt_position - increment < 11
        tilt_position -= increment
        tilt.move_to(tilt_position)
        pass
    elif direction == 'home':
        tilt_position = pan_position = home_position
        tilt.move_to(tilt_position)
        pass
    return '', 204  # No content response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')