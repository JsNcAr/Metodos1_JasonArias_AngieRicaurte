import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc


def Function(x):
    return 5 * (1 - np.exp(-x)) - x


x = np.linspace(0, 10, 100)
y = Function(x)

plt.plot(x, y, label='Function', color='r', linewidth=2, linestyle='-')
plt.axhline(0, color='k')
plt.legend()
plt.savefig('./Function.png')


def central_difference(f, x, h=1e-4):
    return (f(x + h) - f(x - h)) / (2 * h)


def Newton_Raphson(f, df, xn, max_iter=100, tol=1e-5):
    error = 1
    it = 0
    while error > tol and it < max_iter:
        try:
            xn1 = xn - f(xn) / df(f, xn)
            error = abs(f(xn) / df(f, xn))
        except ZeroDivisionError:
            print('Error: division by zero')
        xn = xn1
        it += 1

    return xn


x = Newton_Raphson(Function, central_difference, 4)

print(x)
