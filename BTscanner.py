# -*- coding: utf-8 -*-

# prints already known devices and new discoverable devices.

# use python -m pip install pybluez
import bluetooth

print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(lookup_names = True)

print ("found %d devices" % len(nearby_devices))

for name, addr in nearby_devices:
     print (" %s - %s" % (addr, name))