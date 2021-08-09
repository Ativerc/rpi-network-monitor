import board
import digitalio


# Activity LED
yellowled = digitalio.DigitalInOut(board.D18)

# Status LED
redled = digitalio.DigitalInOut(board.D17)
greenled = digitalio.DigitalInOut(board.D27)
blueled = digitalio.DigitalInOut(board.D26)


def pinout_printer():
	print(f"ACTIVITY LED PIN: {yellowled._pin}")
	print(f"RED LED PIN: {redled._pin}")
	print(f"GREEN LED PIN: {greenled._pin}")
	print(f"BLUE LED PIN: {blueled._pin}")

