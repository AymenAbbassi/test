from typing import Any, Union
import paho.mqtt.client as mqtt
import logger

broker: str = "localhost"
codes = {
    mqtt.MQTT_LOG_ERR: "err",
    mqtt.MQTT_LOG_DEBUG: "info",
    mqtt.MQTT_LOG_INFO: "info",
    mqtt.MQTT_LOG_WARNING: "warn",
    mqtt.MQTT_LOG_NOTICE: "warn"
}

class Publisher:

    def __init__(self, topic: str, name: str) -> None:
        self.topic = topic
        self.name = name
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.info = None

        self.connect()
        self.client.loop_start()

    def __str__(self) -> str:
        return self.name
    
    def connect(self) -> None:
        self.client.on_connect = self.on_connect
        self.client.on_connect_fail = self.on_connect_fail
        self.client.on_disconnect = self.on_disconnect
        self.client.on_pre_connect = self.on_pre_connect
        self.client._reconnect_on_failure  = True

        self.client.connect(broker, keepalive=60)

    def on_connect(self, client, userdata, flags, rc, properties=None) -> None:
        logger.log(f"Publisher {self.name} has connected to broker with code {rc}!", "good")
    def on_connect_fail(self, userdata) -> None:
        logger.log(f"Publisher {self.name} could not connect to broker", "fatal")
    def on_disconnect(self, client, userdata, disconnect_flags, rc, properties=None) -> None:
        logger.log(f"Publisher {self.name} has disconnected from the broker", "fatal")
    def on_pre_connect(self, client, userdata) -> None:
        logger.log(f"Publisher {self.name} is requesting connection to the broker", "info")
    def on_log(self, client, userdata, level, buf) -> None:
        logger.log(f"Log message from MQTT: {buf}", codes[level])
    def publish(self, data: Any) -> None:
        if not isinstance(data, mqtt.PayloadType):
            data = str(data)
        self.info = self.client.publish(self.topic, data)
    def report_loop_times() -> float:
        pass

class Subscriber:
    def __init__(self, topic: str, name: str) -> None:
        self.topic = topic
        self.name = name
        self.client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.msg = None

        self.connect()
        self.client.loop_start()

    def __str__(self) -> str:
        return self.name
    
    def connect(self) -> None:
        self.client.on_connect = self.on_connect
        self.client.on_connect_fail = self.on_connect_fail
        self.client.on_disconnect = self.on_disconnect
        self.client.on_pre_connect = self.on_pre_connect
        self.client.on_message = self.on_message
        self.client._reconnect_on_failure  = True
        self.client.on_subscribe = self.on_subscribe

        self.client.connect(broker, keepalive=60)
        self.client.subscribe(self.topic)

    def on_connect(self, client, userdata, flags, rc, properties=None) -> None:
        logger.log(f"Subscriber {self.name} has connected to broker with code {rc}!", "good")
    def on_connect_fail(self, userdata) -> None:
        logger.log(f"Subscriber {self.name} could not connect to broker", "fatal")
    def on_disconnect(self, userdata) -> None:
        logger.log(f"Subscriber {self.name} has disconnected from the broker", "fatal")
    def on_pre_connect(self, client, userdata) -> None:
        logger.log(f"Subscriber {self.name} is requesting connection to the broker", "info")
    def on_log(self, client, userdata, level, buf) -> None:
        logger.log(f"Log message from MQTT: {buf}", codes[level])
    def on_subscribe(self, client, userdata, mid, reason_code_list, properties=None):
        logger.log(f"Subscribed with errorcode {reason_code_list}")
    def on_message(self, client, userdata, msg: mqtt.MQTTMessage) -> None:
        self.msg = (msg.payload.decode(), msg.timestamp)

    def recieve(self) -> tuple[Union[str, bytes, bytearray, int, float, None], float]:
        return self.msg
    def report_loop_times() -> float:
        pass
