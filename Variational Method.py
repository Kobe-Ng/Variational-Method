import numpy as np
from sympy import *

# The test function will have E=C_0*h*w. We only calculate C_0 and multiple hw after. 
x = Symbol('x')
h_bar = 1.0
m = 1.0
w = 1.0

# test function. Expected expectation value is -0.244845268923
a = 0.336796
A = (a/np.pi)**(0.25)
psi_test = A*exp(-a*x**2.0/2.0)
# The values we use to approximate the integral
xfine = np.linspace(-30, 30, 20000)


# TODO: Check if conjugation and differentiation via numpy
# instead of numpy confers a notable speed up.
def energy_expectation_value(x, psi, V, xfine):
    # Set up numpy arrays.
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

    # ke_expression is the expression to be integrated related to the p^2/2m term
    ke_expression = psi_conjugate_array * -h_bar**2.0 / (2.0*m) * psi_second_prime_array 
    # pe_expression is the expression to be integrated related to the V(x) term
    pe_expression = psi_conjugate_array * V_array * psi_array
    kinetic_energy = np.trapz(ke_expression, xfine)
    potential_energy = np.trapz(pe_expression, xfine)

    return kinetic_energy + potential_energy


def potential(x):
    return -((x**2.0) / 2.0) + ((x**4.0) / 16.0)

V = potential(x)
print(energy_expectation_value(x, psi_test, V, xfine))
