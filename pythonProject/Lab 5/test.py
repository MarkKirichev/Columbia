import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Given data for Double-Slit
linear_position = np.array([-0.079, -0.076, -0.082, -0.074, -0.085, -0.072, -0.087, -0.068, -0.09, -0.066, -0.092])
order_number = np.arange(1, len(linear_position) + 1)

# Sinusoidal function
def sinusoidal(x, A, B, C, D):
    return A * np.sin(B * x + C) + D

# Grid search over possible parameters
A_range = np.linspace(0, 2, 100)
B_range = np.linspace(0, 2, 100)
C_range = np.linspace(0, 2*np.pi, 100)
D_range = np.linspace(0, 2, 100)

min_error = np.inf
best_params = (0, 0, 0, 0)

for A in tqdm(A_range):
    for B in B_range:
        for C in C_range:
            for D in D_range:
                error = np.sum((linear_position - sinusoidal(order_number, A, B, C, D))**2)
                if error < min_error:
                    min_error = error
                    best_params = (A, B, C, D)

# Plot using best params
predicted = sinusoidal(order_number, *best_params)

plt.figure(figsize=(10,6))
plt.scatter(order_number, linear_position, label='Data')
plt.plot(order_number, predicted, 'orange', label='Sinusoidal Fit')
plt.title("Double-Slit Diffraction: xm vs. m")
plt.xlabel("Order number (m)")
plt.ylabel("Linear position xm (m)")
plt.legend()
plt.grid(True)
plt.show()