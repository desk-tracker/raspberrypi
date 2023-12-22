from picamera import PiCamera
import datetime

def capture():
	camera = PiCamera()
	camera.rotation = 180
	camera.resolution = (1920,1080)
	now = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
	file_dir = '/home/loveliest/desk-tracker/images/img_' + now + '.jpg'
	try:
		camera.capture(file_dir)
	finally:
		camera.close()
	
	return file_dir