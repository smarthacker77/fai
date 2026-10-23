room = {"A": "Dirty", "B": "Dirty"}
location = "A"

while "Dirty" in room.values():
    print("Location:", location)
    print("Room Status:", room[location])

    if room[location] == "Dirty":
        print("Action: Clean")
        room[location] = "Clean"
    else:
        print("Action: Move")

    if location == "A":
        location = "B"
    else:
        location = "A"

print("All rooms are clean")