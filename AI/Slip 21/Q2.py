current = input("Enter current location (A/B/C): ").upper()
goal = input("Enter goal location (A/B/C): ").upper()

locations = ['A', 'B', 'C']

print("Current State:", current)
print("Goal State:", goal)

if current not in locations or goal not in locations:
    print("Invalid location")
elif current == goal:
    print("Action: Goal reached")
elif locations.index(current) < locations.index(goal):
    print("Action: Move Forward")
else:
    print("Action: Move Backward")