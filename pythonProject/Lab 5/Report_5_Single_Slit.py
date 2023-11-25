import numpy as np
import matplotlib.pyplot as plt

# Given data for Single-Slit
linear_position_single = np.array([-0.128, -0.11, -0.1, -0.061, -0.05, -0.048])
order_number_single = np.arange(1, len(linear_position_single) + 1)

# Least Squares for Single-Slit
N = len(order_number_single)
a, b = np.polyfit(order_number_single, linear_position_single, 1)
predicted_values_single = a * order_number_single + b
sigma_a = np.sqrt(np.sum((linear_position_single - predicted_values_single)**2) / (N - 2) / np.sum((order_number_single - np.mean(order_number_single))**2))
sigma_b = sigma_a * np.sqrt(np.sum(order_number_single**2) / N)

print(f"Single-Slit: a = {a:.4f}, sigma_a = {sigma_a:.4f}, b = {b:.4f}, sigma_b = {sigma_b:.4f}")

# Plot data, linear fit, and least squares residuals
plt.figure(figsize=(10,6))
plt.scatter(order_number_single, linear_position_single, label='Data')
plt.plot(order_number_single, predicted_values_single, 'blue', label='Linear Fit')

# Visualizing the least squares residuals
for i, j, pred in zip(order_number_single, linear_position_single, predicted_values_single):
    plt.plot([i, i], [j, pred], 'g--')

plt.title("Single-Slit Diffraction: xn vs. n")
plt.xlabel("Order number (n)")
plt.ylabel("Linear position xn (m)")
plt.legend()
plt.grid(True)
plt.show()