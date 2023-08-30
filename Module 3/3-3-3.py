list = [56, 9, 11, 2]
def key_func(num):
    return str(num) * 3
sorted_list = sorted(list, key=key_func, reverse=True)
largest_number = "".join([str(num) for num in sorted_list])
print('Максимально возможное число:', largest_number)