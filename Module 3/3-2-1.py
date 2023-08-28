l = [1, 4, 1, 6, 'hello', 'a', '5', 'hello']
l_dp = []
for i in l:
    if l.count(i) > 1 and i not in l_dp:
        l_dp.append(i)
print(l_dp)