Limit = int(input("Enter data: "))
IsPrime = [False for _ in range(Limit)]
for Number in range(2, Limit, 1):
    IsPrime[Number] = True
for Number in range(2, Limit, 1):
    if IsPrime[Number] == True:
        print(Number)
        for Multiple in range(2, (Limit // Number), 1):
            IsPrime[(Number * Multiple)] = False
