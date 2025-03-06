import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

# Sample dataset: Each row represents a house
data = {
    'Size_sqft': [1200, 1500, 1800, 2000, 2200, 2500, 2750, 3000, 3200, 3500],
    'Bedrooms': [2, 3, 3, 4, 4, 4, 5, 5, 5, 6],
    'Bathrooms': [1, 2, 2, 3, 3, 3, 4, 4, 5, 5],
    'Location_Score': [7, 8, 6, 9, 8, 7, 9, 8, 9, 10],  # Higher is better
    'House_Age': [10, 5, 15, 7, 3, 8, 12, 4, 2, 1],  # Age in years
    'Price': [500000, 600000, 650000, 700000, 750000, 800000, 850000, 900000, 950000, 1000000]  # Price in USD
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Splitting features (X) and target (y)
X = df[['Size_sqft', 'Bedrooms', 'Bathrooms', 'Location_Score', 'House_Age']]
y = df['Price']

# Split into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print(f"Mean Absolute Error (MAE): {mae}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

# Predict price for a 2BHK house (Example: 1400 sqft, 2 bedrooms, 2 bathrooms, location score 7, age 8 years)
house_features = np.array([[1400, 2, 2, 7, 8]])  # Input as a 2D array
predicted_price = model.predict(house_features)

print(f"Predicted price for a 2BHK house: ${predicted_price[0]:,.2f}")
