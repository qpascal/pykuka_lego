# Using pyusb to talk to the robot
import usb.core

# Find a device (vendor & product can be found via lsusb)
def find_usb_device(vid,pid):
    device = usb.core.find(idVendor=vid,idProduct=pid)

    if device is None :
        raise ValueError("USB Device not found")

    return device

# Find the device's interfaces
def open_usb_interface(device, interface_number):
    device.set_configuration()
    usb.util.claim_interface(device,interface_number)
    endpoint = device[0][(0,0)][0]

    return endpoint

# Finding the robot
vendor_id = 0x0694
product_id = 0x0010
kuka_robot = find_usb_device(vendor_id,product_id)
"""
print(kuka_robot)

# Returns when robot plugged :  => robot_usb_log.txt 
# Returns when no robot      :  ValueError: USB Device not found
"""
# Finding the robot interfaces
interface_number = 0
endpoint = open_usb_interface(kuka_robot,interface_number)
"""
print(endpoint)

# Returns : usb.core.USBError: [Errno 13] Access denied (insufficient permissions)
"""