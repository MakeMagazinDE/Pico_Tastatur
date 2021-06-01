# Maus.py
# Mausbewegung bei Tastendruckimport usb_hid
from adafruit_hid.mouse import Mouse

import board
import digitalio
import time

m = Mouse(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP16)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
    # 3. Parameter ist Scrollrad   
    m.move(-10, -10, 0)
time.sleep(0.2) 