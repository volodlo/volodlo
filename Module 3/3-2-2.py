from random import randint
n = int(input())
m = [[randint(0,100) for i in range(n)] for j in range(n)]
large = []
print(m)
for k in m:
    for i in k:
        large.append(i)
print(max(large))
