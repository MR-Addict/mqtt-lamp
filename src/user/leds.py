from machine import Pin
from .config import config

leds = [
    Pin(20, Pin.OUT),
    Pin(19, Pin.OUT),
    Pin(18, Pin.OUT)
]


def set_leds(mask = 0x6):
    for i in range(3):
        output = mask >> i & 0x1
        leds[i].value(output)


def get_leds():
    mask = 0x0
    for i in range(3):
        mask = leds[i].value() << i | mask
    if mask == 0x0:
        return "off", "Bright"
    else:
        mode = [key for key, value in config["leds"]["mode"].items() if value == mask]
        if not mode:
            return "on", "Bright"
        else:
            return "on", mode[0]
