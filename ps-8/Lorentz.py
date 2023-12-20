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

initial_conditions = [0, 1, 0]
time_span = (0, 50)

solution = solve_ivp(lorenz, time_span, initial_conditions, t_eval=np.linspace(0, 50, 10000))

plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[1], label='y component')
plt.title('Lorenz Equation: y component vs Time')
plt.xlabel('Time')
plt.ylabel('y component')
plt.legend()
plt.grid(True)
plt.show()