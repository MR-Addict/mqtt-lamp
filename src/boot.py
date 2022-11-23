import network
from utime import sleep
from secret import ssid, password


def wifi_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while not wlan.isconnected():
        wlan.connect(ssid, password)
        print(f"Connecting to {ssid}...")
        sleep(10)
    ip = wlan.ifconfig()[0]
    print(f'IP Address {ip}')
    return wlan
