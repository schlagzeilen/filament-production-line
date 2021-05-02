from classes import rot_axis,lin_axis,maschine
from interface import *
from pthat.pthat import Axis
import time
mmaschine = maschine()

# switches = [switch(1), switch(2),switch(3)

def show_responses(axis):
    resps = axis.get_all_responses()

    # Parse the responses
    if resps is not None:
        axis.parse_responses(resps)
    else:
        print("No responses received")


def wait_for_responses(responses_to_check, msg):
    responses = abzug.get_all_responses()
    while not all(x in responses for x in responses_to_check):
        responses = responses + abzug.get_all_responses()

    # Print the responses
    print(msg)
    abzug.parse_responses(responses)

steps_per_rev = 400  #int(input("How many steps per revolution [1600]? ") or "1600")
total_revolutions = 50 #int(input("How many total revolutions [50]? ") or "50")
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

# Setup the X axis
rdc = int(rpm / 10)
abzug.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,  start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)

# wait_for_responses(["RI01CX*", "CI01CX*"], "------- Set X axis command responses -------")

# Y axis
time.sleep(0.1)

yaxis = Axis("Y", command_id=2, serial_device="/dev/ttyS0")
yaxis.debug = True
yaxis.auto_send_command = True

# Setup the X axis
yaxis.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,
               start_ramp=1, finish_ramp=1, ramp_divide=100, ramp_pause=10, enable_line_polarity=1)
# Get the responses - look for both responses to be returned before continuing
# wait_for_responses(["RI02CY*", "CI02CY*"], "------- Set Y axis command responses -------")


# Z axis
time.sleep(0.1)
zaxis = Axis("Z", command_id=3, serial_device="/dev/ttyS0")
zaxis.debug = True
zaxis.auto_send_command = True

# Calculate frequency and pulse count
frequency = zaxis.rpm_to_frequency(rpm=rpm, steps_per_rev=steps_per_rev, round_digits=3)
pulse_count = zaxis.calculate_pulse_count(steps_per_rev, total_revolutions)

# Setup the E axis
rdc = int(rpm / 10)
zaxis.set_axis(frequency=frequency, pulse_count=pulse_count, direction=direction,
               start_ramp=1, finish_ramp=1, ramp_divide=rdc, ramp_pause=10, enable_line_polarity=1)
# Get the responses - look for both responses to be returned before continuing
# wait_for_responses(["RI03CZ*", "CI03CZ*"], "------- Set Z axis command responses -------")

# Start all motors - either axis can be used to call the start all method
time.sleep(0.1)
abzug.start_all()
time.sleep(10)
# wait_for_responses(["RI01SX*", "RI02SY*","RI03SZ*", "CI01SX*", "CI02SY*", "CI03SZ*"], "------- Start all axis command responses -------")



#wicklung  =     rot_axis("Z",command_id=2, serial_device="/dev/ttyS0")
#y_axis =        lin_axis("Y",command_id=3, serial_device="/dev/ttyS0")
