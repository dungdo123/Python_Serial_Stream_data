import pandas as pd
import matplotlib.pyplot as plt

chicken_data = pd.read_csv('12h_.csv', index_col=0)
dataFrame = pd.DataFrame(chicken_data, columns=['number', 'Temp', 'Humd', 'Pressure'])
x = dataFrame.Temp
y = dataFrame.Humd
z = dataFrame.Pressure


# print(len(x))
plt.xlim(0,1000)
plt.ylim(0,40)
plt.plot(x)
plt.xlabel("Time (x2 minutes)")
plt.ylabel("Temp oC")
#
# plt.plot(y)
# plt.xlabel("Time (x2 minutes)")
# plt.ylabel("Humidity %")

# plt.plot(z)
# plt.xlabel("Time (x2 minutes) ")
# plt.ylabel("Pressure hPa")
#

plt.show()