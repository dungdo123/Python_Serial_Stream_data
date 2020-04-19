import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

chicken_refri_data =pd.read_csv("6h.csv", index_col=0)
dataFrame = pd.DataFrame(chicken_refri_data, columns=["number", "Temp", "Humd", "Press"])

temperature = dataFrame.Temp[1:2040]
humidity = dataFrame.Humd[1:2040]
pressure = dataFrame.Press[1:2040]

fig, ax = plt.subplots()
labels = ['12h', '24h', '36h', '48h', '60h', '72h']
def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([340,680,1020,1360,1700,2040])
    ax.set_xticklabels(labels)

# temp
plt.title('Temperature - chicken in refrigerator')
plt.xlim(0, 2040)
plt.ylim(0,10)
set_axis_style(ax, labels)
plt.plot(temperature, color='green')
plt.xlabel("Time")
plt.ylabel("Temperature *C")
plt.show()

# # press
# plt.title('Air Pressure - Chicken in refrigerator')
# plt.xlim(0,2040)
# plt.ylim(1000, 1030)
# set_axis_style(ax, labels)
# plt.plot(pressure, color='red')
# plt.xlabel("Time")
# plt.ylabel("Pressure hPa")
# plt.show()
