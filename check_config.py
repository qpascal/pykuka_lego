# check_config.py (From Spike Python Tutorials)


from pybricks.hubs import InventorHub                                           # Same firmware as PrimeHub, just different class
from pybricks.pupdevices import Motor                                           # Only motors connected
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
from pybricks.iodevices import PUPDevice

# ---- DETECT WHAT IS CONNECTED TO EACH PORT ----

""" device_names = {
    48: "SPIKE Medium Angular Motor",
    49: "SPIKE Large Angular Motor",
    61: "SPIKE Color Sensor",
    62: "SPIKE Ultrasonic Sensor",
    63: "SPIKE Force Sensor"
} """

ports = [Port.A, Port.B, Port.C, Port.D, Port.F]
print("Hub configuration")


for port in ports:
    device = PUPDevice(port)
    print(port, ": ", device.info()["id"])


# CHECK THAT LEFT AND RIGHT MOTORS ARE CONNECTED TO CORRECT PORTS
first_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
second_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
first_motor.run_angle(20,90)
second_motor.run_angle(20,90)
first_motor.Direction=Direction.CLOCKWISE
second_motor.Direction=Direction.CLOCKWISE
first_motor.run_angle(20,90)
second_motor.run_angle(20,90)