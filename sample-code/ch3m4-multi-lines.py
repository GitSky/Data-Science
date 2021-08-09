import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
# plt.savefig("plot.png")
plt.show()
