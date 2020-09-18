import datetime
from Contract import BoxContract

"""
    Box lifecycle methods declared. 
    Define any extra methods here.
"""
class Box(BoxContract.Contract):

    def __init__(self, deviceId):
        self.deviceId = deviceId
        self.configuredState = False
        self.boxBreached = False
        self.msg = "The box is safe(or yet to be configured)"
        self.numOfTimesBoxOpened = 0

    def intialConfiguration(self):
        if not self.configuredState:
            self.configuredState = True
            # self.boxClosed = True
            # self.legalOpening = True
            print("Box - {} - Configuration Complete At : {}".format(self.deviceId, datetime.datetime.now()))
        else:
            pass

    # TODO: Action to perform when box is breached.
    def boxBreached(self):
        print("Box has been breached!")
        pass

    def deactivate(self):
        print("Deactivation Protocol Initiated!")
        pass

    def reboot(self):
        print("Rebooting")
        self.numOfTimesBoxOpened = self.numOfTimesBoxOpened + 1


    # def state(self):
    #     try:
    #         file = open("status"+self.device_no+".txt","r+")
    #         file.close()
    #     except:
    #         file = open("status"+self.device_no+".txt","x")
    #         file.close()
    #     file = open("status"+self.device_no+".txt",'r+')
    #     status_code = file.read(2)
    #     print(status_code)
    #     file.close()
    #     if status_code=="07":
    #         return("The box is configured")
    #     else:
    #         return("The box is not configured")
    #
    # def configure_the_box(self):
    #     self.save_to_mongo()
    #     time.sleep(0.1)
    #     if self.status=="The box is configured":
    #         self.status="The box is already configured and is now rebooted"
    #         self.save_to_mongo()
    #         print(self.status)
    #         self.status = self.state()
    #         try:
    #             file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         except:
    #             file=open("condition_of_the_box"+self.device_no+".txt","x")
    #         file.close()
    #         file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         m=file.read(6)
    #         file.close()
    #         self.config_the_box=m
    #         try:
    #             file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #         except:
    #             file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
    #         file.close()
    #         file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #         m=file.read(5)
    #         if m=="":
    #             m=0
    #         else:
    #             m=int(m)
    #         file.close()
    #         self.num_of_times_box_opened=m
    #     else:
    #         config_the_box = input("Do you want to configure the box: (y)")
    #         if(config_the_box=="y"):
    #             file=open("status"+self.device_no+".txt","r+")
    #             file.write("07")
    #             file.close()
    #             timenow = datetime.datetime.now()
    #             self.status="The box is successfull configured at time {}.".format(timenow)
    #             print(self.status)
    #             self.status = self.state()
    #             try:
    #                 file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #             except:
    #                 file=open("condition_of_the_box"+self.device_no+".txt","x")
    #             file.close()
    #             file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #             file.write(self.condition_of_the_box)
    #             file.close()
    #             try:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             except:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
    #             file.close()
    #             file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             file.write(str(self.num_of_times_box_opened))
    #             file.close()
    #             self.save_to_mongo()
    #
    #
    # def detect_box_is_opened(self):
    #     time.sleep(0.1)
    #     try:
    #         file=open("Detect_for_opening.txt","r+")
    #     except:
    #         file=open("Detect_for_opening.txt","x")
    #     file.close()
    #     file = open("Detect_for_opening.txt","r+")
    #     read_signal=file.read(1)
    #     if read_signal=="1":
    #         timenow=datetime.datetime.now()
    #         if self.condition_of_the_box=="closed":
    #             self.msg="The box was opened at time {}.".format(timenow)
    #             print(self.msg)
    #             self.num_of_times_box_opened=self.num_of_times_box_opened+1
    #             try:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             except:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
    #             file.close()
    #             file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             file.write(str(self.num_of_times_box_opened))
    #             file.close()
    #             self.save_to_mongo()
    #
    #         self.condition_of_the_box="opened"
    #         try:
    #             file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         except:
    #             file=open("condition_of_the_box"+self.device_no+".txt","x")
    #         file.close()
    #         file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         file.write(self.condition_of_the_box)
    #         file.close()
    #     else:
    #         self.condition_of_the_box="closed"
    #         try:
    #             file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         except:
    #             file=open("condition_of_the_box"+self.device_no+".txt","x")
    #         file.close()
    #         file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #         file.write(self.condition_of_the_box)
    #         file.close()
    # def deactivate_the_box(self):
    #         try:
    #             file=open("Detect_for_deactivation.txt","r+")
    #         except:
    #             file=open("Detect_for_deactivation.txt","x")
    #         file.close()
    #         file = open("Detect_for_deactivation.txt","r+")
    #         read_signal=file.read(1)
    #         file.close()
    #         if read_signal=="1":
    #             try:
    #                 file = open("status"+self.device_no+".txt","r+")
    #                 file.close()
    #             except:
    #                 file = open("status"+self.device_no+".txt","x")
    #                 file.close()
    #             file = open("status"+self.device_no+".txt",'r+')
    #             file.write("19")
    #             file.close()
    #             try:
    #                 file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #             except:
    #                 file=open("condition_of_the_box"+self.device_no+".txt","x")
    #             file.close()
    #             file=open("condition_of_the_box"+self.device_no+".txt","r+")
    #             file.write(self.condition_of_the_box)
    #             file.close()
    #             try:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             except:
    #                 file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
    #             file.close()
    #             file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
    #             file.write(str(self.num_of_times_box_opened))
    #             file.close()
    #             self.status="The box is being deactivated"
    #             print(self.status)
    #             self.save_to_mongo()
    #             return True
    #
    #         else:
    #             return False