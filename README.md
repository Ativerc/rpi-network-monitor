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
* Activity LED:
  * RED: GPIO17
  * GREEN: GPIO27
  * BLUE: GPIO26
* Status LED:
  * YELLOW: GPIO18

## Some obstacles:
1. **The RPi is connected to Wifi**:
  * Due to physical shortcomings with my current network, I have to use WiFi. 
  * This helps a bit as well, since I could be coding on my sofa, bed, etc. and RPi can be beside me with the LEDs and I can see how they react to any changes to code.
  * However, the problems imposed by connecting to WiFi are far too many.
    * My WiFi AP does not have any electrical Backup, so my RPi is orphaned if there's a power outage.
    * The code is written in this way to accomodate this default connection to WiFi.
2. **The RPi is powered by a 20,000mAh powerbank**
  * This means, every 24-48 hours I have to switch OFF the RPi in order to charge the powerbank.

## To Do:
* [ ] Check which network interface the device is connected to.
* [ ] Rewrite the code to support any network interface its connected to.
* [ ] [Fix]Improve the messages to STDOUT
* [ ] Run as a daemon (Already have figured it out, I want to improve the STDOUT before doing this)
* [ ] Add logging
* [ ] Add a way to print the default pinout, so endusers can easily connect the LEDs and get started.
* [x] ~~Check Wifi Status~~
* [x] ~~Add STATUS LED Support~~ 
* [x] ~~Add WIFI LED Support~~
* [ ] Add ACTIVITY LED Support
* [ ] Add MQTT support (direnv for constants)
* [ ] Fix:
  * [ ] Standardize STATUS CODES to be sent over MQTT
  * [ ] The timings for ACTIVITY LED and STATUS LED
  * [ ] MQTT topic names for network status and device status

