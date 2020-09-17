import time
import datetime
import pymongo
import requests
from BoxContract import BoxContract as contract

class Box:
    URI = "mongodb://127.0.0.1:27017"
    Database = "smart-box"

    def __init__(self,device_no):
        self.device_no=device_no
        self.status=self.state()
        self.msg = "The box is safe(or yet to be configured)"
        self.num_of_times_box_opened = 0
        self.condition_of_the_box = "closed"
    def json(self):
        return{
        "device_no":self.device_no,
        "status":self.status,
        "msg":self.msg,
        "number_of_times_box_was_opened":str(self.num_of_times_box_opened),
        "condition_of_the_box":self.condition_of_the_box
        }
    def save_to_mongo(self):
        client = pymongo.MongoClient(Device.URI)
        Database = client[Device.Database]
        Database["sb" + self.device_no].insert(self.json())
        headers = {'Content-type':'application/json','Accept':'application/json'}
        pload = self.json()
        r = requests.post(url = "https://cargodiegratia.herokuapp.com/api/new",json=pload,headers=headers)
        print("Response is: %s"%r.text)

    def state(self):
        time.sleep(0.1)
        try:
            file = open("status"+self.device_no+".txt","r+")
            file.close()
        except:
            file = open("status"+self.device_no+".txt","x")
            file.close()
        file = open("status"+self.device_no+".txt",'r+')
        status_code = file.read(2)
        print(status_code)
        file.close()
        if status_code=="07":
            return("The box is configured")
        else:
            return("The box is not configured")
    def configure_the_box(self):
        self.save_to_mongo()
        time.sleep(0.1)
        if self.status=="The box is configured":
            self.status="The box is already configured and is now rebooted"
            self.save_to_mongo()
            print(self.status)
            self.status = self.state()
            try:
                file=open("condition_of_the_box"+self.device_no+".txt","r+")
            except:
                file=open("condition_of_the_box"+self.device_no+".txt","x")
            file.close()
            file=open("condition_of_the_box"+self.device_no+".txt","r+")
            m=file.read(6)
            file.close()
            self.config_the_box=m
            try:
                file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
            except:
                file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
            file.close()
            file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
            m=file.read(5)
            if m=="":
                m=0
            else:
                m=int(m)
            file.close()
            self.num_of_times_box_opened=m
        else:
            config_the_box = input("Do you want to configure the box: (y)")
            if(config_the_box=="y"):
                file=open("status"+self.device_no+".txt","r+")
                file.write("07")
                file.close()
                timenow = datetime.datetime.now()
                self.status="The box is successfull configured at time {}.".format(timenow)
                print(self.status)
                self.status = self.state()
                try:
                    file=open("condition_of_the_box"+self.device_no+".txt","r+")
                except:
                    file=open("condition_of_the_box"+self.device_no+".txt","x")
                file.close()
                file=open("condition_of_the_box"+self.device_no+".txt","r+")
                file.write(self.condition_of_the_box)
                file.close()
                try:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                except:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
                file.close()
                file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                file.write(str(self.num_of_times_box_opened))
                file.close()
                self.save_to_mongo()


    def detect_box_is_opened(self):
        time.sleep(0.1)
        try:
            file=open("Detect_for_opening.txt","r+")
        except:
            file=open("Detect_for_opening.txt","x")
        file.close()
        file = open("Detect_for_opening.txt","r+")
        read_signal=file.read(1)
        if read_signal=="1":
            timenow=datetime.datetime.now()
            if self.condition_of_the_box=="closed":
                self.msg="The box was opened at time {}.".format(timenow)
                print(self.msg)
                self.num_of_times_box_opened=self.num_of_times_box_opened+1
                try:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                except:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
                file.close()
                file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                file.write(str(self.num_of_times_box_opened))
                file.close()
                self.save_to_mongo()

            self.condition_of_the_box="opened"
            try:
                file=open("condition_of_the_box"+self.device_no+".txt","r+")
            except:
                file=open("condition_of_the_box"+self.device_no+".txt","x")
            file.close()
            file=open("condition_of_the_box"+self.device_no+".txt","r+")
            file.write(self.condition_of_the_box)
            file.close()
        else:
            self.condition_of_the_box="closed"
            try:
                file=open("condition_of_the_box"+self.device_no+".txt","r+")
            except:
                file=open("condition_of_the_box"+self.device_no+".txt","x")
            file.close()
            file=open("condition_of_the_box"+self.device_no+".txt","r+")
            file.write(self.condition_of_the_box)
            file.close()
    def deactivate_the_box(self):
            try:
                file=open("Detect_for_deactivation.txt","r+")
            except:
                file=open("Detect_for_deactivation.txt","x")
            file.close()
            file = open("Detect_for_deactivation.txt","r+")
            read_signal=file.read(1)
            file.close()
            if read_signal=="1":
                try:
                    file = open("status"+self.device_no+".txt","r+")
                    file.close()
                except:
                    file = open("status"+self.device_no+".txt","x")
                    file.close()
                file = open("status"+self.device_no+".txt",'r+')
                file.write("19")
                file.close()
                try:
                    file=open("condition_of_the_box"+self.device_no+".txt","r+")
                except:
                    file=open("condition_of_the_box"+self.device_no+".txt","x")
                file.close()
                file=open("condition_of_the_box"+self.device_no+".txt","r+")
                file.write(self.condition_of_the_box)
                file.close()
                try:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                except:
                    file=open("number_of_times_box_was_opened"+self.device_no+".txt","x")
                file.close()
                file=open("number_of_times_box_was_opened"+self.device_no+".txt","r+")
                file.write(str(self.num_of_times_box_opened))
                file.close()
                self.status="The box is being deactivated"
                print(self.status)
                self.save_to_mongo()
                return True

            else:
                return False
