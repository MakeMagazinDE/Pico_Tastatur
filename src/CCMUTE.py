# Consumer Control Mediensteuerung
import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)
cc.send(ConsumerControlCode.MUTE)