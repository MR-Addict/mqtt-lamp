import ujson
from utime import sleep
from umqtt.simple import MQTTClient

from .config import config
from .leds import set_leds, get_leds


def mqtt_update_sensor():
    status, mode = get_leds()
    pub_topic = str.encode(config["mqtt"]["pub_topic"])
    msg = str.encode(f'{{"status":"{status}","mode":"{mode}"}}')
    client.publish(pub_topic, msg, True)


def mqtt_sub_callback(topic, msg):
    msg = ujson.loads(msg.decode("utf-8"))
    if "status" in msg and msg["status"] == "off":
        set_leds(0x0)
    elif "status" in msg and msg["status"] == "on":
        mode = 0x6
        if "mode" in msg and msg["mode"] in config["leds"]["mode"]:
            mode = config["leds"]["mode"][msg["mode"]]
        set_leds(mode)
    mqtt_update_sensor()


def mqtt_connect():
    sub_topic = str.encode(config["mqtt"]["sub_topic"])
    client_id = str.encode(config["mqtt"]["client_id"])
    broker = str.encode(config["mqtt"]["broker"])
    username = str.encode(config["mqtt"]["username"])
    password = str.encode(config["mqtt"]["password"])
    will_topic = str.encode(config["mqtt"]["will_topic"])
    will_msg = str.encode(config["mqtt"]["will_msg"])

    global client
    reconnect = True
    client = MQTTClient(client_id, broker, 1883, username, password, 60)
    client.set_callback(mqtt_sub_callback)
    client.set_last_will(will_topic, will_msg, True)
    while reconnect:
        try:
            client.connect()
            reconnect = False
        except:
            print(f'Connecting to {broker.decode("utf-8")}...')
            sleep(10)
    print(f'Connected to {broker.decode("utf-8")}')
    client.subscribe(sub_topic)
    mqtt_update_sensor()
    return client
