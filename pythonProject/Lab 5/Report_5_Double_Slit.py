import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

# Given data for Double-Slit
linear_position = np.array([-0.079, -0.076, -0.082, -0.074, -0.085, -0.072, -0.087, -0.068, -0.09, -0.066, -0.092])
order_number = np.arange(1, len(linear_position) + 1)


# Sinusoidal fitting function
def sinusoidal_fit(x, A, B, C, D):
    return A * np.sin(B * x + C) + D


# Estimate initial parameters for sinusoidal fit
A_init = (np.max(linear_position) - np.min(linear_position)) / 2
B_init = 2 * np.pi / (order_number[-1] - order_number[0])
C_init = 0
D_init = np.mean(linear_position)
initial_guess = [A_init, B_init, C_init, D_init]

# Gradient descent-like approach
learning_rate = 0.01
num_iterations = 1000

params = initial_guess
for _ in tqdm(range(num_iterations)):
    A_grad = np.sum((sinusoidal_fit(order_number, *params) - linear_position) * np.sin(B_init * order_number + C_init))
    B_grad = np.sum((sinusoidal_fit(order_number, *params) - linear_position) * A_init * order_number * np.cos(
        B_init * order_number + C_init))
    C_grad = np.sum(
        (sinusoidal_fit(order_number, *params) - linear_position) * A_init * np.cos(B_init * order_number + C_init))
    D_grad = np.sum(sinusoidal_fit(order_number, *params) - linear_position)

    params[0] -= learning_rate * A_grad
    params[1] -= learning_rate * B_grad
    params[2] -= learning_rate * C_grad
    params[3] -= learning_rate * D_grad

# Calculate sinusoidal values for plotting
sinusoidal_values = sinusoidal_fit(order_number, *params)

# Plot
plt.figure(figsize=(10, 6))
plt.scatter(order_number, linear_position, label='Data')
plt.title("Double-Slit Diffraction: xm vs. m")
plt.xlabel("Order number (m)")
plt.ylabel("Linear position xm (m)")
plt.legend()
plt.grid(True)
plt.show()