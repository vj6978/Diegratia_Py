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
        self.initialConfiguration = False

    def open(self):
        if not self.initialConfiguration:
            self.start()
        self.box.onBreach()

    def start(self):
        print("Initializing Box With Device ID : {}".format(self.deviceId))
        print("Powering On and calling initialConfiguration method")
        self.box.onInitialConfiguration()
        self.initialConfiguration = True

    def deactivate(self):
        self.box.onDeactivation()
        self.initialConfiguration = False

driver = Driver()

# D1.configure_the_box()
# while D1.deactivate_the_box()==False:
#     D1.detect_box_is_opened()
