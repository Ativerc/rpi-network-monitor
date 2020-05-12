import subprocess
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

def check_internet():
    try:
        subprocess.check_call(['ping 8.8.8.8 -c1'], shell=True)
    except subprocess.CalledProcessError:
        print("Couldn't ping. Possible Network or Internet Connection Error!")
        publish.single("main/internet/status", payload="NetPing Failure. Network/Internet Error.", qos=1, retain=True)
    else:
        publish.single("main/internet/status", payload="NetPing Success. Network and Internet OK", qos=1, retain=True)
        print("Network and Internet OK!")


def on_connect(client, userdata, flags, rc):
    print("Connected with result code"+str(rc))
    


def on_publish(client, userdata, mid):
    print(f"Message published {client} {userdata} {mid}")

def on_disconnect(client, userdata, rc):
    client.loop_stop()

client = mqtt.Client()
client.on_connect = on_connect
# client.on_message = on_message
client.on_publish = on_publish
client.on_disconnect = on_disconnect


client.connect("localhost", keepalive=60)
client.loop_start()

if __name__ == "__main__":
    check_internet()