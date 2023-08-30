a=int(input('Введите сторону a '))
b=int(input('Введите сторону b '))
c=int(input('Введите сторону c '))
def per(a, b, c):
    return a + b + c
def area(a, b, c):
    p = per(a, b, c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** .5
print(area(a, b, c))