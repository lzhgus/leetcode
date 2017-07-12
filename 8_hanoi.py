def hanoi(n, origin, destination, buffer):
    if n == 1:
        move(1, orgin, destination)
    else:
        hanoi(n-1, origin, buffer, destination)
        move(n, origin, destination)
        hanoi(n-1, buffer, destination, origin)

def move(n, a, b):
    print(c + "time move number " + n + " from " + a + " to " + b)
    c+=1

c = 0
hanoi(3, "A", "B", "C")
