from adafruit_circuitplayground import cp
import time

#maxs
MAX = 300
MAX_INDEX = 9

#Sensor Index
def scale(value):
    index = int(value / MAX * MAX_INDEX)
    return min(index, MAX_INDEX)

 #turning off pixels
def clear_pixels():
    for i in range(10):
        cp.pixels[i] = (0,0,0)

#sensor(program)
while True:
    light=cp.light
    index = scale(light)
    clear_pixels()
    cp.pixels[index] = (255,0,0)

    print(light)
    time.sleep(0.5)



