import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("advertising.csv")

X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

model = LinearRegression()
model.fit(X, y)

print("Predicted Sales:", model.predict([[100, 20, 10]])[0])