#Read data from ESP-32

import serial
import time

start = time.time()

read_data = serial.Serial("COM3", 115200)
num_data = 100
#while True:
#    print(str(read_data.readline()))

with open('line_0-0.txt', 'w') as distance:
    i = 0
    for _ in range(num_data*2):
        data = str(read_data.readline()).split(' ')
        try:
            print(i, data[5])
            distance.write(data[5] + '\n')
            i += 1
        except:
            continue

print('time:', time.time() - start)