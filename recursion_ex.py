# Task1
def pal(_str):
    if len(_str) < 2:
        return True
    elif _str[0] != _str[-1]:
        return False
    else:
        return pal(_str[1:-1])


number = input("Enter integer: ")
result = pal(number)
print(result)


# Task2
def iseven(x):
    if x < 2:
        return x % 2 == 0
    return iseven(x-2)


no = int(input("Enter integer: "))
result2 = iseven(no)
print("Even status:", result2)

