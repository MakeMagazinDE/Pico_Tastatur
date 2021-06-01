# 3V3->Taster->GPIO xx
# Pulldown -> Taster gedrückt = Eingang True -> Taste per USB

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Keyboard Objekt
kbd = Keyboard(usb_hid.devices)

# Drei Tasten definieren und GPs setzen
taste1=digitalio.DigitalInOut(board.GP16)
taste1.switch_to_input(pull=digitalio.Pull.DOWN)
taste2=digitalio.DigitalInOut(board.GP17)
taste2.switch_to_input(pull=digitalio.Pull.DOWN)
taste3=digitalio.DigitalInOut(board.GP18)
taste3.switch_to_input(pull=digitalio.Pull.DOWN)

# "Endlose" Schleife
while True:
    if taste1.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.K)
        time.sleep(0.2)
    if taste2.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.O)
        time.sleep(0.2)
    if taste3.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.M)
        time.sleep(0.2)