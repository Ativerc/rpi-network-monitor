'''Checks the device and installs appropriate libs
Mostly to prevent installation of GPIO libs of RPi'''
import subprocess
import sys


all_platforms = [
    "Adafruit-PlatformDetect"
]

rpi_only = [
    "digitalio"
]

non_rpi = [
    "notify-py"
]

def install(packages):
    '''Install a given list of packages'''
    for package in packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        # Apparently, a kitten dies whenever somebody uses import pip in their code
        # https://pip.pypa.io/en/latest/user_guide/#using-pip-from-your-program



if __name__ == '__main__':
    install(all_platforms)
    from adafruit_platformdetect import Detector
    det = Detector()
    chip_id = det.chip.id
    board_id = det.board.id
    chip_id_msg = 'GENERIC_X86'
    board_id_msg = 'GENERIC_LINUX_PC'
    if chip_id == chip_id_msg and board_id == board_id_msg:
        #TODO set WORK_ENV == GENERIC_LINUX_PC
        #Notification libs
        print(f"DETECTED: Chip:{chip_id_msg} Board:{board_id_msg}")
        install(non_rpi)
    else:
        #TODO set WORK_ENV == RPI
        install(rpi_only)
