# Getting the numpy module
import numpy as np

# Polynomial definition
poly_p = np.array([-4, 7, -3, 9])

# Plunomial derivative (numpy)
p_der = np.polyder(poly_p)
print('Derivative polinomial =', p_der)

# Polynomial derivative (numpy)
p_der = np.polyder(poly_p)
print('Derivative polinomial =', p_der)

# Analytical result at x = 0
p_der_eval = np.polyval(p_der, 0.0)
print('Theoretical derivative =', p_der_eval)

# Numerical calculations using FMD (forward)
x_0 = 0.0
h = np.float(0.25)
forward_difference = (np.polyval(poly_p, x_0 + h) - np.polyval(poly_p, x_0)) / h
print('Forward derivative =', forward_difference)

# Numerical calculations usinf FMD (backward)
x_0 = 0.0
h = np.float(0.25)
backward_difference = (np.polyval(poly_p, x_0) - np.polyval(poly_p, x_0 - h)) / h
print('Backward derivative =', backward_difference)

# Numerical calculations using FMD (central)
x_0 = 0.0
h = np.float(0.25)
central_difference = (np.polyval(poly_p, x_0 + h) - np.polyval(poly_p, x_0 - h)) / (2 *h)
print('Central derivative =', central_difference)
