import time

import psutil
import platform
my_system = platform.uname()


def convertTime(seconds):

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")



battery = psutil.sensors_battery()

print("Battery percentage : ", battery.percent)
print("Power plugged in : ", battery.power_plugged)


print("Battery left : ", convertTime(battery.secsleft))
time.sleep(60*60)