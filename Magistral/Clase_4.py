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

Ex = np.zeros((n, n))
Ey = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        Ex[i, j] = 1.

fig = plt.figure(figsize=(5, 5))
ax = fig.add_subplot(111)
ax.scatter(X, Y, c='r', marker='o', s=25)

for i in range(n):
    for j in range(n):
        ax.quiver(x[i], y[j], Ex[i, j], Ey[i, j], color='b')

plt.savefig('2D.png', dpi=300)
