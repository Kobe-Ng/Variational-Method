import numpy as np

# The test function will have E=C_0*h*w. We only calculate C_0 and multiple hw after. 
h_bar = 1.0
m = 1.0
w = 1.0

# test function. Expected expectation value is -0.244845268923
xfine = np.linspace(-10, 10, 2000)
a = 0.336796


def psi_test(x):
    return np.exp(-a*x**2.0/2.0)


def psi_test2(x):
    return 0.5+0.5*np.tanh(1000*(x+(20/3)**.5)) - (0.5+0.5*np.tanh(1000*(x-(20/3)**.5)))


# normalizes a square integrable function.
def normalize(psi):
    inner_product = np.trapz(psi * np.conj(psi), xfine)
    return 1 / (inner_product)**(0.5) * psi


def energy_expectation_value(psi, V, xfine):
    V_array = V(xfine)
    psi_array = psi(xfine)

    psi_array = normalize(psi_array)

    # Set up numpy arrays.
    psi_conjugate = np.conj(psi_array)

    # xfine[1]-xfine[0] gives the spacing between two elements.
    psi_prime = np.gradient(psi_array, (xfine[1]-xfine[0]))
    psi_second_prime = np.gradient(psi_prime, (xfine[1]-xfine[0]))

    # ke_expression is the expression to be integrated related to the p^2/2m term
    ke_expression = psi_conjugate * -h_bar**2.0 / (2.0*m) * psi_second_prime
    # pe_expression is the expression to be integrated related to the V(x) term
    pe_expression = psi_conjugate * V_array * psi_array
    kinetic_energy = np.trapz(ke_expression, xfine)
    potential_energy = np.trapz(pe_expression, xfine)

    return kinetic_energy + potential_energy


def potential(x):
    return -((x**2.0) / 2.0) + ((x**4.0) / 16.0)


V = potential
psi = psi_test
print(energy_expectation_value(psi, V, xfine))
