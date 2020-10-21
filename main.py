import subprocess, time
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish

def check_internet():
    internet_status = 0
    try:
        subprocess.check_call(['ping 8.8.8.8 -c1 -W1'], shell=True)
    except subprocess.CalledProcessError as calledexception:
        print(f"{calledexception} Couldn't ping. Possible Internal Network or Internet Connection Error!\n\n")
        return calledexception.returncode
        # publish.single("main/internet/status", payload="NetPing Failure. Network/Internet Error.", qos=1, retain=True)
    else:
        # publish.single("main/internet/status", payload="NetPing Success. Network and Internet OK", qos=1, retain=True)
        print("Network and Internet OK!\n")
        internet_status = 0
    return internet_status

# def normal_mode():
#     while True:
#         check_internet()
#         time.sleep(5)

# def net_failure():
#     internet_status = 1
#     while internet_status != 0:
#         internet_status = check_internet()
#         time.sleep(1)
#     return internet_status


if __name__ == "__main__":
    internet_status = check_internet()
    print(f"internet status = {internet_status}")
    while True:
        while internet_status == 0:
            internet_status = check_internet()
            time.sleep(5)
        else:
            internet_status = check_internet()
            time.sleep(1)