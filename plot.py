import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import datetime as dt
from matplotlib import style

data_path = os.path.join("data", "result.csv")

style.use('dark_background')

fig, axs = plt.subplots(2, figsize=(10, 10))
fig.suptitle('Temperature and Humidity')

pause = False


def on_click(_):
    global pause
    pause ^= True


def animate(_):
    graph_data = open(data_path, 'r').read()
    lines = graph_data.split('\n')
    
    date = []
    temperature = []
    humidity = []
    
    if not pause:
        for line in lines:
            if len(line) > 1:
                time, temp, humid = line.split(',')
                time = dt.datetime.strptime(time, '%H:%M:%S')

                date.append(time)
                temperature.append(float(temp))
                humidity.append(float(humid))

        axs[0].clear()
        axs[1].clear()
        
        axs[0].plot(date, temperature, 'tab:red')
        axs[1].plot(date, humidity, 'tab:blue')
        
        axs[0].set(xlabel='Date', ylabel='Temperature (°C)')
        axs[1].set(xlabel='Date', ylabel='Humidity (%)')


def show_plot():
    _ = animation.FuncAnimation(fig, animate, interval=200)

    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()


if __name__ == '__main__':
    show_plot()
