import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("car_data.csv")

plt.scatter(df["Car_Age"], df["Selling_Price"])
plt.xlabel("Car Age")
plt.ylabel("Selling Price")
plt.title("Car Age vs Selling Price")
plt.show()