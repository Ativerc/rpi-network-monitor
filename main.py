import subprocess, time, logging, os

import digitalio
import RPi.GPIO as GPIO
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish


#LED SETUP:
from led_pinouts import redled, blueled, greenled, yellowled
redled.direction = blueled.direction = greenled.direction = yellowled.direction = digitalio.Direction.OUTPUT


def set_status_led(status):
    if status == "CON":
        redled.value = False
        greenled.value = True
    if status == "DCON":
        redled.value = True
        greenled.value = False


def yellowled_blink(timing):
    yellowled.value = True
    time.sleep(timing)
    yellowled.value = False

def blue_led(status):
    if status == "W_CON":
        blueled.value = True
    elif status == "W_DCON":
        blueled.value = False

def check_internet():
    internet_status = 0
    try:
        subprocess.check_call(['ping 8.8.8.8 -c1 -W1'], shell=True)
        yellowled_blink(0.3)
    except subprocess.CalledProcessError as calledexception:
        yellowled_blink(0.3)
        print(f"{calledexception} Couldn't ping. Possible Internal Network or Internet Connection Error!\n\n")
        return calledexception.returncode
    else:
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
            blue_led("W_CON")
            while internet_status == 0: # Normal Mode: Wifi on, net on
                internet_status = check_internet()
                #blink activity led
                set_status_led("CON")
                # publish.single("main/internet/status", payload="NETWORK&INTERNET OK", qos=1, retain=True)
                time.sleep(5)
            else: # Net Failure mode: Wifi on, net off
                internet_status = check_internet()
                #blink activity led
                set_status_led("DCON")
                # publish.single("main/internet/status", payload="NETWORK/INTERNET ERROR", qos=1, retain=True)
                time.sleep(1)
        else:     # Wifi Failure Mode: wifi off, net off
            while check_wifi() == False:
                blue_led("W_DCON")
                check_wifi()
                time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()