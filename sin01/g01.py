import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4*np.pi, 100)
y = np.sin(t)

plt.plot(t,y)
plt.show()

