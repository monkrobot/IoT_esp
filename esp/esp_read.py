#import serial
#import re
#
#read_data = serial.Serial("COM3", 115200)
#
##while True:
##    print(str(read_data.readline()))
#
#with open('distance710cm.txt', 'w') as distance:
#    for i in range(300):
#        data = str(read_data.readline()).split(' ')
#        try:
#            print(i, data[5])
#            distance.write(data[5] + '\n')
#        except:
#            continue

import pandas as pd
import numpy as np
#import re

#speed_list = []
#
#for i in [5,50,250,500]:
#
#    with open('distance' + str(i) + 'cm.txt', 'r') as file:
#        empty_list = []
#        for line in file:
#            empty_list.append(float(re.sub(r"\n", '', line)))
#        frame = pd.DataFrame({'Speed': empty_list})
#        frame_mean = frame.mean()
#        print(str(frame_mean))
#        #print('frame.mean:', frame_mean)
#        speed_list.append(re.sub(r"[^0-9.]", '', str(frame_mean))[:-2])
#        #print(speed_list[-1])
#
#print('speed_list:\n', speed_list)

#speed_list = {'5': '7.168', '50': '6.7936', '250': '6.749333', '500':'6.4224'}
speed_list = [np.nan] * 100
speed_list[0], speed_list[9], speed_list[49], speed_list[99] = [7.168, 6.7936, 6.749333, 6.4224]

print(speed_list)
s = pd.Series(speed_list)
print('interpolate:\n', s.interpolate())

#import pandas as pd
#import numpy as np
#frame = pd.DataFrame({'1': [0, 1, np.nan, 3, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 10], '2': [0, -1, np.nan, 9, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 116]})
#s = pd.Series([0, -1, np.nan, 9, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 116])
#
#print('s:\n', s)
#print('interpolate:\n', s.interpolate())
#
#print('frame:\n', frame)
#print('interpolate frame:\n', frame.interpolate())