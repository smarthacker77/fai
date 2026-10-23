monkey = "floor"
box = "middle"
banana = "high"

if monkey == "floor":
    print("Monkey moves to box")
    monkey = "box"

if monkey == box:
    print("Monkey climbs box")
    monkey = "on box"

if monkey == "on box" and banana == "high":
    print("Monkey gets banana")