from pthat.pthat import Axis
from gpiozero import Button
import datetime

print("basinga")
class rot_axis(Axis):
    pulling_speed_ist= float()
    pulling_speed_soll= float()

    rpm_ist= float()
    rpm_soll = float()

    durchmesser_rolle = float()
    rotationcount= int()

    #--------------------getters
    #--------------------setters



class lin_axis(Axis):
    position_ist = float()
    position_soll =float()

    linear_speed_ist = float()
    linear_speed_soll = float()

    max_pos = float()
    min_pos = float()
    #--------------------getters
    #--------------------setters

class switch(Button):
    soll = int()

class maschine():
    durchmesser_ist = float()
    durchmesser_soll = float()
    durchmesser_mean = float()

    startzeit = datetime.datetime.now()
    layer = int()
    filament_length_soll =float()
    buffer_hight_ist =float()
    buffer_hight_soll = float()

    switches = [switch(1), switch(2),switch(3)]

    abzug =         rot_axis("X",command_id=1, serial_device="/dev/ttyS0")
    wicklung  =     rot_axis("Z",command_id=2, serial_device="/dev/ttyS0")
    y_axis =        lin_axis("Y",command_id=3, serial_device="/dev/ttyS0")

    #--------------------getters
    #--------------------setters
