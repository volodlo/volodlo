x = float(input())
p = float(input())
y = float(input())
i = 0
t = p/100
while x < y:
    x = (x+(x*t)) // 1
    i = i+1
print(i)