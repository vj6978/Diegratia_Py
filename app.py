from device import Device
D1 = Device("1234")
D1.configure_the_box()
while D1.deactivate_the_box()==False:
    D1.detect_box_is_opened()
