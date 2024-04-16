# PyKUKA LEGO Robot

## Documentation links

[PyBricks Documentation](https://docs.pybricks.com/en/latest/)  
[PyBricksDev Guide](https://pypi.org/project/pybricksdev/)

Further information on papers

## Commands

- Turning on the robot and plugging it in
- Big command to see LEGO Rules for every Hub :
``pipx run pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules``
- Command to execute code (after installing pybricksdev on pipx)
``pybricksdev run usb filename.py``
- Command to give permission to access the device
``sudo chmod 666 /dev/ttyAMA0``

## Remaining errors

> AttributeError: 'REPLHub' object has no attribute '_stdout_line_queue'