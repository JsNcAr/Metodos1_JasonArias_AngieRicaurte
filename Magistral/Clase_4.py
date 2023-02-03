import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = 1
B = 1
omega = 2 * np.pi
N = 100
t = np.linspace(0, 10, N)

r = np.array([A * np.cos(omega * t), A * np.sin(omega * t), B * t])

print(r[:10])