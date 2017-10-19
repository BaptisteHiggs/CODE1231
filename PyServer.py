from flask import Flask
app = Flask(__name__)

from_arduino = -1

import serial

@app.route('/')
def count():
    # Logic for getting arduino stuff
    ser = serial.Serial('/dev/tty.usbserial', 9600)
    from_arduino = int(ser.readline())
    print from_arduino
    return str(from_arduino)