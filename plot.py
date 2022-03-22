import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.dates as mdates
import datetime as dt
from matplotlib import style

data_path = os.path.join("data", "result.csv")

style.use('dark_background')

fig, axs = plt.subplots(2, figsize=(10, 10), sharex=True)
fig.suptitle('Temperature and Humidity')

locator = mdates.AutoDateLocator(minticks=12, maxticks=24)
formatter = mdates.DateFormatter('%H:%M:%S')

pause = False


def on_click(_):
    global pause
    pause ^= True


def animate(i):
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

        plt.cla()
        
        axs[0].plot(date, temperature, 'tab:red')
        axs[1].plot(date, humidity, 'tab:blue')
    
    axs[1].xaxis.set_major_locator(locator)
    axs[1].xaxis.set_major_formatter(formatter)
    
    plt.xticks(rotation=40)

    axs[0].set(ylabel='Temperature (°C)')
    axs[1].set(xlabel='Date', ylabel='Humidity (%)')


def show_plot():
    ani = animation.FuncAnimation(fig, animate, interval=2000)

    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()


if __name__ == '__main__':
    show_plot()
