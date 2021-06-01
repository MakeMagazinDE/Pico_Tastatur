import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

taste1=digitalio.DigitalInOut(board.GP16)
taste1.switch_to_input(pull=digitalio.Pull.DOWN)
taste2=digitalio.DigitalInOut(board.GP17)
taste2.switch_to_input(pull=digitalio.Pull.DOWN)
taste3=digitalio.DigitalInOut(board.GP18)
taste3.switch_to_input(pull=digitalio.Pull.DOWN)

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