from pthat.pthat import Axis
from gpiozero import Button
import datetime

# Die maschine wird zwei rotatorische Achsen haben 1. die wickllung und zweitens dem Abzug.
# die KLasse rot_achses dient in erster Linie der Strukturierung des Codes
#sie erbt von der Axis klasse der Pthat API und soll dazu dienen einzelne parameter und methoden unabhängig von der Version des pthat moduls zu ändernund funktionalität hinzuzufügen

class rot_axis(Axis):
    #--------------------constructor
    def __init__(self, axis, command_type="I", command_id=0, serial_device="/dev/ttyS0", baud_rate=115200,
                 test_mode=False):

        # weitergeben der Parameter an den Konstruktor der Elternklasse
        super().__init__(axis,command_type=command_type, command_id=command_id, serial_device=serial_device,
                         baud_rate=baud_rate, test_mode=test_mode)

        # erstellen der Attribute der Klasse. der doppelte Unterstrich macht die Attribute privat
        self.__pulling_speed_ist= float()
        self.__pulling_speed_soll= float()

        self.__rpm_ist= float()
        self.__rpm_soll = float()

        self.__durchmesser_rolle = float()
        self.__rotationcount= int()

        self.__control_state =False #soll am ende aussagen ob die Regelung an oder aus ist.
    # kontext es werden getter und setter funktionen genutzt um die Variablen vor ungewolltem ändern zu schützen
    #--------------------getters
    def get_pulling_speed_ist():
        return self.__pulling_speed_ist
    def get_pulling_speed_soll():
        return self.__pulling_speed_soll
    def get_rpm_ist():
        return self.__rpm_ist
    def get_rpm_soll ():
        return self.__rpm_soll
    def get_durchmesser_rolle():
        return self.__durchmesser_rolle
    def get_rotationcount():
        return self.__rotationcount
    def get_control_state():
        return self.control_state
    #--------------------setters
    def set_pulling_speed_ist(v):
        self.__pulling_speed_ist=v
    def set_pulling_speed_soll(v):
        self.__pulling_speed_soll=v
    def set_rpm_ist(v):
        self.__rpm_ist=v
    def set_rpm_soll (v):
        self.__rpm_soll=v
    def set_durchmesser_rolle(v):
        self.__durchmesser_rolle=v
    def set_rotationcount(v):
        self.__rotationcount=v
    def set_control_state(v):
        self.control_state

    #--------------------methodes
    #wird aufgerufen in den controll pannels der interface klasse
    def increment_speed(self,rpm_delta):
        #die funktion übersetzt, was ein inkremnt von delta für die frequentz bedeutet
        new_frequency = self.frequency + self.rpm_to_frequency(rpm_delta,200,3)
        self.change_speed(new_frequency)



class lin_axis(Axis):
    def __init__(self, axis, command_type="I", command_id=0, serial_device="/dev/ttyS0", baud_rate=115200,
                 test_mode=False):

        super().__init__(axis,command_type=command_type, command_id=command_id, serial_device=serial_device,
                         baud_rate=baud_rate, test_mode=test_mode)

        self.__position_ist = float()
        self.__position_soll =float()

        self.__linear_speed_ist = float()
        self.__linear_speed_soll = float()

        self.__max_pos = float()
        self.__min_pos = float()



    #--------------------getters
    def get_position_ist ():
        return self.__position_ist
    def get_position_soll():
        return self.__position_sol
    def get_linear_speed_ist ():
        return self.__linear_speed_ist
    def get_linear_speed_soll ():
        return self.__linear_speed_soll
    def get_max_pos ():
        return self.__max_pos
    def get_min_pos ():
        return self.__min_pos


    #--------------------setters
    def set_position_ist ():
        self.__position_ist = v
    def set_position_soll():
        self.__position_soll =v
    def set_linear_speed_ist ():
        self.__linear_speed_ist = v
    def set_linear_speed_soll ():
        self.__linear_speed_soll = v
    def set_max_pos ():
        self.__max_pos = v
    def set_min_pos ():
        self.__min_pos = v



class switch(Button):
    __soll = int() #TODO konstruktor aus der KLasse hier herein kopieren, mit super consturctor von der elternklasse aufrufen, zusätzlichen Attribut hinzufügen

#von dieser Klasse wird es nur eine Instanz geben. Sie dient lediglich der Strukturierung der Attribute und Methoden des Gesamtsystems
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
    def get_durchmesser_ist():
        return self.__durchmesser_ist
    def get_durchmesser_soll():
        return self.__durchmesser_soll
    def get_durchmesser_mean():
        return self.__durchmesser_mean
    def get_filament_length_soll():
        return self.__filament_length_soll
    def get_startzeit():
        return self.__startzeit
    def get_layer():
        return self.__layer
    def get_buffer_hight_ist():
        return self.__buffer_hight_ist
    def get_buffer_hight_soll():
        return self.__buffer_hight_soll

    #--------------------setters
    def set_durchmesser_ist(v):
        self.__durchmesser_ist=v
    def set_durchmesser_soll(v):
        self.__durchmesser_soll=v
    def set_durchmesser_mean(v):
        self.__durchmesser_mean=v
    def set_filament_length_soll(v):
        self.__filament_length_soll=v
    def set_startzeit(v):
        self.__startzeit=v
    def set_layer(v):
        self.__layer=v
    def set_buffer_hight_ist(v):
        self.__buffer_hight_ist=v
    def set_buffer_hight_soll(v):
        self.__buffer_hight_soll=v
