# PyKUKA LEGO Robot

## Documentation links

[PyBricks Documentation](https://docs.pybricks.com/en/latest/)  
[PyBricksDev Guide](https://pypi.org/project/pybricksdev/)

[Interfacing with Inventor Hub](https://github.com/smr99/lego-hub-tk)

Further information on papers

## First installation & scanning

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

## Connection & Piloting using lego-hub-tk

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

### First Test
Connect the hub using USB.  

List the programs currently stored on the hub:

```shell
python3 run_command.py ls
Slot Decoded Name                               Size Last Modified        Project_id   Type      
   0 Zero motors                                733b 2020-12-30 04:02:45  lmlJdiW3kVR2 scratch   
   1 MR1 - Line Follower                       3641b 2020-12-31 17:47:18  T8g7vJ4jYExt python    
   2 MR1 - Wanderer                            2650b 2020-12-31 17:47:49  GzcKr5xPBJrQ python    
   3 MR1 - Connect the Dots                    4375b 2021-01-01 02:11:06  Qm_0zJkWgkGM python    
   4 MR1 - Navigator 1                        13563b 2021-01-04 05:20:15  sUtzpgAokATv python    
   5 Project 3                                  128b 2021-01-02 18:52:18  bGz62LGIzCOl python    
   6 Guard my room 3                           8115b 2020-12-29 17:16:28  kDj0zNTjueJV scratch   
   8 Grab and move                             8949b 2020-12-30 03:49:16  V12C35ra2EdG scratch   
  10 Hi World                                    13b 2021-02-01 04:05:14  50uN1ZaRpHj2 python    
  11 Winner! 6                                 7226b 2020-12-29 22:00:17  cis5eAYFX5bd scratch   
```

### Features

#### Runing code on the hub - command line

The python3 script `run_command.py` can
* list programs stored on the hub
* upload a program to the hub
* start a program on the hub
* stop the program currently running on the hub

Usage:
```shell
python3 run_command.py ls
python3 run_command.py cp myprogram.py 4
python3 run_command.py start 4
python3 run_command.py stop
```

#### Runing code on the hub - GUI

The GUI program hubcontrol can be used to run a program on the hub and display the console output and status while it runs.  

#### Monitoring running hub

The script hubstatus displays the live hub status.

Usage:
```shell
python3 hubstatus.py
```

A window should open displaying the hub status details of the connection type, on-board sensors (yaw, pitch, roll), and the status of the six ports (A-F).  The Hub Gesture value indicates when the hub is tapped, double-tapped, etc.

#### Python scripting

See the [API Design documentation](design.md).


After all packages are confirmed installed you may need to add `export PATH="$HOME/bin:$PATH"`
 
## How To Run Functional Code on the Hub

- Having the firmware installed through PyBricks Code (Pybricks Code -> Follow Instructions)
   - Make sure udev is correctly configured for Web Bluetooth & USB Access
   - Web Bluetooth has to be enabled (only works on Chrome & Edge)
   - Pair the device one time with Bluetooth on PyBricks Code

- Have pybricksdev installed
- Have Bluetooth on
- Use the structure in "hub_light" or "pybricksdev_test" to write code
- Use the command "pybricksdev run ble nameofprogram.py" ===> PyBricksDev has to be installed

- Execute Program : BLE
- Electricity : USB

## Remaining errors

### From basic tests

> AttributeError: 'REPLHub' object has no attribute '_stdout_line_queue'

### From lego-hub-tk method

## Links

- [Project homepage](https://github.com/smr99/lego-hub-tk)
- [Repository](https://github.com/smr99/lego-hub-tk)
- [Issue tracker](https://github.com/smr99/lego-hub-tk/issues)
- [Spike Tools](https://github.com/nutki/spike-tools)
- [Spike Prime info and micropython decompiler](https://github.com/gpdaniels/spike-prime)
- [Spike Prime Extension for VS Code](https://github.com/sanjayseshan/spikeprime-vscode)
- [Pybricks](https://pybricks.com/)
- [Lego Spike Python Coding Tutorials](https://damom73.github.io/lego-spike-tutorials/index.html)
- [rshell (Remote MicroPython Shell)](https://github.com/dhylands/rshell)

### Acknowledgements

This project owes a particular debt of gratitude to several other open source projects.

#### [Remote MicroPython Shell](https://github.com/dhylands/rshell)

Provided the inspiration -- and the core pyudev code -- for USB autodetect.  Additionally, rshell was hugely helpful in exploring the on-board python Read-Evaluate-Print-Loop (REPL) and the hub's file structure.

#### [Spike Tools](https://github.com/nutki/spike-tools)

Provided the core code for decoding the JSON message structure.  The script run_command.py in this toolkit started as a copy of spikejsonrpc from spike tools, with the serial handling code replaced by the comm library.