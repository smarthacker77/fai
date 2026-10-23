from sklearn.tree import DecisionTreeClassifier

# Features: [Is leafy, Grows from flower]
X = [[1, 0], [1, 0], [0, 1], [0, 1]]
y = ["Leafy", "Leafy", "Fruit", "Fruit"]

model = DecisionTreeClassifier()
model.fit(X, y)

leafy = int(input("Is it a leafy vegetable? (1=Yes, 0=No): "))
flower = int(input("Grows from flower? (1=Yes, 0=No): "))

result = model.predict([[leafy, flower]])
print("Vegetable Type:", result[0])