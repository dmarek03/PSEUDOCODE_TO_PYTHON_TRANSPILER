# Declaration and implementation of function calculating factorial of given number
def Factorial(Num: int) -> int:
    if Num == 0 or Num == 1:
        return 1
    else:
        return Num * Factorial((Num - 1))


# Getting number from user
Number = input("Enter data: ")
Number = int(Number)
print(Factorial(Number))
