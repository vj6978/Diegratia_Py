from Driver import Driver
from utility import Utility
import threading

driver = Driver()

#Happy Path Test Suite
def happy_path_test():
    print("\nInitiating Happy Path Test")
    print("\n---------------------------")
    driver.open()
    driver.open(True)

#Breach Path Test Suite:
def breach_path_test():
    print("\nInitiating Breach Path Test")
    print("\n---------------------------")
    driver.open()
    driver.open()

happy_path_test()
# breach_path_test()