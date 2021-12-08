def fibonacci(index: int):
    if index == 1:
        return 1
    if index == 2:
        return 1
    return fibonacci(index - 1) + fibonacci(index - 2)


x = input()
if x.isdigit() and int(x) > 0:
    print(fibonacci(int(x)))
else:
    print("Wrong input!")


