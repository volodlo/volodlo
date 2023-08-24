#Часть 1
#Уровень 1
print((5+((7*5)/8))/(3**5))
#Уровень 2
s = 109
v = int(input('Введите скорость: '))
t = int(input('Введите время = '))
x1 = v * t
if x1 < s:
    print(x1)
elif x1 > s:
    x2 = x1 % s
    print(x2)
#Уровень 3
x1 = float(input('Введите первое число: '))
x2 = float(input('Введите второе число = '))
if x1>x2:
    print('Max: ', x1)
elif x1<x2:
    print('Max: ', x2)
elif x1==x2:
    print('Числа равны')
#Часть 2
#Уровень 1
x1 = int(input('Введите первое число: '))
x2 = int(input('Введите второе число: '))
x3 = int(input('Введите третье число: '))
if x1 == x2 and x1 == x3:
    print(3)
elif x1 == x2 and x1 != x3 or x2 == x3 and x2 != x1:
    print(2)
elif x1 == x3 and x2 != x3:
    print(2)
elif x1 != x2 and x1 != x3:
    print(0)
#Уровень 2
x1 = int(input('Введите первую координату фигуры: '))
y1 = int(input('Введите вторую координату фигуры: '))
x2 = int(input('Введите первую координату клетки: '))
y2 = int(input('Введите вторую координату клетки: '))
if x1 == x2 or y1 == y2:
    print('Yes')
else:
    print('No')
#Уровень 3
password = str(input('Введите пароль: '))
while len(password) < 8 or password.islower() == 1:
    print('Пароль должен включать в себя 8 символов и более, а так же содержать буквы в верхнем и нижнем регистрах')
    password = input('Введите новый пароль: ')
print('Успешно')