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


# This function is an envelope that
# approximates a box function centred at 0 with length 2L.
# As k->inf, the approximation becomes exact.
# k = 1000 is a bit of a placeholder.
def generate_envelope_function(L, x, k=1000):
    return (0.5+0.5*np.tanh(k*(x+L))) - (0.5+0.5*np.tanh(k*(x-L)))


# Generates a wavefunction.
# The wave function is guaranteed not
# to diverge at infinity due to the envelope
def generate_psi(cn, x, L, k = 1000):
    return exponential_series(cn, x, L) * generate_envelope_function(L, x, k)

y = generate_psi(an, xfine, L)
plt.plot(xfine, y)
plt.axis([-12, 12, -5, 5])
plt.show()
