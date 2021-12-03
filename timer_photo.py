# The code is used to demonstrate the operation of photoresistor function
# and setting up a blinker
# Pin 8 to PH (Green LED)
# Pin 9 to reading the LS photoresistor output

from microbit import *

display.off()  # Turn off on-board LED displays

def handle_blinkpin8():  # Defining a function for blinking the green LED
    sleep(50)
    pin8.write_digital(1)  # Turning on green LED
    sleep(500)  # Wait for 1/2 a second
    pin8.write_digital(0)  # Turning off green LED
    sleep(500)  # Wait for 1/2 a second

while True:

    pin1.write_digital(0)  # Keep Red of RGB off
    sleep(50)
    pin2.write_digital(0)  # Keep Green of RGB off
    sleep(50)
    pin3.write_digital(0)  # Keep Blue of RGB off
    sleep(50)
    pin6.write_digital(1)  # Keep Red LED PL off
    sleep(50)
    if pin9.read_digital():  # If the light level is low
        handle_blinkpin8()  # Call blinking green LED function
    else:  # Otherwise
        pin8.write_digital(0)  # Turn off green LED


