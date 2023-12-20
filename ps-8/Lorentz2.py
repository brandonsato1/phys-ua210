import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Define the Lorenz system of equations
def lorenz(t, y):
    sigma = 10
    r = 28
    b = 8 / 3
    dydt = [sigma * (y[1] - y[0]), r * y[0] - y[1] - y[0] * y[2], y[0] * y[1] - b * y[2]]
    return dydt

# Set initial conditions and time span
initial_conditions = [0, 1, 0]
time_span = (0, 50)

# Solve the system of equations
solution = solve_ivp(lorenz, time_span, initial_conditions, t_eval=np.linspace(0, 50, 10000))

# Plot z vs x
plt.figure(figsize=(10, 6))
plt.plot(solution.y[0], solution.y[2], label='z vs x')
plt.title('Lorenz Equation: z vs x')
plt.xlabel('x')
plt.ylabel('z')
plt.legend()
plt.grid(True)
plt.show()