import copy
import math
from datetime import datetime, timedelta


class Date(object):
    def __init__(self):
        self.day = int(input("Enter day: "))
        if self.day < 1 or self.day > 31:
            self.day = int(input("ReEnter day: "))
        self.month = int(input("Enter month: "))
        while self.month < 1 or self.month > 12:
            self.month = int(input("ReEnter month: "))
        self.year = int(input("Enter year: "))
        if self.month in [4, 6, 9, 11] and self.day == 31:
            print("In month", self.month, "there are 30 days")
            print("Enter new date:")
            self.__init__()
        if self.month == 2 and self.day > 28:
            if self.year % 400 == 0 or (self.year % 100 != 0 and self.year % 4 == 0):
                if self.day > 29:
                    print("In month", self.month, "there are 29 days")
                    print("Enter new date:")
                    self.__init__()
            else:
                print("In month", self.month, "there are 28 days")
                print("Enter new date:")
                self.__init__()

    def print(self):
        print(self.day, "/", self.month, "/", self.year)

    def __add__(self, days: int):
        specific_date = datetime(self.year, self.month, self.day)

        new_date = specific_date + timedelta(days)
        date1 = copy.deepcopy(self)
        date1.day = new_date.day
        date1.month = new_date.month
        date1.year = new_date.year
        return date1

    def __sub__(self, other):
        specific_date = datetime(self.year, self.month, self.day)
        sub_date = datetime(other.year, other.month, other.day)
        days = specific_date - sub_date
        return days.days

    def __eq__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 == date2

    def __lt__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 < date2

    def __gt__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 > date2

    def __le__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 <= date2

    def __ge__(self, other):
        date1 = datetime(self.year, self.month, self.day)
        date2 = datetime(other.year, other.month, other.day)
        return date1 >= date2


first_date = Date()
first_date.print()
second_date = first_date + int(input("Enter Days: "))
second_date.print()
print(second_date - first_date)
print(second_date + (-556) == first_date)
