# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import pickle

# Load data
df = pd.read_csv("caffeine_sleep.csv")

# X = caffeine, y = sleep quality
X = df[["Caffeine_mg"]]
y = df["Sleep_Quality"]

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# train linear regression
model = LinearRegression()
model.fit(X_train, y_train)

# evaluate
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"R^2: {r2:.3f}   MSE: {mse:.3f}")

# save model
with open("sleep_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Print coefficients for the regression line
m = model.coef_[0]
c = model.intercept_
print(f"Model: Sleep_Quality = {m:.4f} * Caffeine_mg + {c:.4f}")
print("Saved trained model to sleep_model.pkl")
