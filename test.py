from bluepy.btle import *
import struct


def ble_micro_handle():
    scanner = Scanner(0)
    devices = scanner.scan(3)
    for dev in devices:
        print ("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))

        for (adtype, desc, value) in dev.getScanData():
            print ("  %s = %s" % (desc, value))
            num_ble = len(devices)
            print (num_ble)
    if num_ble==0:
        return None
    ble_mic = []
    char_sensor = 0
    non_sensor = 0
    led_char = Characteristic
    mic_char = Characteristic
    led_handle =0

    for i in range(num_ble):
        try:
            devices[i].getScanData()
            ble_mic.append(Peripheral())
            ble_mic[char_sensor].connect(devices[i].addr,devices[i].addrType)
            char_sensor = char_sensor + 1
            print ("Connected %s device with addr %s " % (char_sensor, devices[i].addr))
        except:
            non_sensor = non_sensor + 1
        try:
            for i in range(char_sensor):
                services = ble_mic[i].getServices()
                characteristics = ble_mic[i].getCharacteristics()
                for k in characteristics:
                    print (k)
                    if k.uuid=="2a6e":
                        #print "temp"
                        # print k.uuid
                        # print k.peripheral
                        value = struct.unpack('<H',k.read())
                        value = value[0] / 100
                        print (value)
                    if k.uuid == "2a6f":
                        print ("humidity")
                        value = struct.unpack('<H',k.read())
                        value = value[0] / 100
                        print (value)
        except:
            return None

ble_micro_handle()
