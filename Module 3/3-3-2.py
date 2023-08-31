import re
a = ('''Было просто пасмурно, дуло с севера
     А к обеду насчитал сто градаций серого.
     Так всегда первого ноль девятого
     То ли весь мир сошёл с ума, то ли я - того...
     На столе записка от неё смятая
     Недопитый виски допивая с матами.
     Посмотрю в оно, допишу главу
     Первое сентября, дворник жжёт листву.
     Серым облакам наплевать на нас
     Если знаешь как жить - живи
     Ты хотела плыть как все - так плыви!''')
delimiters = [';', ',', ':', '.', '|', ' ', '\n', '-']
pattern = re.compile("|".join(map(re.escape, delimiters)))
result = pattern.split(a)
def lenwd(txt):
    shortwords = []
    for word in txt:
        if len(word) < 5 and len(word) > 0:
            shortwords.append(word)
            continue

    return shortwords
s = lenwd(result)
print(s)


