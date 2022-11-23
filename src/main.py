from utime import sleep
from boot import wifi_connect
from user.mqtt import mqtt_connect


if __name__ == "__main__":
    count_down = 0
    wlan = wifi_connect()
    client = mqtt_connect()
    while True:
        if count_down % 10 == 9 and not wlan.isconnected():
            set_leds(False)
            machine.reset()
        if count_down == 59:
            client.ping()
        client.check_msg()
        count_down = ( count_down + 1 ) % 60
        sleep(1)