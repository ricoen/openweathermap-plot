import os
import csv
import math
from time import sleep
from pyowm import OWM
from multiprocessing import Process


data_path = os.path.join("data", "result.csv")

owm = OWM('05ddbbab284feea8ff74da8a292e9c36')
mgr = owm.weather_manager()

observation = mgr.weather_at_place('Lowokwaru, ID')
w = observation.weather

def write_csv(data):
    with open(data_path, 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)
        
def run_plot():
    import plot
    
def start_plot_thread(p):
    p.start()
    
def join_plot_thread(p):
    p.join()
    
if __name__ == '__main__':
    p = Process(target=run_plot)
    start_plot_thread(p)
    
    while(1):
        temp = w.temperature('celsius')
        [i for i in temp]
        new_temp = int(math.ceil(temp['temp']))

        print("temperature:", new_temp)
        print("humidity:", w.humidity)
        
        data = (new_temp, w.humidity)
        
        write_csv(data)

        sleep(1.1)

    join_plot_thread(p)
