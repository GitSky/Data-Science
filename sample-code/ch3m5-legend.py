import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
plt.plot(x,np.sin(x),'k:',label='sin(x)')
plt.plot(x,np.cos(x),'r--',label='cos(x)')
plt.legend()
plt.savefig("plot.png")
plt.show()
