import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Sample Data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # Independent variable (features)
y = np.array([2, 4, 5, 4, 5])  # Dependent variable (target)

print(X)
print(y)
# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict values
y_pred = model.predict(X)

# Print coefficients
print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

# Plot the results
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, y_pred, color='red', linestyle="--", label="Regression Line")
plt.xlabel("X (Independent Variable)")
plt.ylabel("y (Dependent Variable)")
plt.legend()
plt.show()

# 1.X contains the independent variable (reshaped to a 2D array).
# 2.y contains the dependent variable.
# 3.LinearRegression().fit(X, y) trains the model.
# 4.model.predict(X) generates predictions.
# 5.The regression line is plotted against actual data.
