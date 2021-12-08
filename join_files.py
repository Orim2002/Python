def join_file(path1: str, path2: str, path3: str):
    """

    :param path: gt a path
    :return: how many words are in the file
    """

    with open(path1, "rb") as file:
        data = file.read()
    with open(path2, "rb") as file:
        data += file.read()
    with open(path3, "wb") as file:
        file.write(data)


join_file(r"C:\Users\o2002\Desktop\Txt1.txt", r"C:\Users\o2002\Desktop\Txt2.txt",
          r"C:\Users\o2002\Desktop\Txt3.txt")
