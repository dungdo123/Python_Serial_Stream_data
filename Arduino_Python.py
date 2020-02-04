

import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
#
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# plot class
class AnalogPlot:
    def __init__(self, strPort, maxlen):
        self.ser = serial.Serial(strPort, maxlen)

        self.ax = deque([0.0]*maxlen)
        self.ay = deque([0.0]*maxlen)

        self.maxlen = maxlen
    def addToBuf(self, buf, val):
        if len(buf) < self.maxlen:
            buf.append(val)
        else:
            buf.popleft()
            buf.append(val)
    def add(self, data):
        # assert (len(data)==2)
        self.addToBuf(self.ax, data[0])
        self.addToBuf(self.ay, data[1])
    def update(self, frameNum, a0, a1):
        try:
            line = self.ser.readline()
            data = [float(val) for val in line.split()]
            # if(len(data) == 2):
            self.add(data)
            a0.set_data(range(self.maxlen), self.ax)
            a1.set_data(range(self.maxlen), self.ay)
        except KeyboardInterrupt:
            print('exiting')
        return a0,
    def print_comment(self):
        line = self.ser.readline()
        #print(line)
    def close(self):
        self.ser.flush()
        self.ser.close()
# main() function
def main():

    print('reading from serial port ...' )

    analogPlot = AnalogPlot('COM3', 100)

    print('plotting data...')

    # set up animation
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 100), ylim=(0, 1023))
    a0, = ax.plot([], [])
    a1, = ax.plot([], [])
    anim = animation.FuncAnimation(fig, analogPlot.update,
                                   fargs=(a0, a1),
                                   interval=1000)
    # show plot
    plt.show()
    analogPlot.close()
    print('exiting')
if __name__ == '__main__':
    main()