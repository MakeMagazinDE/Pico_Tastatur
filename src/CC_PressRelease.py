# CC_PressRelease.py
# Consumer Control Mediensteuerung
import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

cc = ConsumerControl(usb_hid.devices)

# 2 Sekunden Lautstärke erhöhencc.press(ConsumerControlCode.VOLUME_INCREMENT)
time.sleep(1)
cc.release()

time.sleep(2)

# 2 Sekunden Lautstärke verringerncc.press(ConsumerControlCode.VOLUME_DECREMENT)
time.sleep(1)
cc.release()