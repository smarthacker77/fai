from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

model = LinearRegression()
model.fit(X, y)

n = int(input("Enter value to predict: "))
result = model.predict([[n]])

print("Predicted output:", result[0])