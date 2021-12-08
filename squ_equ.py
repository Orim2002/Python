a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
des = (b ** 2 - 4 * a * c)
if des >= 0:
    x1 = (-b + des ** 0.5) / (2 * a)
    x2 = (-b - des ** 0.5) / (2 * a)
    if x1 == x2:
        print("x:", x1)
    else:
        print("x1:", x1, "x2:", x2)
else:
    print("No solution")
