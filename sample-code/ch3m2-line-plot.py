import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
y = np.sin(x)
fig = plt.figure()
ax = plt.axes()
ax.plot(x, y)
plt.savefig("plot.png")
plt.show()
