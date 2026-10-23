utility = {
    "Walk": 5,
    "Bus": 8,
    "Train": 9,
    "Car": 6
}

print("Available actions and utility:")
for action, value in utility.items():
    print(action, ":", value)

best = max(utility, key=utility.get)

print("Best action:", best)
print("Highest utility:", utility[best])