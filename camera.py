from picamera import PiCamera

class Camera:

  def takePicture()
    camera = PiCamera()
    print("timestamp = ", datetime.now())
    camera.capture('/home/pi/Desktop/image' + datetime.now() + '.jpg')