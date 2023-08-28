
x = int(input('Введите число: '))
y = 0
while x != 0:
    y = y + x % 10
    x = x // 10
print('Сумма равна: ', y)
