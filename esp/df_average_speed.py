#A list of average speed making
import pandas as pd
import numpy as np
import re

speed_list = []
#Distance measurement step = 5cm
step = 5

for i in [['0-0','0-5','0-50','0-100','0-200','0-300','0-400','0-500'],
          ['50-0','50-5','50-50','50-100','50-200','50-300','50-400','50-500'],
          ['100-0', '100-50', '100-100', '100-200', '100-300', '100-400', '100-500'],
          ['200-0', '200-50', '200-100', '200-200', '200-300', '200-400', '200-500'],
          ['300-0', '300-50', '300-100', '300-200', '300-300', '300-400', '300-500'],
          ['400-0', '400-50', '400-100', '400-200', '400-300', '400-400', '400-500'],
          ['500-0', '500-50', '500-100', '500-200', '500-300', '500-400', '500-500']]:

    line_speed_list = {}
    for distance in i:
        with open('line_' + distance + '.txt', 'r') as file:
            empty_list = []
            for line in file:
                empty_list.append(float(re.sub(r"\n", '', line)))
            frame = pd.DataFrame({'Speed': empty_list})
            frame_mean = frame.mean()
            line_speed_list[distance] = re.sub(r"[^0-9.]", '', str(frame_mean))[:-2]
    speed_list.append(line_speed_list)


import pandas as pd
import numpy as np
speed_column = [np.nan] * 201
speed_column_name = {x: speed_column for x in range(0,1001,5)}
speed_frame = pd.DataFrame(data=speed_column_name)


#print(speed_frame.tail())
for line_dict_speed in speed_list:
    for key in line_dict_speed:
        key_split = key.split('-')
        #print(int(key_split[0]))
        #print('line_dict_speed[key]', line_dict_speed[key])
        speed_frame[int(key_split[0])][int(key_split[1])/step] = line_dict_speed[key]


if __name__ == "__main__":
    print('speed list:', speed_list)
    print(speed_frame[100])
    print(speed_frame)


##Data interpolation
#speed_list[0], speed_list[9], speed_list[49], speed_list[99] = [7.168, 6.7936, 6.749333, 6.4224]
#print(speed_list)
#s = pd.Series(speed_list)
#print('interpolate:\n', s.interpolate())