def my_map(func, lst: list):
    mapped_list = []
    for item in lst:
        mapped_list.append(func(item))
    return mapped_list


def fact(x: int):
    factorial = 1
    for i in range(x):
        factorial *= i + 1
    return factorial


print(my_map(len, ["Ori", "Maor"]))
print(my_map(fact, [1, 2, 3, 4, 5]))
