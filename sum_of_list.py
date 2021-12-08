quantity = int(input())
lst = []
sum_of_elements = 0
for i in range(quantity):
    x = int(input())
    lst.append(x)
    sum_of_elements += x
print("list:", lst)
print("sum:", sum_of_elements)
