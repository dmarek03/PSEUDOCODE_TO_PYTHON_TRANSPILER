print("Enter a number: ")
NumA = input("Enter data: ")
print("Enter another number: ")
NumB = input("Enter data: ")
NumA = float(NumA)
NumB = float(NumB)
print("Enter operator: ")
Operator = input("Enter data: ")
match Operator:
    case "add":
        print((NumA + NumB))
    case "sub":
        print((NumA - NumB))
    case "mul":
        print((NumA * NumB))
    case "div":
        print((NumA / NumB))
    case "mod":
        print((NumA % NumB))
    case _:
        print("Unknown operator")
