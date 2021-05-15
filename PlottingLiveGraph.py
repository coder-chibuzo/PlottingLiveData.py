#	By Chibuzo Iyioke (Coder_Chibuzo)

#	In this program, I'm plotting data from a .csv file.
#	If the .csv file is stores it data in real time, the graph will update automatically in real time too



import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')


index = count()

fieldnames = ['TIME','SENSOR 1','SENSOR 2','SENSOR 3','SENSOR 4']


def animate(i):
    data = pd.read_csv('Simulated_Sensor_Data.csv')
    x_axis = data['TIME']
    y1_axis = data['SENSOR 1']
    y2_axis = data['SENSOR 2']
    y3_axis = data['SENSOR 3']
    y4_axis = data['SENSOR 4']
    


    plt.cla()

    plt.plot(x_axis, y1_axis, label='SENSOR 1')
    plt.plot(x_axis, y2_axis, label='SENSOR 2')
    plt.plot(x_axis, y3_axis, label='SENSOR 3')
    plt.plot(x_axis, y4_axis, label='SENSOR 4')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()