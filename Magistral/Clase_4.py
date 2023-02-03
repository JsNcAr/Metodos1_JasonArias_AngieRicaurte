import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = 1
B = 3
omega = 2 * np.pi / 10
N = 100
t = np.linspace(0, 10, N)

r = np.array([A * np.cos(omega * t), A * np.sin(omega * t), B * t])

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(r[0], r[1], r[2], c='r', marker='o', s=25)

plt.savefig('3D.png', dpi=300)

n = 4
x = np.linspace(0, 1, n)
y = np.linspace(0, 1, n)

X, Y = np.meshgrid(x, y)

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.scatter(X, Y, c='r', marker='o', s=25)
plt.savefig('2D.png', dpi=300)
