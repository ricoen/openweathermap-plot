import os
import csv
import math
from time import sleep
from pyowm import OWM
from multiprocessing import Process

data_path = os.path.join("data", "result.csv")

owm = OWM('your_api_key')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Lowokwaru, ID')
w = observation.weather

def write_csv(data):
    with open(data_path, 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)
        
def run_plot():
    import plot
    
def run_plot_thread():
    Process(target=run_plot).start()
    
if __name__ == '__main__':
    run_plot_thread()

    while(1):
        temp = w.temperature('celsius')
        [i for i in temp]
        new_temp = int(math.ceil(temp['temp']))

        print("temperature:", new_temp)
        print("humidity:", w.humidity)
        
        data = (new_temp, w.humidity)
        
        write_csv(data)

        sleep(1.1)
