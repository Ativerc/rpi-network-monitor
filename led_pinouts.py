import board
import digitalio

# Status LED
redled = digitalio.DigitalInOut(board.D17)
greenled = digitalio.DigitalInOut(board.D27)
blueled = digitalio.DigitalInOut(board.D26)

# Activity LED 
yellowled = digitalio.DigitalInOut(board.D18)

# How do i print these pinouts over CLI for the user?
