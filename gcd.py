x = int(input())
y = int(input())
if x == 1:
    print(y)
elif y == 1:
    print(x)
else:
    while y != 0:
        tmp = x
        x = y
        y = tmp % y
    print(x)
