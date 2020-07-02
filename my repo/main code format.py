from __future__ import print_function
import dronekit_sitl
import dronekit
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)   #connect via serial port of pi,put adress of pi(com10 for pc)

while not vehicle.is_armable:
    time.sleep(1)
vehicle.mode=VehicleMode("GUIDED")
#put some code to wait before arming



#finally get the message to arm,so arming
vehicle.armed=True
while not vehicle.armed:
    time.sleep(1)

    
#some code again to varify that everyone is armed
    
vehicle.simple_takeoff(5)

#some code to varify that everyone is at some height

while vehicle.location.global_relative_frame.alt<2:
    print(vehicle.location.global_relative_frame.alt)
if vehicle.location.global_relative_frame.alt>=2:
    
    vehicle.mode=VehicleMode("LAND")
    while(vehicle.location.global_relative_frame.alt>0):
        print(vehicle.location.global_relative_frame.alt)


    
