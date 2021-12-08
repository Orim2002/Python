class Preson(object):
    def __init__(self):
        self.first_name = input("Enter first name: ")
        while self.first_name == "" or not all(x.isalpha() or x.isspace() for x in self.first_name):
            self.first_name = input("ReEnter first name: ")
        self.last_name = input("Enter last name: ")
        while self.last_name == "" or not all(x.isalpha() or x.isspace() for x in self.last_name):
            self.last_name = input("ReEnter last name: ")
        self.age = input("Enter age: ")
        while not self.age.isdigit():
            self.age = input("ReEnter age: ")
        self.age = int(self.age)


class Talker(Preson):
    def __init__(self):
        Preson.__init__(self)

    def talk(self, text: str):
        print(text)


class HappyTalker(Talker):
    def __init__(self):
        Talker.__init__(self)

    def talk(self, text: str):
        print(text + "!!!")


class SlowTalker(Talker):
    def __init__(self):
        Talker.__init__(self)

    def talk(self, text: str):
        # talk += " ".join(text) //second option
        talk = ""
        for ch in text:
            talk += ch
            talk += " "
        print(talk)


class StutterTalker(Talker):
    def __init__(self):
        Talker.__init__(self)

    def talk(self, text: str):
        lst = text.split()
        talk = ""
        for item in lst:
            tmp = item[0] * 2
            tmp += item
            talk += tmp
            talk += " "
        print(talk)


def makeThemTalk(talkerList: list, sayWhat: str):
    for talker in talkerList:
        if talker.age > 10:
            print(talker.first_name, talker.last_name + ":")
            talker.talk(sayWhat)


talkerList = [Talker(), StutterTalker(), SlowTalker(), StutterTalker(), HappyTalker()]
makeThemTalk(talkerList, "I love pizza")
