students = {
    "Amit": 85,
    "Rahul": 92,
    "Priya": 78,
    "Sneha": 95
}

print("Student Records:")
for name, percentage in students.items():
    print(name, ":", percentage, "%")

topper = max(students, key=students.get)

print("Topper:", topper)
print("Percentage:", students[topper], "%")