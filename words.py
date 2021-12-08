def words_count(file_name: str):
    f = open(file_name, "rb")
    data = f.read()
    data = data.decode("utf-8")
    lst = data.split()
    x = len(lst)
    f.close()
    return x


def words_appear(file_name: str):
    f = open(file_name, "rb")
    data = f.read()
    data = data.decode("utf-8")
    dictionary = {}
    lst = data.split()
    for item in lst:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    f.close()
    return dictionary


def print_dict(dictionary: dict):
    dict_keys = dictionary.keys()
    dict_items = dictionary.items()
    for key in dict_keys:
        print(str(key) + ":" + str(dictionary.get(key)))


print("There are", words_count(r"C:\Users\o2002\Desktop\Txt1.txt"), "words in the file")
print("\nWords dictionary:")
print_dict(words_appear(r"C:\Users\o2002\Desktop\Txt1.txt"))
