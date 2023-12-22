from s3_connect import s3_connection
from camera import capture
import serial
import time

s3 = s3_connection()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()

def upload_file(file_dir):
	global s3
	try:
		print(file_dir[-23:])
		s3.upload_file(file_dir, "desk-tracker", file_dir[-23:])
		print("upload success")
	except Exception as e:
		print(e)


while True:
	if ser.in_waiting > 0:
		line = ser.readline().decode('utf-8').rstrip()
		if line == 'ON':
			file_dir = capture()
			upload_file(file_dir)
			time.sleep(10)
	