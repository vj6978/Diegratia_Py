import threading
import time
import config

"""
    Use this class for countdown to 0 in case of delays if required.
"""
class CountdownTimer(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.t_zero = config.DEACTIVATION_MESSAGE_EXPECTED_IN_SECONDS
        self.event = event
        self.timeRanOut = False
        self.deactivationMessage = False

    """
        Use this method to listen for any deactivation message
    """
    def initializeSocket(self):
        self.deactivationMessage == True

    def run(self):
        #TODO: Open connection with server. Wait for Deactivation message.
        self.initializeSocket()
        self.event.wait(config.DEACTIVATION_MESSAGE_EXPECTED_IN_SECONDS)
        #Call set when deactivation message received
        if self.deactivationMessage == True:
            self.event.set()