
from batteryService import BatteryService
import binascii
from network import Bluetooth
import pycom
from pysense import Pysense
from temperatureservice import TemperatureService
import time

bluetooth = Bluetooth()
pysense = Pysense()

def initializeBluetooth():
    bluetooth.set_advertisement(name='Pup Alert Pycom')
    bluetooth.advertise(True)

initializeBluetooth()

tempService = TemperatureService(pysense, bluetooth)
tempService.start()

batteryService = BatteryService(pysense, bluetooth)
batteryService.start()

while True:
    pycom.rgbled(0x1000)
    time.sleep(0.25)
    pycom.rgbled(0x00)
    time.sleep(1.75)
