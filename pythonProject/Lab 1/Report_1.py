import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Constructing the dataframe from the provided data
data = {
    "height": np.repeat([1.24, 2.53, 3.8, 5.18, 6.71], 10),
    "trial": list(range(1, 11)) * 5,
    "distance": [1.164, 1.156, 1.097, 1.227, 1.244, 1.216, 1.206, 1.109, 1.106, 1.192,
                 1.174, 1.203, 1.179, 1.195, 1.189, 1.196, 1.172, 1.207, 1.167, 1.212,
                 1.223, 1.197, 1.196, 1.191, 1.2, 1.234, 1.2, 1.207, 1.179, 1.192,
                 1.21, 1.203, 1.207, 1.21, 1.24, 1.23, 1.23, 1.188, 1.219, 1.215,
                 1.206, 1.217, 1.21, 1.206, 1.201, 1.195, 1.204, 1.215, 1.212, 1.208],
    "v_after_collision": [-0.17, -0.15, -0.15, -0.16, -0.17, -0.17, -0.16, -0.16, -0.16, -0.17,
                          -0.23, -0.21, -0.23, -0.23, -0.23, -0.23, -0.22, -0.22, -0.23, -0.22,
                          -0.25, -0.25, -0.26, -0.25, -0.25, -0.27, -0.27, -0.26, -0.25, -0.27,
                          -0.3, -0.3, -0.3, -0.3, -0.31, -0.31, -0.3, -0.29, -0.3, -0.29,
                          -0.33, -0.34, -0.33, -0.33, -0.34, -0.31, -0.34, -0.34, -0.35, -0.35],
    "slope_ax": [0.0134, 0.0127, 0.0137, 0.0134, 0.0133, 0.0128, 0.0129, 0.0135, 0.0122, 0.013,
                 0.0259, 0.0263, 0.0251, 0.0258, 0.025, 0.0254, 0.0249, 0.0258, 0.0252, 0.0251,
                 0.0376, 0.0371, 0.0378, 0.0383, 0.0381, 0.0384, 0.0383, 0.0381, 0.0382, 0.0379,
                 0.052, 0.0524, 0.0518, 0.0519, 0.0517, 0.0506, 0.0527, 0.0515, 0.0509, 0.0518,
                 0.0667, 0.0647, 0.0654, 0.0665, 0.0657, 0.0656, 0.0654, 0.0648, 0.0654, 0.0654]
}

df = pd.DataFrame(data)

# Linear regression and plotting for height vs distance
sns.lmplot(x='height', y='distance', data=df)
plt.title("Linear Regression: Height vs. Distance")
plt.show()

# Linear regression and plotting for height vs v_after_collision
sns.lmplot(x='height', y='v_after_collision', data=df)
plt.title("Linear Regression: Height vs. V After Collision")
plt.show()

# Linear regression and plotting for height vs slope_ax
sns.lmplot(x='height', y='slope_ax', data=df)
plt.title("Linear Regression: Height vs. Slope (ax)")
plt.show()
