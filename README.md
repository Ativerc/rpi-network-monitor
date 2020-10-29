# my-ncsi

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
  * BLUE: GPIO22 [Not used. But connected just in case.]
* Status LED:
  * YELLOW: GPIO18

## To Do:
* [x] ~~Check Wifi Status~~
* [x] ~~Add STATUS LED Support~~
* [ ] Check which network interface the device is connected to.  
* [ ] Add ACTIVITY LED Support

## About the name:
The name comes from TV show which is famous for "Enhance! Enhance! Enchance!" phrase. Kidding! The name comes from Microsoft's 
Network Connection Status Indicator tool for Windows based systems. Some details about Microsoft's NCSI can be found [here](https://support.microsoft.com/en-us/help/4494446/an-internet-explorer-or-edge-window-opens-when-your-computer-connects)
