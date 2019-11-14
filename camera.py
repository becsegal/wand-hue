from picamera import PiCamera

class Camera:

  def takePicture(self):
    camera = PiCamera()
    print("timestamp = ", datetime.now())
    camera.capture('/home/pi/Desktop/image' + datetime.now() + '.jpg')