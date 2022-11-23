config = {
    "mqtt": {
        "client_id": "Pi Pico W",
        "broker": "mqtt_broker_ip",
        "username": "mqtt_username",
        "password": "mqtt_password",
        "pub_topic": "home/device/desktop_lamp/status",
        "sub_topic": "home/device/desktop_lamp/control",
        "will_msg": '{"status":"off","mode":"Bright"}',
        "will_topic": "home/device/desktop_lamp/status",
    },
    "leds": {
        "mode": {
            "Bright": 0x6,
            "Warm": 0x5,
            "Night": 0x4,
        }
    }
}
