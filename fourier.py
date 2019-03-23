import matplotlib.pyplot as plt
import numpy as np

xfine = np.linspace(-10, 10, 2000)
L = 1


def cos_series(an, x, L):
    f = 0
    for n, a in enumerate(an):
        f += a * np.cos(n * np.pi * x / L)
    return f


def sin_series(bn, x, L):
    f = 0
    for n, b in enumerate(bn, 1):
        f += b * np.sin(n * np.pi * x / L)
    return f


def exponential_series(cn, x, L):
    f = 0
    for n, c in enumerate(cn, 1):
        f += c * np.exp(2 * 1j * n * np.pi * x / L)
    return f


an = np.array([1, 1, 0, -1 / 3.0, 0, 1 / 5.0, 0, -
               1 / 7.0, 0, 1 / 9.0, 0, -1 / 11.0, 0, 1 / 13.0])


y = cos_series(an, xfine, L)
print(xfine.size)
print(y.size)
plt.plot(xfine, y)
plt.axis([-12, 12, -5, 5])
plt.show()
