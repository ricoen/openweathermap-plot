import csv
import math
import os
import time
import plot
from multiprocessing import Process
from time import sleep
from pyowm import OWM


data_path = os.path.join("data", "result.csv")

owm = OWM('your_api_key')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Lowokwaru, ID')
w = observation.weather


def write_csv(result):
    with open(data_path, 'a') as outfile:
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

        sleep(1.1)
        

if __name__ == '__main__':
    run_dump_data = Process(target=dump_data)

    run_dump_data.start()
    
    plot.show_plot()

    run_dump_data.join()
