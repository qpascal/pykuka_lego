from pybricks.ev3devices import Motor
from pybricks.parameters import Port,Color
from pybricks.tools import wait

# Initialize a motor at port A
example_motor = Motor(Port.A)

# Make the motor run clockwise at 45 degrees per second
example_motor.run(30)

# Wait for 2 seconds
wait(2000)

# Make the motor run counterclockwise at 45 degree per second
example_motor.run(-45)

# Stop the motor
example_motor.brake()