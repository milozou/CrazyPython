import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.01)

y = np.sin(x)

plt.plot(x,y)
plt.show()
