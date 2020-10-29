import subprocess, time, logging

import board
import digitalio
import RPi.GPIO as GPIO
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish


#LED SETUP:
activity_led = digitalio.DigitalInOut(board.D18)
activity_led.direction = digitalio.Direction.OUTPUT
redled = digitalio.DigitalInOut(board.D17)
greenled = digitalio.DigitalInOut(board.D27)
blueled = digitalio.DigitalInOut(board.D22)
redled.direction = blueled.direction = greenled.direction = digitalio.Direction.OUTPUT


def set_status_led(status):
    if status == "CON":
        redled.value = False
        greenled.value = True
    if status == "DCON":
        redled.value = True
        greenled.value = False


def activity_ledd():
    pass


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

def check_wifi(): #Adding this thing sets up check_internet loop for failure. 
# Coz what happens when wifi is connected now and then check_internet starts and then wifi is disconnected again.
# Poor check_internet loop will never exit.
# Unless I call check_wifi from within check_internet
    ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    try:
        output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
        print(output)
    except subprocess.CalledProcessError:
        print("No Wireless Networks Connected!")
        return False
    return True

def check_which_interface():
    pass



if __name__ == "__main__":
    try:
        internet_status = check_internet()
        print(f"internet status = {internet_status}")
        while check_wifi() == True: # Wifi Check: ;Net: Unknown
            while internet_status == 0: # Normal Mode: Wifi on, net on
                internet_status = check_internet()
                #blink activity led
                set_status_led("CON")
                time.sleep(5)
            else: # Net Failure mode: Wifi on, net off
                internet_status = check_internet()
                #blink activity led
                set_status_led("DCON")
                time.sleep(1)
        else:     # Wifi Failure Mode: wifi off, net off
            while check_wifi() == False:
                check_wifi()
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()