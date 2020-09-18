import uuid
from Box import Box

"""
    Driver class
    Manages the lifecycle of the Box
"""
class Driver:

    #TODO: Ensure lifecycle methods are correct. Replace Constructor with correct lifecycle methods
    def __init__(self):
        self.deviceId = uuid.uuid4()
        self.box = Box(self.deviceId)
        self.boxBreach = False
        self.start()

    def start(self):
        print("Initializing Box With Device ID : {}".format(self.deviceId))
        print("Powering On and calling initialConfiguration method")
        self.box.intialConfiguration()
        self.alive()

    def alive(self):
        while not self.box.boxBreached:
            pass
        else:
            self.box.boxBreached()

    def deactivate(self):
        self.box.deactivate()

driver = Driver()

# D1.configure_the_box()
# while D1.deactivate_the_box()==False:
#     D1.detect_box_is_opened()
