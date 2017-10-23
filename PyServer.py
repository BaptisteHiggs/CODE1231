from flask import Flask
from flask import render_template

app = Flask(__name__)


import serial

@app.route('/test')
def count():
    # Logic for getting arduino stuff
    from_arduino = -1
    ser = serial.Serial('COM3', 9600)
    from_arduino = ser.readline()
    print from_arduino
    return str(from_arduino)
    #print "hey I'm working"
    #return str("woah I'm working")


@app.route('/')
def test():
    # Logic for getting arduino stuff
    #from_arduino = -1
    #ser = serial.Serial('/dev/ttyS2.usbserial', 9600)
    #from_arduino = int(ser.readline())
    #print from_arduino
    #return str(from_arduino)
    print "hey I'm working"
    # return str("woah I'm working")
    #ser = serial.Serial('COM3', 9600)
    #from_arduino = ser.readline()
    # print from_arduino
    return render_template('bikestat.html', num_people="14")

if __name__ == '__main__':
    app.run(host='0.0.0.0')