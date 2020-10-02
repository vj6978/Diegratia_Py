import threading
import config
import time

"""
    Use this class for countdown to 0 in case of delays if required.
"""
class DeactivationService(threading.Thread):
    def __init__(self, event):
        threading.Thread.__init__(self)
        self.t_zero = config.DEACTIVATION_MESSAGE_EXPECTED_IN_SECONDS
        self.event = event
        self.timeRanOut = False
        self.deactivationMessage = False

    """
        Use this method to listen for any deactivation message
    """
    def run(self):
        #TODO: Open connection with server. Wait for Deactivation message.
        time.sleep(config.DEACTIVATION_MESSAGE_EXPECTED_IN_SECONDS)
        #Check if deactivation message arrived
        #Call set when deactivation message received
        if self.deactivationMessage == True:
            self.event.set()