import csv
import math
import os
import time
import plot
from multiprocessing import Process
from time import sleep
from pyowm import OWM


data_path = os.path.join("data", "result.csv")

owm = OWM('df1c3f5c317429743ab4b25c5acb196d')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Lowokwaru, ID')
w = observation.weather


def write_csv(result):
    with open(data_path, 'a', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(result)


def dump_data():
    while 1:
        now = time.strftime('%H:%M:%S')
        temp = w.temperature('celsius')
        _ = [i for i in temp]
        new_temp = int(math.ceil(temp['temp']))

        print("temperature:", new_temp)
        print("humidity:", w.humidity)

        data = (now, new_temp, w.humidity)

        write_csv(data)

        sleep(1.98)
        

if __name__ == '__main__':
    run_dump_data = Process(target=dump_data)

    run_dump_data.start()
    
    plot.show_plot()

    run_dump_data.join()
