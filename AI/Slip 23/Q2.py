list1 = [10, 20, 30]
print("Original List:", list1)

list1.append(40)
print("After Append:", list1)

list1.extend([50, 60])
print("After Extend:", list1)

list1.insert(1, 15)
print("After Insert:", list1)

list1.remove(30)
print("After Remove:", list1)

del list1[0]
print("After Delete:", list1)