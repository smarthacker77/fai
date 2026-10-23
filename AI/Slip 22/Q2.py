from sklearn.linear_model import LinearRegression

# Dataset: Area, Bedrooms, Price
X = [
    [1000, 2],
    [1500, 3],
    [2000, 3],
    [2500, 4],
    [3000, 4]
]

y = [20, 30, 40, 50, 60]  # Price in lakhs

model = LinearRegression()
model.fit(X, y)

area = float(input("Enter house area in sq.ft: "))
bedrooms = int(input("Enter number of bedrooms: "))

price = model.predict([[area, bedrooms]])

print("Predicted House Price:", round(price[0], 2), "Lakhs")