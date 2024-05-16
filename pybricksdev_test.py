from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialize a motor at Port A
example_motor = Motor(Port.A)

# Make the motor run clockwise at 30 degrees per second
example_motor.run(30)

# Wait for three seconds
wait(3000)

# Make the motor run counterclockwise at 30 degrees per second
example_motor.run(-30)