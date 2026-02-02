import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load data
df = pd.read_csv("data/house_prices.csv")

X = df[["area_sqft", "bedrooms", "bathrooms", "location_score"]]
y = df["price"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("R2 Score:", r2_score(y_test, preds))

# Save model
with open("models/house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully")

