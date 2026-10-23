def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(source, "to", destination)
    else:
        hanoi(n-1, source, destination, auxiliary)
        print(source, "to", destination)
        hanoi(n-1, auxiliary, source, destination)

n = int(input("Enter number of disks: "))
hanoi(n, 'A', 'B', 'C')