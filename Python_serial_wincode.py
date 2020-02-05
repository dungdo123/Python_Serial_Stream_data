import sys, serial, argparse
import numpy as np
from time import sleep
import pandas as pd

from collections import  deque

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# plot class
class AnalogPlot:
    def __init__(self, strPort, maxlen):
        self.ser = serial.Serial(strPort, 9600)

        self.temp = deque([0.0]*maxlen)
        self.humd = deque([0.0]*maxlen)
        self.pres = deque([0.0]*maxlen)

        self.maxlen = maxlen

    # add to buf
    def addToBuf(self, buf, val):
        if len(buf) < self.maxlen :
            buf.append(val)
        else:
            buf.pop()
            buf.appendleft(val)
    # Add data
    def add(self, data):
        assert (len(data) == 3)
        self.addToBuf(self.temp, data[0])
        self.addToBuf(self.humd, data[1])
        self.addToBuf(self.pres, data[2])

    # update plot
    def update(self,frameNum, a0, a1, a2):
        try:
            line = self.ser.readline()
            data = [float(val) for val in line.split()]

            if(len(data) == 3):
                self.add(data)
                a0.set_data(range(self.maxlen), self.temp)
                a1.set_data(range(self.maxlen), self.humd)
                a2.set_data(range(self.maxlen), self.pres)

        except KeyboardInterrupt:
            print('exiting')
        return a0,
    # clean up
    def close(self):
        self.ser.flush()
        self.ser.close()
# main function
def main():
    analogPlot = AnalogPlot('COM3', 100)
    print('ploting data...')
    # setup animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 100), ylim=(0, 100))
    ax.set_title("BME280 Data")
    ax.set_xlabel("Time")
    ax.set_ylabel("Sensor Data")

    a0, = ax.plot([], [], label='Temp')
    a1, = ax.plot([], [], label='Humd')
    a2, = ax.plot([], [], label='Press')

    anim = animation.FuncAnimation(fig, analogPlot.update, fargs=(a0, a1, a2), interval=50)

    plt.legend(loc="upper left")
    plt.show()

    analogPlot.close()

if __name__ == '__main__':
    main()
