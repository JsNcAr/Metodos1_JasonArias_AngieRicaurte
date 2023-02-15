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


x = np.linspace(0, 2 * np.pi, 50)

h = x[1] - x[0]

f = Function(x)


def RightDerivative(f, x, h):

    d = 0.

    if h != 0:
        d = (f(x + h) - f(x)) / h

    return d


def LeftDerivative(f, x, h):

    d = 0.

    if h != 0:
        d = (f(x) - f(x - h)) / h

    return d


def CentralDerivative(f, x, h):

    d = 0.

    if h != 0:
        d = (f(x + h) - f(x - h)) / (2 * h)

    return d


RightDerivative(Function, 0.5, 0.001)

RDerivative = RightDerivative(Function, x, h)
LDerivative = LeftDerivative(Function, x, h)
CDerivative = CentralDerivative(Function, x, h)

plt.scatter(x, EDerivative(x))
plt.scatter(x, RDerivative)
plt.scatter(x, LDerivative)
plt.scatter(x, CDerivative)

plt.scatter(x, np.abs(EDerivative(x) - RDerivative), label='Right Derivative')
plt.scatter(x, np.abs(EDerivative(x) - LDerivative), label='Left Derivative')
plt.scatter(x,
            np.abs(EDerivative(x) - CDerivative),
            label='Central derivative')
plt.yscale('log')
plt.legend()

K = np.array([+1., 0., -1.])
