from classes import rot_axis,lin_axis,maschine
import time

from pthat.pthat import Axis
from interface import *
time.sleep(5)
import time
root = Tk()

steps_per_rev = 400  #int(input("How many steps per revolution [1600]? ") or "1600")
total_revolutions =200  #int(input("How many total revolutions [50]? ") or "50")
rpm = 500 #int(input("How many RPMs [500]? ") or "500")
direct = "F" #input("Direction (Forward = F, Reverse = R) [F]? ") or "F"
direction = 0

abzug = rot_axis("X",command_id=1, serial_device="/dev/ttyS0")
abzug.debug = True
abzug.auto_send_command = True

# print(abzug.axis)

# Calculate frequency and pulse count
frequency = abzug.rpm_to_frequency(rpm=rpm, steps_per_rev=steps_per_rev, round_digits=3)
pulse_count = abzug.calculate_pulse_count(steps_per_rev, total_revolutions)

time.sleep(5)
print("scjaiu")
# Setup the X axis
rdc = int(rpm / 10)
abzug.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,  start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)
#


# # wait_for_responses(["RI01CX*", "CI01CX*"], "------- Set X axis command responses -------")
#
# # Y axis
# time.sleep(0.1)
#
# yaxis = Axis("Y", command_id=2, serial_device="/dev/ttyS0")
# yaxis.debug = True
# yaxis.auto_send_command = True
#
# # Setup the X axis
# yaxis.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,
#                start_ramp=1, finish_ramp=1, ramp_divide=100, ramp_pause=10, enable_line_polarity=1)
# # Get the responses - look for both responses to be returned before continuing
# # wait_for_responses(["RI02CY*", "CI02CY*"], "------- Set Y axis command responses -------")
#
#
# # Z axis
# time.sleep(0.1)
# zaxis = Axis("Z", command_id=3, serial_device="/dev/ttyS0")
# zaxis.debug = True
# zaxis.auto_send_command = True
#
# # Calculate frequency and pulse count
# frequency = zaxis.rpm_to_frequency(rpm=rpm, steps_per_rev=steps_per_rev, round_digits=3)
# pulse_count = zaxis.calculate_pulse_count(steps_per_rev, total_revolutions)
#
# # Setup the E axis
# rdc = int(rpm / 10)
# zaxis.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,
#                start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)
# # Get the responses - look for both responses to be returned before continuing
# # wait_for_responses(["RI03CZ*", "CI03CZ*"], "------- Set Z axis command responses -------")
#
# # Start all motors - either axis can be used to call the start all method
# time.sleep(0.1)
# abzug.start_all()
# time.sleep(10)
# # wait_for_responses(["RI01SX*", "RI02SY*","RI03SZ*", "CI01SX*", "CI02SY*", "CI03SZ*"], "------- Start all axis command responses -------")
#
#
#
# #wicklung  =     rot_axis("Z",command_id=2, serial_device="/dev/ttyS0")
# #y_axis =        lin_axis("Y",command_id=3, serial_device="/dev/ttyS0")
