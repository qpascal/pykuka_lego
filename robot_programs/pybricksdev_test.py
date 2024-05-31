from pybricks.hubs import InventorHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = InventorHub()

# Initialize a motor at Port A
example_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE)

# Make the motor run clockwise at 30 degrees per second
example_motor.run(-60)

# Wait for three seconds
wait(3000)

# Make the motor run counterclockwise at 30 degrees per second
example_motor.stop()