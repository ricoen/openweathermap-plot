import os
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count
from matplotlib import style


data_path = os.path.join("data", "result.csv")

style.use('fast')

fig, axs = plt.subplots(2, figsize=(10, 10))
fig.suptitle('Temperature and Humidity')

pause = False


def on_click(_):
    global pause
    pause ^= True


def animate(_):
    graph_data = open(data_path, 'r').read()
    lines = graph_data.split('\n')
    
    index = count()
    n = []
    temperature = []
    humidity = []
    
    if not pause:
        for line in lines:
            if len(line) > 1:
                temp, humid = line.split(',')
                
                n.append(next(index))
                temperature.append(float(temp))
                humidity.append(float(humid))

        axs[0].clear()
        axs[1].clear()
        
        axs[0].plot(n, temperature, 'tab:red')
        axs[1].plot(n, humidity, 'tab:blue')
        
        axs[0].set(xlabel='Detik Ke-n (s)', ylabel='Temperature (°C)')
        axs[1].set(xlabel='Detik Ke-n (s)', ylabel='Humidity (%)')


def show_plot():
    _ = animation.FuncAnimation(fig, animate, interval=10)

    fig.canvas.mpl_connect('button_press_event', on_click)
    
    plt.show()


if __name__ == '__main__':
    show_plot()
