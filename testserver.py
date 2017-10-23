from flask import Flask
from flask import render_template

app = Flask(__name__)


# import serial

@app.route('/test')
def count():
    # Logic for getting arduino stuff
    # from_arduino = -1
    # ser = serial.Serial('COM3', 9600)
    #from_arduino = ser.readline()
    # print from_arduino
    return str("yooooooo wassssssssssuuuuppp!")
    #print "hey I'm working"
    #return str("woah I'm working")