Limit = int(input("Enter data: "))
IsPrime = [False for _ in range(Limit)]
for Number in range(2, Limit):
    IsPrime[Number] = True
for Number in range(2, Limit):
    if IsPrime[Number] == True:
        print(f"{Number}")
        for Multiple in range(2, (Limit // Number)):
            IsPrime[(Number * Multiple)] = False
