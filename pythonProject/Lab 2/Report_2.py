import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Ball': ['metal ball no hole'] * 20 + ['metal ball with hole'] * 20 + ['white ball'] * 20,
    'Try #': list(range(1, 21)) * 3,
    'h1': [124]*20 + [124.8]*20 + [123.6]*20,
    'h2': [118.4]*20 + [117.7]*40,
    'h3': [109.5]*20 + [109.1]*40,
    'D': [27.9]*20 + [28.2]*20 + [27.8]*20,
    'x': [35, 35.3, 35.9, 36, 36.8, 36.7, 36.4, 36.5, 36.5, 36.5, 36.5, 36.5, 36.6, 36.6, 36.6, 36.7, 36.7, 36.7, 36.5, 36.7] +
         [54.1, 54.5, 54.8, 56.3, 57.7, 58.4, 58.5, 58.6, 59.7, 60.8, 60.9, 61, 61.2, 61.5, 61.7, 62.1, 62.5, 62.7, 62.8, 62.8] +
         [43.1, 43.2, 43.4, 43.4, 43.7, 43.9, 44.1, 44.3, 44.3, 44.3, 44.4, 44.5, 44.5, 44.7, 44.8, 45.2, 45.6, 45, 44.9, 44.9],
    'L': [29.4]*60,
    'h1\'': [121.4]*20 + [122.3]*20 + [123]*20,
    'h2\'': [120.6]*20 + [119.4]*20 + [118.2]*20,
    'Prediction': [40.26]*20 + [37.77]*20 + [28.36]*20
}

df = pd.DataFrame(data)
"""
# Splitting the data
train_dataset = df.sample(frac=0.8, random_state=0)
test_dataset = df.drop(train_dataset.index)

# Split features from labels
train_labels = train_dataset.pop('Prediction')
test_labels = test_dataset.pop('Prediction')

# Normalize the data
train_stats = train_dataset.describe().transpose()
train_dataset = (train_dataset - train_stats['mean']) / train_stats['std']
test_dataset = (test_dataset - train_stats['mean']) / train_stats['std']

# Build the model
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=[len(train_dataset.keys())]),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1)
])

model.compile(optimizer=tf.optimizers.Adam(), loss='mse', metrics=['mae', 'mse'])

# Train the model
model.fit(train_dataset, train_labels, epochs=100, validation_split=0.2)

# Evaluate the model
loss, mae, mse = model.evaluate(test_dataset, test_labels, verbose=2)
print(f"Mean Abs Error on test data: {mae}")

# Predictions
test_predictions = model.predict(test_dataset).flatten()
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame(data)

# Statistical description
print(df.describe())

# Setting style
sns.set(style="whitegrid")

# Aggregations
aggregations = {
    'h1': ['mean', 'std', 'median'],
    'h2': ['mean', 'std', 'median'],
    'h3': ['mean', 'std', 'median'],
    'D': ['mean', 'std', 'median'],
    'x': ['mean', 'std', 'median'],
    'L': ['mean', 'std', 'median'],
    'h1\'': ['mean', 'std', 'median'],
    'h2\'': ['mean', 'std', 'median'],
    'Prediction': ['mean', 'std', 'median']
}

import numpy as np
import statsmodels.api as sm

# Regression Analysis for each ball type
ball_types = df['Ball'].unique()
for ball in ball_types:
    subset = df[df['Ball'] == ball]
    X = subset[['h1', 'h2', 'h3', 'D', 'L', 'h1\'', 'h2\'']]
    X = sm.add_constant(X)  # Adds a constant term to the predictor
    y = subset['x']

    model = sm.OLS(y, X).fit()
    print(f"Regression Analysis for {ball}")
    print(model.summary())
    print("\n" + "=" * 50 + "\n")

    residuals = model.resid
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=subset['x'], y=residuals)
    plt.axhline(y=0, color='red', linestyle='--')
    plt.title(f'Residuals Plot for {ball}')
    plt.show()


