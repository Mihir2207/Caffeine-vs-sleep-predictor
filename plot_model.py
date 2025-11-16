# plot_model.py
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

df = pd.read_csv("caffeine_sleep.csv")
with open("sleep_model.pkl","rb") as f:
    model = pickle.load(f)

X = df["Caffeine_mg"].values
y = df["Sleep_Quality"].values
xs = np.linspace(0, 600, 200).reshape(-1,1)
ys = model.predict(xs)

plt.scatter(X, y, alpha=0.6, label="data")
plt.plot(xs, ys, color="red", label="regression")
plt.xlabel("Caffeine (mg)")
plt.ylabel("Sleep Quality (0-10)")
plt.legend()
plt.grid(True)
plt.savefig("regression_plot.png", dpi=150)
print("Saved regression_plot.png")
