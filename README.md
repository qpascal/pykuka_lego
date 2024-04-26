# PyKUKA LEGO Robot

## Documentation links

[PyBricks Documentation](https://docs.pybricks.com/en/latest/)  
[PyBricksDev Guide](https://pypi.org/project/pybricksdev/)

[Interfacing with Inventor Hub](https://github.com/smr99/lego-hub-tk)

Further information on papers

## Installation & Piloting

### Basic scanning and piloting attempt

- Turning on the robot and plugging it in
- Big command to see LEGO Rules for every Hub :
```shell
pipx run pybricksdev udev | sudo tee /etc/udev/rules.d/99-pybricksdev.rules
```
- Command to execute code (after installing pybricksdev on pipx)
```shell
pybricksdev run usb filename.py
```
- Command to give permission to access the device
```shell
sudo chmod 666 /dev/ttyAMA0
```

### Connection & Piloting using lego-hub-tk

#### Python Packages

Install pre-requisite Python packages.

Either install the minimal set of packages:

```shell
pip3 install -r requirements.txt
```

#### Configuration

Out of the box, the software uses the USB cable to connect to the hub.  It will automatically determine the correct USB device.  
If the auto-detection does not work on your system, or if you wish to use bluetooth, the connection can be specified by configuration file.  

Create and edit the configuration file:

1. Locate the correct user_config_dir for your system (see https://pypi.org/project/appdirs/) and create a sub-directory named 'lego-hub-tk'.
   - For linux, this will be `mkdir ~/.config/lego-hub-tk/`
2. Copy the template file lego_hub.yaml to the newly-created directory.
   - For linix, this will be `cp lego_hub.yaml ~/.config/lego-hub-tk/lego_hub.yaml`
3. Edit your copy of lego_hub.yaml, following the notes in the template file.
   - For linix, this will be `nano ~/.config/lego-hub-tk/lego_hub.yaml`  

## Remaining errors

### From basic tests

> AttributeError: 'REPLHub' object has no attribute '_stdout_line_queue'

### From lego-hub-tk method