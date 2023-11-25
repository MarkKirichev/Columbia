import numpy as np
import matplotlib.pyplot as plt
# from scipy.optimize import curve_fit

# Given data for Malus' Law
angular_position = np.array([0, 10.8, 20, 30.1, 39.5, 51.5, 58.4, 68.9, 81, 89.6, 100.3, 110, 121.1, 130.2, 139.2, 149.9, 161, 179.2, 190.7, 199.2])
relative_intensity = np.array([1254.96, 1726.42, 2104.12, 2438.26, 2623.46, 2657.03, 2548.81, 2276.38, 1780.34, 1403.94, 923.45, 545.74, 209.82, 60.58, 27.19, 154.05, 454.38, 1189.73, 1708.55, 2058.31])
theta_0 = 47.6
I_0 = 2675.47

# Calculation
theta_rad = np.radians(angular_position - theta_0)
I_I0 = relative_intensity / I_0
cos2_theta = np.cos(theta_rad)**2

# Linear Regression for Malus' Law
slope, intercept = np.polyfit(cos2_theta, I_I0, 1)

residuals = I_I0 - (slope * cos2_theta + intercept)
std_error = np.std(residuals)
print(f"Standard error (Noise approximation) for Malus' Law: {std_error:.4f}")
print(f"Slope: {slope:.4f} ± {std_error:.4f}")
print(f"Intercept: {intercept:.4f} ± {std_error:.4f}")

# Plot
plt.figure(figsize=(10,6))
plt.scatter(cos2_theta, I_I0, label='Data')
plt.plot(cos2_theta, slope * cos2_theta + intercept, 'r', label=f'Linear Fit: y={slope:.2f}x + {intercept:.2f}')
plt.title("Malus' Law: I/I0 vs. cos^2(θ)")
plt.xlabel("cos^2(θ - θ_0)")
plt.ylabel("I/I0")
plt.legend()
plt.grid(True)
plt.show()

# Least Squares for Malus' Law
N = len(cos2_theta)
a, b = np.polyfit(cos2_theta, I_I0, 1)
predicted_values = a * cos2_theta + b
sigma_a = np.sqrt(np.sum((I_I0 - predicted_values)**2) / (N - 2) / np.sum((cos2_theta - np.mean(cos2_theta))**2))
sigma_b = sigma_a * np.sqrt(np.sum(cos2_theta**2) / N)

print(f"Malus' Law: a = {a:.4f}, sigma_a = {sigma_a:.4f}, b = {b:.4f}, sigma_b = {sigma_b:.4f}")
