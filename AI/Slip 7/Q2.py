previous = input("Enter previous door status: ").upper()
current = input("Enter current door status: ").upper()

if previous not in ["OPEN", "CLOSED"] or current not in ["OPEN", "CLOSED"]:
    print("Error: Enter OPEN or CLOSED only")

elif previous == "CLOSED" and current == "OPEN":
    print("Alert! Door opened. Security alarm ON")

elif previous == "OPEN" and current == "CLOSED":
    print("Door closed. Security alarm OFF")

elif current == "OPEN":
    print("Warning! Door is still OPEN")

else:
    print("Door is CLOSED. Home is secure")