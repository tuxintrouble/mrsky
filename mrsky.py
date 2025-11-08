#Author: Sebastian Stetter, DJ5SE

# MRSKY is allows to connect a regular morse paddle
# to a serial interface (as used with SigBit https://github.com/tuxintrouble/sigbit)
# and generate keyboard strokes as they are used with VBand (https://hamradio.solutions/vband/)

import time
from pynput.keyboard import Key, Controller
from serial import Serial

# Settings

left_key = "ü" #set these to the letters that work for you with VBand
right_key = "+"
port = "/dev/ttyUSB0" #set this to the serial port you use. Make sure you add your user to the group dialout on Linux
interval = 0.005

# Eond of settings

print(f'MRSKY started with left key "{left_key}" and right key "{right_key}" on serial port "{port}".\n Press "Strg+D to exit"\n')
print("MRSKY is allows to connect a regular morse paddle to a serial interface (as used with SigBit https://github.com/tuxintrouble/sigbit) and generate keyboard strokes as they are used with VBand (https://hamradio.solutions/vband/)")
print("Please configure the serial port and key dirctely in the script.")
s = Serial(port)
kbd = Controller()
left_pressed = False
right_pressed = False

if __name__ == "__main__":
    time.sleep(2)
    while True:
        if s.getDSR() and not left_pressed:
            left_pressed = True
            kbd.press(left_key)
        else:
            kbd.release(left_key)
            left_pressed = False
        if s.getCTS() and not right_pressed:
            right_pressed = True
            kbd.press(right_key)
        else:
            kbd.release(right_key)
            right_pressed = False
            
        time.sleep(interval)
