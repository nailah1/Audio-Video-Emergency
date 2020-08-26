#!/usr/bin/python
from __future__ import print_function
import paho.mqtt.client, sys, time, base64

BROKER_ADDRESS = "iqueue.ics.uci.edu"

def on_connect(mosq, obj, rc):
    #mosq.subscribe("$SYS/#", 0)
    print("rc: "+str(rc))

def on_message(mosq, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
    print(obj)
    print("mid: "+str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mosq, obj, level, string):
    print(string)

def publish(pred):
    mqttc = paho.mqtt.client.Client()
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    # Uncomment to enable debug messages
    #mqttc.on_log = on_log
    fileName = "./image.jpg"
    with open(fileName, "rb") as image:
        b64string = base64.b64encode(image.read())
        #print(str(b64string))
        file = '/9j/4AAQSkZJRgABAQEBLAEsAAD/2wBDABALDA4MChAODQ4SERATGCgaGBYWGDEjJR0oOjM9PDkzODdASFxOQERXRTc4UG1RV19iZ2hnPk1xeXBkeFxlZ2P/2wBDARESEhgVGC8aGi9jQjhCY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2NjY2P/wAARCATiBOIDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD0CiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAoopKAFopjyxxjMkiqP9o4qq+rabH/rNQtU/wB6ZR/WgC7RWW/iPRk66pafhKD/ACqM+KdDHXUoPwNAGxRWL/wlmhf9BKH9f8KcPFOhnpqUH4mgDYorMTxFoz9NUtPxlA/nU8eq6fL/AKu/tn/3ZVP9aALlFMSRJBlHVh6g5p1AC0UUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUU13WNSzsFUckk4ArA1HxpotgSv2n7RIP4YBu/Xp+tAHQ0ledX3xJuHythZRxjs0rFj+QxXO3vinWr7Ilv5VU/wxHYP0oA9gur60s13XV1DCP8Apo4X+dYl3440K2yBctOw7RIT+pwK8jd2dizsWY9STnNJQB6JdfEqAZFrp8j+hlcL+gzWVc/ETVpMiGK2hHspY/qf6VyFFAG5P4v16fO7UJFHoihf5Cs+bVdRn/11/cyf70rH+tU6KAFLMxyxJPqTSUUUAFFFFABRRRQAUUUUAOV2Q5Vip9QcVbh1jU4P9TqF0nsJWx/OqVFAG9b+Mtegxi/Zx6SIrf0zWpbfEbU48C4traYeoBU/z/pXG0UAek2vxJsnwLqxmi942Dj9cVtWnjDQrvAW+SNj2lBTH4nivHKKAPfIZ4bhN8MqSKf4kYEVJXgcFxNbPvgmkif+8jFT+lbtj411yzwDdC4QfwzLu/Xr+tAHr9FcJYfEmFsLqFk8Z7vC24fkcfzrptO8R6TqWBbXsRc/wOdrfketAGrRSUtABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQAUUVDdXVvZwmW6mjhjHVnYAUATUlcbq3xDsbfdHp0LXTj+NvlT/ABP6Vxeq+KtX1XKzXTRxH/llF8q/4n8aAPT9U8UaRpeVuLtWlH/LOL5m/Tp'
        #pred = 89
        timestamp = time.time()*1000000
        mqttc.connect(BROKER_ADDRESS, 1883, 60)
        print("connected!")
        mqttc.publish("iot-1/d/801f02ee6789/evt/audioemergency/json",
                      '{"d": {"timestamp": '+ str(int(timestamp)) +
                          ', "value": '+ str(pred) +
                          ', "prio_value": 9, "prio_class": "high",'+
                           '"device": "mqtt://127.0.1.1:1883/scale/applications/MQTTEventImage",'+
                            '"event": "audioemergency", "condition": {"interval": 10}, "schema": "www.schema.org/scale/2.0/sensed_event", "image_file":'+ file+'}}')
        
    # mqttc.publish("iot-1/d/801f02ee6789/evt/audioemergency/json",'{"d": {"timestamp": '+ str(int(timestamp)) + ', "value": '+ str(pred) +', "prio_value": 9, "prio_class": "high", "device": "mqtt://127.0.1.1:1883/scale/applications/MQTTEventImage", "event": "audioemergency", "condition": {"interval": 10}, "schema": "www.schema.org/scale/2.0/sensed_event"}}')

if __name__ == '__main__':
    publish(00)