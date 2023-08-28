from random import randint
from functools import reduce
n = int(input())
m = [[randint(0,100) for i in range(n)] for j in range(n)]
print(m)
c = sorted(m)
result = c[-1]
print(result)
x = reduce(max, result)
print(x)