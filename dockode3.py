n = int(input("Enter a columns :"))
r = int(input("Enter a rows : "))
for a in range(0, r):
    for i in range(0, n):
        if i == 0:
            for x in range(i, int(n/2) + 1):
                print(end="   ")
                print("___", end="      ")
            print()
        elif i == 1:
            for x in range(i, int(n/2) + 2):
                print(" /     \ ", end="")
                if i == 1:
                    print("___", end="")
        elif i == 2:
            print()
            for x in range(i, int(n/2) + 3):
                print(" \ ___ / ", end="   ")
