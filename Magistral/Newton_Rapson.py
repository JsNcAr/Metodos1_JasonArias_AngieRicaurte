import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
import random


def Function(x):
    return 0.5 * (3 * x**2 - 1)


x = np.linspace(-1, 1, 100)
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
            #print(
            #    f'Iteration {it}: xn = {xn}, x = {xn1}, error = {error}, f(x) = {f(xn1)}, df(x) = {df(f, xn)}'
            #)
        except ZeroDivisionError:
            print('Error: division by zero')
        xn = xn1
        it += 1

    return xn


x = Newton_Raphson(Function, central_difference, random.uniform(-1, 1))

print(x)
