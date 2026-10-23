from sklearn.ensemble import RandomForestClassifier

X = [[20, 5], [25, 4], [40, 1], [50, 0],
     [22, 6], [45, 1], [30, 3], [55, 0]]

y = ["FIT", "FIT", "UNFIT", "UNFIT",
     "FIT", "UNFIT", "FIT", "UNFIT"]

model = RandomForestClassifier(random_state=1)
model.fit(X, y)

n = int(input("Enter number of people: "))

for i in range(n):
    age = int(input("Enter age: "))
    hours = float(input("Enter exercise hours per week: "))

    result = model.predict([[age, hours]])
    print("Fitness:", result[0])