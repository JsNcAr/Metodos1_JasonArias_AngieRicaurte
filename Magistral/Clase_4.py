import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = 1
B = 1
omega = 2 * np.pi
N = 100
t = np.linspace(0, 10, N)

r = np.array([A * np.cos(omega * t), A * np.sin(omega * t), B * t])

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(r[0], r[1], r[2], c='r', marker='o', s=25)

plt.savefig('Figura_4.png', dpi=300)