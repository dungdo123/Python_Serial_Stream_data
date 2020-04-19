import pandas as pd
import matplotlib.pyplot as plt

pork_data = pd.read_csv("dataset_pork.csv", index_col=0)
dataFrame = pd.DataFrame(pork_data, columns=["number", "Temp", "Humd", "Press"])
temperature = dataFrame.Temp[1:15000]
humidity = dataFrame.Humd[1:15000]
pressure = dataFrame.Press[1:2880]
fig, ax = plt.subplots()
labels = ['12h', '24h', '36h', '48h']
def set_axis_style(ax, labels):
    ax.get_xaxis().set_tick_params(direction='out')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticks([720, 1440, 2160, 2880])
    ax.set_xticklabels(labels)

# press
plt.title('Air Pressure - Pork')
plt.xlim(0, 2880)
plt.ylim(1000, 1030)
set_axis_style(ax, labels)
plt.plot(pressure, color = 'red')
plt.xlabel("Time")
plt.ylabel("Pressure hPa")
plt.show()

