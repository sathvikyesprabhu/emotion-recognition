import serial
import RPi.GPIO as GPIO
import time

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.baudrate = 9600

if __name__ == "__main__":
	with open('output.txt', 'wb') as f:
		while True:
			read_ser = ser.readline()
			f.write(read_ser)
			print(read_ser)
      
