import math

prime_list = [i for i in range(2, 1001) if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1))]
print("Prime Numbers List\n", prime_list)
perfect_list = [x for x in range(1, 1001) if sum([y for y in range(1, int(x / 2) + 1) if x % y == 0]) == x]
print("Perfect Numbers List\n", perfect_list)
