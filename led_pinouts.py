import board
import digitalio


# Activity LED
yellowled = digitalio.DigitalInOut(board.D18)

# Status LED
redled = digitalio.DigitalInOut(board.D17)
greenled = digitalio.DigitalInOut(board.D27)
blueled = digitalio.DigitalInOut(board.D26)


def pinout_printer():
	print("ACTIVITY LED:")
	print(f"  Yellow LED Pin: {yellowled._pin}")
	print("STATUS LED:")
	print(f"  Red LED Pin: {redled._pin}")
	print(f"  Green LED Pin: {greenled._pin}")
	print(f"  Blue LED Pin: {blueled._pin}")

