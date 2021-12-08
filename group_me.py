def mod3(x: int):
    return x % 3


def group(func, lst: list):
    dictionary = {}
    for item in lst:
        x = func(item)
        if x in dictionary:
            dictionary[x].append(item)
        else:
            dictionary[x] = [item]
    dictionary = dict(sorted(dictionary.items()))
    return dictionary


print(group(mod3, [1, 3, 4, 5, 7, 9]))
