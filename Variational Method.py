import numpy as np
from sympy import *

x = Symbol('x')
h_bar = 1.0
m = 1.0
w = 1.0

# testing expressions using known values
a = 0.16839
A = (a/np.pi)**(0.25)
psi_test = A*exp(-a*x**2.0/2.0)
# The values we use to approximate the integral
xfine = np.linspace(-30, 30, 20000)


def energy_expectation_value(x, psi, V, xfine):
    # Set up numpy arrays.
    # Currently differentiating symbolically due to laziness.
    # One should use numpy differentiation for speeds sake.
    # TODO: change differentiation to be entirely numpy
    psi_conjugate = conjugate(psi)
    psi_conjugate = lambdify(x, psi_conjugate, 'numpy')
    psi_conjugate_array = psi_conjugate(xfine)

    psi_second_prime = psi.diff(x, 2)
    psi_second_prime = lambdify(x, psi_second_prime, 'numpy')
    psi_second_prime_array = psi_second_prime(xfine)

    psi = lambdify(x, psi, 'numpy')
    psi_array = psi(xfine)

    V = lambdify(x, V, 'numpy')
    V_array = V(xfine)

    ke_expression = psi_conjugate_array * -h_bar**2.0 / (2.0*m) * psi_second_prime_array 
    pe_expression = psi_conjugate_array * V_array * psi_array
    kinetic_energy = np.trapz(ke_expression, xfine)
    potential_energy = np.trapz(pe_expression, xfine)

    return kinetic_energy + potential_energy


def potential(x):
    return -((x**2.0) / 2.0) + ((x**4.0) / 16.0)

V = potential(x)
print(energy_expectation_value(x, psi_test, V, xfine))
