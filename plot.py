import numpy as np
import matplotlib.pyplot as plt

v = np.array([1, 2])
plt.plot([0, v[0]], [0, v[1]])
for i in range(10):
    s = np.random.randn()
    sv = s * v
    plt.plot([0, sv[0]], [0, sv[1]])
plt.grid("on")
plt.axis([-4, 4, -4, 4])
plt.show()