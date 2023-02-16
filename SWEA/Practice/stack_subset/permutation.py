from itertools import permutations, combinations
from pprint import pprint

a = range(1, 4)
b = list(permutations(a))
for i in b:
    print(i)

c = list(combinations(a, 3))
for i in c:
    print(i)