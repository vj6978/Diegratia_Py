from Driver import Driver

driver = Driver()

#Happy Path Test Suite
def happy_path_test():
    print("\nInitiating Happy Path Test")
    print("\n---------------------------")
    driver.open()
    driver.open()

#Breach Path Test Suite:
def breach_path_test():
    print("\nInitiating Breach Path Test")
    print("\n---------------------------")
    driver.open()
    driver.open()

# happy_path_test()
breach_path_test()