from pthat.pthat import Axis
from gpiozero import Button
import datetime


class rot_axis(Axis):

    def __init__(self, axis, command_type="I", command_id=0, serial_device="/dev/ttyS0", baud_rate=115200,
                 test_mode=False):
        """
        Constructor
        """
        super().__init__(axis,command_type=command_type, command_id=command_id, serial_device=serial_device,
                         baud_rate=baud_rate, test_mode=test_mode)

        self.__pulling_speed_ist= float()
        self.__pulling_speed_soll= float()

        self.__rpm_ist= float()
        self.__rpm_soll = float()

        self.__durchmesser_rolle = float()
        self.__rotationcount= int()


    #--------------------getters
    #--------------------setters



class lin_axis(Axis):
    def __init__(self, axis, command_type="I", command_id=0, serial_device="/dev/ttyS0", baud_rate=115200,
                 test_mode=False):
        """
        Constructor
        """
        super().__init__(axis,command_type=command_type, command_id=command_id, serial_device=serial_device,
                         baud_rate=baud_rate, test_mode=test_mode)
        self.__position_ist = float()
        self.__position_soll =float()

        self.__linear_speed_ist = float()
        self.__linear_speed_soll = float()

        self.__max_pos = float()
        self.__min_pos = float()

    #--------------------getters
    #--------------------setters

class switch(Button):
    __soll = int() #TODO konstruktor aus der KLasse hier herein kopieren, mit super consturctor von der elternklasse aufrufen, zusätzlichen Attribut hinzufügen

class maschine():
    def __init__(durchmesser_soll=1.75,buffer_hight_soll=0.5):
        self.__durchmesser_ist = float()
        self.__durchmesser_soll = float()
        self.__durchmesser_mean = float()
        self.__filament_length_soll =float()
        self.__startzeit = datetime.datetime.now()
        self.__layer = int()
        self.__buffer_hight_ist =float()
        self.__buffer_hight_soll = float()




    #--------------------getters
    #--------------------setters
