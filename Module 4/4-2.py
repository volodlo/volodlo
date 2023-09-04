def insert_sort(massive):
    for i in range(1, len(massive)):
        temp = massive[i]
        j = i - 1
        while (j >= 0 and temp < massive[j]):
            massive[j + 1] = massive[j]
            j = j - 1
        massive[j + 1] = temp

massive = input('Enter the list of numbers: ').split()
massive = [int(x) for x in massive]
insert_sort(massive)
print('Sorted list: ', end='')
print(massive)