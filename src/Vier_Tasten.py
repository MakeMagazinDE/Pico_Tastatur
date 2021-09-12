######################
# Version passend zur Frontplatte mit 4 Druckschaltern
######################

# 3V3->Taster->GPIO xx
# Pulldown -> Taster gedrückt = Eingang True -> Taste per USB

# taster 0 = GPIO15 = Videoanruf annehmen = STRG+UMSCHALT+A
# taster 1 = GPIO16 = Anruf beenden = STRG+UMSCHALT+B
# taster 2 = GPIO17 = Video = STRG+UMSCHALT+O
# taster 3 = GPIO18 = Mikrofon = STRG+UMSCHALT+M

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Keyboard Objekt
kbd = Keyboard(usb_hid.devices)

# Vier Tasten definieren und GPs setzen
# Achtung auf dem Bord ist zwischen GP17 und 18 ein Masseanschluss!
taster0=digitalio.DigitalInOut(board.GP15)
taster0.switch_to_input(pull=digitalio.Pull.DOWN)
taster1=digitalio.DigitalInOut(board.GP16)
taster1.switch_to_input(pull=digitalio.Pull.DOWN)
taster2=digitalio.DigitalInOut(board.GP17)
taster2.switch_to_input(pull=digitalio.Pull.DOWN)
taster3=digitalio.DigitalInOut(board.GP18)
taster3.switch_to_input(pull=digitalio.Pull.DOWN)

# "Endlose" Schleife
while True:
    if taster0.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.A)
        time.sleep(0.5)
    if taster1.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.B)
        time.sleep(0.5)
    if taster2.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.O)
        time.sleep(0.5)
    if taster3.value:
        kbd.send(Keycode.CONTROL,Keycode.SHIFT,Keycode.M)
        time.sleep(0.5)
