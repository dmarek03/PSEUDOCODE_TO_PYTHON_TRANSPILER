def Factorial(Num: int) -> int:
    if Num == 0 or Num == 1:
        return 1
    else:
        return Num * Factorial((Num - 1))
