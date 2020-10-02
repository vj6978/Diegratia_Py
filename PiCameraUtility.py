import time
import config
import datetime
import picamera
import picamera.array
from utility import Utility

class PiCameraUtility():
    def __init__(self, deviceId):
        self.utility = Utility()
        self.__deviceId = deviceId

    def snap(self):
        with picamera.PiCamera() as camera:
            camera.start_preview()
            """
                2 second delay required to allow sensors to detect light levels
            """
            time.sleep(2)
            with picamera.array.PiRGBArray(camera) as stream:
                camera.capture(stream, format='bgr')
                image = stream.array
                payload = {"DeviceId": self.__deviceId, "imageData": image}
                self.utility.saveToMongo(payload)