# Beliebig viele Tasten
# 3V3->Taster->GPIO
# Pulldown -> Taster gedrückt = Eingang True

import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Auflistung der GPIOs und zugehörige Tastencodes
tasten = [
    # GPIO      ,   Tastencodes
    [board.GP16,    [Keycode.CONTROL, Keycode.S]],
    [board.GP17,    [Keycode.B]],
    [board.GP18,    [Keycode.SHIFT,Keycode.C]],
    # u.s.w.
    ]

# Buttons merken und initialisieren 
for t in tasten:
    t.append(digitalio.DigitalInOut(t[0]))          # Tastenobjekt an Array
    t[2].switch_to_input(pull=digitalio.Pull.DOWN)  # Tasten GP auf Eingang/Pulldown


while True:
    for t in tasten:         # Array durchgehen
        if t[2].value:       # t[2] ist der aktuelle Taster
            kbd.send(*t[1])  # Keycode(s) aus t[1] entpacken(*)
            time.sleep(0.4)  # Entprellen
