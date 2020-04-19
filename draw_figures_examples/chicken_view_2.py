import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# # remove [] characters
# with open('6h.csv', 'r') as infile, open('60h_a.txt', 'w') as outfile:
#     data = infile.read()
#     data = data.replace("]", "")
#     outfile.write(data)

# with open('60h_a.txt', 'r') as infile, open('60h.csv', 'w') as outfile:
#     data = infile.read()
#     outfile.write(data)

chicken_data = pd.read_csv("dataset.csv", index_col=0)
dataFrame = pd.DataFrame(chicken_data, columns=["number", "Temp", "Humd", "Press"])
temperature = dataFrame.Temp[1:4320]
humidity = dataFrame.Humd[1:4320]
pressure = dataFrame.Press[1:4320]

print(len(temperature))

fig, ax = plt.subplots()
labels = ['12h', '24h', '36h', '48h']
def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([1080, 2160, 3240, 4320])
    ax.set_xticklabels(labels)

# # temp
# plt.title('Temperature - chicken')
# plt.xlim(0, 4320)
# plt.ylim(0, 50)
# set_axis_style(ax, labels)
# plt.plot(temperature)
# plt.xlabel("Time")
# plt.ylabel("Temperature *C")
# plt.show()

# # humd
# plt.title('humidity - chicken')
# plt.xlim(0, 4320)
# plt.ylim(0, 100)
# set_axis_style(ax, labels)
# plt.plot(humidity)
# plt.xlabel("Time")
# plt.ylabel("Humidity %")
# plt.show()

# # press
# plt.title('Air Pressure - Chicken')
# plt.xlim(0,3000)
# plt.ylim(1000, 1030)
# set_axis_style(ax, labels)
# plt.plot(pressure)
# plt.xlabel("Time")
# plt.ylabel("Pressure hPa")
# plt.show()
