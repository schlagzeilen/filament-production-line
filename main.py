from classes import rot_axis,lin_axis,maschine
from interface import *
mmaschine = maschine()

switches = [switch(1), switch(2),switch(3)]

abzug =         rot_axis("X",command_id=1, serial_device="/dev/ttyS0")
wicklung  =     rot_axis("Z",command_id=2, serial_device="/dev/ttyS0")
y_axis =        lin_axis("Y",command_id=3, serial_device="/dev/ttyS0")
