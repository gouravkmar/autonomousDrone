from __future__ import print_function
import dronekit_sitl
import dronekit
import time
from dronekit import connect, VehicleMode, LocationGlobalRelative
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)

while not vehicle.is_armable:
    time.sleep(1)
vehicle.mode=VehicleMode("GUIDED")
vehicle.armed=True
while not vehicle.armed:
    time.sleep(1)

vehicle.simple_takeoff(5)
while vehicle.location.global_relative_frame.alt>0:
    
    
    print(vehicle.location.global_relative_frame.alt)
    vehicle.mode=VehicleMode("LAND")
   
    '''if vehicle.location.global_relative_frame.alt>=4:
    
        vehicle.mode=VehicleMode("LAND")
        print(vehicle.location.global_relative_frame.alt)
    
        
    vehicle.mode=VehicleMode("GUIDED")
    vehicle.simple_takeoff(2)
    print(vehicle.location.global_relative_frame.alt)'''
    

