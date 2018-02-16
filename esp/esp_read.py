import serial
import re

read_data = serial.Serial("COM3", 115200)

#while True:
#    print(str(read_data.readline()))

with open('distance710cm.txt', 'w') as distance:
    for i in range(300):
        data = str(read_data.readline()).split(' ')
        try:
            print(i, data[5])
            distance.write(data[5] + '\n')
        except:
            continue