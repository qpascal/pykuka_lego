from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from usys import stdin, stdout
from uselect import poll

hub = InventorHub()

# Initialize a motor at Port A
example_motor = Motor(Port.B,Direction.CLOCKWISE)

# Make the motor run clockwise at 30 degrees per second
example_motor.run_angle(speed=125,rotation_angle=2125)

# Make the motor run counterclockwise at 30 degrees per second
# example_motor.stop()