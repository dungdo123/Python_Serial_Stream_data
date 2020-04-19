import pandas as pd
import matplotlib.pyplot as plt

Power_in = pd.read_csv('power.csv')
dataFrame = pd.DataFrame(Power_in, columns=['Distance', 'Simulated', 'Measured'])
x = dataFrame.Distance
y = dataFrame.Simulated
z = dataFrame.Measured

plt.plot(x, y, label="Simulated", linewidth=5)
plt.plot(x, z, '--', label="Measured", linewidth=5)
plt.xlabel("Distance [m]", fontsize=25)
plt.ylabel("Received RF power [dBm]", fontsize=25)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid()
plt.legend(loc='higher right', fontsize=25)

plt.show()