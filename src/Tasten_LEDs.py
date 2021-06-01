# Erweiterter Code für x Tasten und x Status LEDs
# 3V3->Taster->GPIO
# Pulldown -> Taster gedrückt = Eingang True
# 3.3V -> Widerstand 330R -> LED -> GPIO

import sys
import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

# Auflistung der GPIOs und zugehörige Tastencodes
tasten = [
    # LED GPIO ,    Tasten GPIO,    Keycodes
    [board.GP19,    board.GP16,     [Keycode.ALT,Keycode.LEFT_CONTROL,Keycode.K]],
    [board.GP21,    board.GP17,     [Keycode.ALT,Keycode.LEFT_CONTROL,Keycode.O]],
    [board.GP20,    board.GP18,     [Keycode.ALT,Keycode.LEFT_CONTROL,Keycode.M]],
    ]

# Buttons merken und initialisieren 
for t in tasten:
    t.append(digitalio.DigitalInOut(t[0]))          # LED Objekt an Array
    t.append(digitalio.DigitalInOut(t[1]))          # Tastenobjekt an Array
    t[3].switch_to_output(1)                        # LED  GP auf Ausgang
    t[4].switch_to_input(pull=digitalio.Pull.DOWN)  # Tasten GP auf Eingang/Pulldown
    t[3].value=False
    if t[4].value:      # Bei irgendeiner gehaltenen Taste Exit (Sicherheit)
        print("Exit!")
        sys.exit()


while True:
    for t in tasten:         # Array durchgehen
        if t[4].value:       # t[4] ist der aktuelle Taster
            kbd.send(*t[2])  # Keycode(s) aus t[2] entpacken(*)
            t[3].value^=True
            time.sleep(0.4)  # Entprellen
