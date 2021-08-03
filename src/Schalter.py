# 3V3->Taster->GPIO 16
# Pulldown -> Schalter geschlossen = Eingang True

import board
import digitalio
import time

schalter = digitalio.DigitalInOut(board.GP16)      # GPIO 16
schalter.switch_to_input(pull=digitalio.Pull.DOWN) # int. Pulldown

# Schalterstellung bei Programmstart?
s_state = schalter.value

# Schalter geschlossen gibt True am Eingang!
while True:
    if schalter.value != s_state:
        s_state = schalter.value
        if schalter.value:
            print("An")
        else:
            print("Aus")
    time.sleep(0.2)