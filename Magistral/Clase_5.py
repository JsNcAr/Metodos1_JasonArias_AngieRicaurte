import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

epsilon = 1.

while 1 + epsilon != 1.:
    epsilon *= 0.5

print(epsilon)


def epsilon(x):
    return np.sin(x) - (x - x**3 / 6)


x = 3 * np.pi / 2
print(epsilon(x) / epsilon(x / 2))


def Function(x):
    return np.sin(x)


def EDerivative(x):
    return np.cos(x)


x = np.linspace(0, 2 * np.pi, 10)

y = Function(x)

plt.scatter(x, y)
