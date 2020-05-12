from gpiozero import DistanceSensor
from time import sleep
import sys

try:
    sensor = DistanceSensor(echo=24, trigger=18, max_distance=1, threshold_distance=0.3)
    # DistanceSensor(echo, trigger)
    while True:
        print 'Distance ', sensor.distance, ' m'
        sleep(2)

except: # catch *all* exceptions
    print sys.exc_info()[0]
