from __future__ import print_function
from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil # Needed for command message definitions
import time
import numpy as np
from pyquaternion import Quaternion
from PiVideoStream_final_final import PiVideoStream
from picamera.array import PiRGBArray
from picamera import PiCamera
import argparse
import imutils
import cv2
import sys
from datetime import datetime, timedelta
from PID import PIDController


parser = argparse.ArgumentParser(description='Commands vehicle using vehicle.simple_goto.')
parser.add_argument('--connect', 
                   help="Vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect

# Connect to the physical UAV or to the simulator on the network
if not connection_string:
    print ('Connecting to pixhawk.')
    vehicle = connect('/dev/serial0', baud=57600, wait_ready= True)
else:
    print ('Connecting to vehicle on: %s' % connection_string)
    vehicle = connect(connection_string, wait_ready=True)



def set_attitude (pitch, roll, yaw, thrust):
    # The parameters are passed in degrees
    # Convert degrees to radians
    #degrees = (2*np.pi)/360
    yaw = np.radians(yaw)
    pitch = np.radians(pitch)
    roll = np.radians(roll) 
    
    # Now calculate the quaternion in preparation to command the change in attitude
    # q for yaw is rotation about z axis
    qyaw = Quaternion (axis = [0, 0, 1], angle = yaw )
    qpitch = Quaternion (axis = [0, 1, 0], angle = pitch )
    qroll = Quaternion (axis = [1, 0, 0], angle = roll )

    # We have components, now to combine them into one quaternion
    q = qyaw * qpitch * qroll
    
    a = q.elements
    
    rollRate = (roll * 5)
    yawRate = (yaw * 0.5)
    #pitchRate = abs(pitch * 1)
    # print " Yaw: ",yaw, " Yaw Rate: ", yawRate, " Roll: ",roll, "Roll Rate: ", rollRate, " Pitch: ", pitch, " Thrust: ",thrust
   
    msg = vehicle.message_factory.set_attitude_target_encode(
    0,
    0,                #target system
    0,                #target component
    0b0000000,       #type mask
    [a[0],a[1],a[2],a[3]],        #q
    rollRate,                #body roll rate
    0.5,                #body pitch rate
    yawRate,                #body yaw rate
    thrust)                #thrust
    
    vehicle.send_mavlink(msg)
