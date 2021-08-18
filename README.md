# rpi-network-monitor

This script/project aims to build a monitoring system for the Network Status and the Internet Status of the network that its running on. 

## More details:
The personal devices we use have their own network diagnostics tools built in. And the apps running on those devices use those tools for a confirmed network
status.

This project aims to do the same for the entire network, where instead of apps, there are people and devices across multiple rooms and floors. 

This project can be helpful for realising that the Internet is down before my devices or someone in my house complains about the outage. The script is
aimed at running on a Raspberry Pi so that I can use LEDs connected to its GPIOs for informing humans around it about the network status. I will add an API so
the machines on my network can use this as well.

## LED Connection PINOUT for RPi:
```
$ python main.py --pinout
ACTIVITY LED:
  Yellow LED Pin: 18
STATUS LED:
  Red LED Pin: 17
  Green LED Pin: 27
  Blue LED Pin: 26
```

## Bugs/Issues/Feature Requests:
See [Issues](https://github.com/Ativerc/rpi-network-monitor/issues)

## To Do:
* [ ] Check which network interface the device is connected to.
* [ ] Rewrite the code to support any network interface its connected to.
* [ ] [Fix]Improve the messages to STDOUT
* [ ] Run as a daemon (Already have figured it out, I want to improve the STDOUT before doing this)
  * [x] Running as a User Service
* [ ] Add logging
* [x] Add a way to print the default pinout, so endusers can easily connect the LEDs and get started.
* [x] Check Wifi Status
* [x] Add STATUS LED Support
* [x] Add WIFI LED Support
* [x] Add ACTIVITY LED Support
* [ ] Add MQTT support (direnv for constants)
* [ ] Fix:
  * [ ] Standardize STATUS CODES to be sent over MQTT
  * [ ] The timings for ACTIVITY LED and STATUS LED
  * [ ] MQTT topic names for network status and device status

