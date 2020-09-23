import threading

class BreachProtocol(threading.Thread):
    """
        Code to capture images and other required breach events
    """
    def run(self):
        print("Initiating Breach Protocol")