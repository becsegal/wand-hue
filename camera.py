from picamera import PiCamera
from datetime import datetime

class Camera:

  def takePicture(self):
    camera = PiCamera()
    print("timestamp = ", datetime.now())
    camera.capture('/home/pi/Desktop/image' + datetime.now() + '.jpg')