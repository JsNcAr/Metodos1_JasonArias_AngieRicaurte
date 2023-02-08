import numpy as np
import matplotlib.pyplot as plt

M = [1, 0, -1]


def central_convolution(f, x, h):
    return sum([f(x - h * i) * M[i] for i in range(3)]) / (2 * h)


x = np.linspace(0, 2 * np.pi, 100)
d_sin = central_convolution(np.sin, x, 0.01)

plt.plot(x, np.cos(x), label='cos(x)')
plt.plot(x, d_sin, label='d_sin(x)', linestyle='--')

plt.legend()
plt.savefig('d_sin.png', dpi=300)