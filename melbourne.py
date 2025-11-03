# Import libraries
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Global setting to format floating point numbers in pandas DataFrames
pd.options.display.float_format = '{:.2f}'.format

# Load data
melbourne_file_path = "datasets/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.describe())

# Specify prediction target
y = melbourne_data.Price

# Select predictive features
feature_name = ['Rooms', 'Bathroom', 'Landsize', 'BuildingArea', 'YearBuilt', 'Lattitude', 'Longtitude']
X = melbourne_data[feature_name]

# Double-check the data
print(X.head(5))
print(melbourne_data.describe())

# Split the data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)

# Create and fit a DecisionTreeRegressor model
melbourne_model = DecisionTreeRegressor(random_state = 1)
melbourne_model.fit(train_X, train_y)

# Make predictions with validation observations
val_predictions = melbourne_model.predict(val_X)

# Calculate mean absolute error in validation data
val_mae = mean_absolute_error(val_y, val_predictions)
print(f"Mean Absolute Error in Validation Data: {val_mae:.2f}")

# Function to calculate MAE for different tree sizes
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state = 0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return mae

# Try different values for max_leaf_nodes
candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
for candidate in candidate_max_leaf_nodes:
    mae = get_mae(candidate, train_X, val_X, train_y, val_y)
    print(f"Max leaf nodes: {candidate}  \t Mean Absolute Error: {mae:.2f}")

# Final model using the best tree size and all data
best_tree_size = 500
final_model = DecisionTreeRegressor(max_leaf_nodes=best_tree_size, random_state = 1)
final_model.fit(X, y)

# Make predictions using final model, with all observations
predictions = final_model.predict(X)
comparison = pd.DataFrame({
    'Actual': list(y.head(5)),
    'Predicted': predictions[:5]
})
print(comparison)

# Define and fit a Random Forest model
rf_model = RandomForestRegressor(random_state = 1)
rf_model.fit(train_X, train_y)

# Calculate the mean absolute error of the Random Forest model on the validation data
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)
print(f"Validation MAE for Random Forest Model: {rf_val_mae:.2f}")
