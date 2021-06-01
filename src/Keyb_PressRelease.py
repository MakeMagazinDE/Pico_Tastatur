# Keyboard send() und send()/release()
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

kbd.send(Keycode.A) # send

# press/release
kbd.press(Keycode.A)
time.sleep(2)
kbd.release(Keycode.A)