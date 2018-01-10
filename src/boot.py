from machine import UART
import machine
import os
import pycom

uart = UART(0, baudrate=115200)
os.dupterm(uart)

if machine.reset_cause() != machine.SOFT_RESET:
    from network import WLAN

pycom.heartbeat(False)

machine.main('main.py')