import serial
# Logic for getting arduino stuff
from_arduino = -1
# ser = serial.Serial('/dev/ttyS2.usbserial', 9600)
ser = serial.Serial('COM3', 9600)
from_arduino = ser.readline()
print from_arduino
# return str(from_arduino)
#print "hey I'm workin
# g"
#return str("woah I'm working")