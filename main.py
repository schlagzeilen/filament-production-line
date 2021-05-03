from classes import rot_axis,lin_axis,maschine
from pthat.pthat import Axis
from interface_classes import window , control_pannel
import time


steps_per_rev = 400  #int(input("How many steps per revolution [1600]? ") or "1600")
total_revolutions =200  #int(input("How many total revolutions [50]? ") or "50")
rpm = 500 #int(input("How many RPMs [500]? ") or "500")
direct = "F" #input("Direction (Forward = F, Reverse = R) [F]? ") or "F"
direction = 0
rdc = int(rpm / 10)

# TODO move that shit into maschine class constructor
abzug = rot_axis("X",command_id=1, serial_device="/dev/ttyS0")
abzug.debug = True
abzug.auto_send_command = True

yaxis = rot_axis("Y", command_id=2, serial_device="/dev/ttyS0")
yaxis.debug = True
yaxis.auto_send_command = True

wicklung = rot_axis("Z", command_id=3, serial_device="/dev/ttyS0")
wicklung.debug = True
wicklung.auto_send_command = True



# print(abzug.axis)

# Calculate frequency and pulse count
frequency = abzug.rpm_to_frequency(rpm=rpm, steps_per_rev=steps_per_rev, round_digits=3)
pulse_count = abzug.calculate_pulse_count(steps_per_rev, total_revolutions)


yaxis.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)
time.sleep(0.5)
abzug.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)
time.sleep(0.5)
wicklung.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)




#INTERFACE STUFF
interface = window()
abzug_pannel = control_pannel(interface.abzug_control, abzug, home=False)
wicklung_pannel = control_pannel(interface.wicklung_control, wicklung)

interface.run() # versteckte root.mainloop() methode
