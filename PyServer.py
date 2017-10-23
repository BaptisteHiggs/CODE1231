from flask import Flask
from flask import render_template

app = Flask(__name__)

valCount = 0

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
    global valCount
    print "hey I'm workin"
    # return str("woah I'm working")
    ser = serial.Serial('COM3', 9600)
    from_arduino = str(ser.readline())
    try:
        if '1' in from_arduino:
            print 'ooooh'
            valCount += 1
            print valCount
    except Exception:
        print 'oopsies'
    print 'wowsers'
    print valCount
    return render_template('bikestat.html', num_people=str(valCount), num_emissions=str(valCount*6.7))

if __name__ == '__main__':
    app.run(host='0.0.0.0')