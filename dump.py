import csv
import math
import os
from plot import show_plot
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
        temp = w.temperature('celsius')
        _ = [i for i in temp]
        new_temp = int(math.ceil(temp['temp']))

        print("temperature:", new_temp)
        print("humidity:", w.humidity)

        data = (new_temp, w.humidity)

        write_csv(data)

        sleep(1.1)


if __name__ == '__main__':
    proc = Process(target=dump_data)

    proc.start()
    show_plot()
    proc.join()
