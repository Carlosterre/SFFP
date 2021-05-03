# Getting the numpy module
import numpy as np

# Getting the matplotbib module
import matplotlib.pyplot as plt

# Number of grid points
N = 11

# Domain size
L = 1

# Corresponding grid spacing
h = np.float64(L / (N - 1))

# Iteration number
iterations = 0

# Initializing temperature field
T = np.zeros(N)
T[N-1] = 1.

# Initializing iterated temperature
T_new = np.zeros(N)
T_new[N-1] = 1.

# Error related variables
epsilon = 1.E-8
numerical_error = 1                                                            # Set as 1 in order to satisfy the while loop condition

# Checking the error tolerance
while numerical_error > epsilon:
    # Computing for all interior points
    for i in range(1, N-1):
        T_new[i] = 0.5 * (T[i-1] + T[i+1])  
    
    # Resetting the numerical error and recalculate
    numerical_error = 0
    for i in range(1, N-1):
        numerical_error = numerical_error + abs(T[i] - T_new[i])
    
    # Iteration advancement and reassignment
    iterations = iterations + 1
    T = T_new.copy()
    
    # Plotting numerical error
    plt.figure(1)
    plt.plot(iterations, numerical_error, 'ko')
    # plt.pause(0.01)                                                           # Residual plot on fly Ansys Fluent like
    
plt.show()

# Plotting the results
plt.figure(2)

# Defining the position from indexes
x_dom = np.arange(N) * h

# Plotting the variation with customization
plt.plot(x_dom, T, 'bx--', linewidth=2, markersize=10)

# Displaying the gridlines
plt.grid(True, color='k')

# Labelling and providing a title to the plot
plt.xlabel('Position', size=15)
plt.ylabel('Temperature', size=15)
plt.title('T(x)')
# plt.margins(0)

# Showing the plot on screen
plt.show()
