#Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random

SIZE = 11
MIN = 0
MAX = 50

arr = [random.uniform(MIN, MAX) for _ in range(SIZE)]
print('Сгенерированный массив чисел: ', arr)


def merge(a, b):
    sorted_array = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            sorted_array.append(a[i])
            i += 1
        else:
            sorted_array.append(b[j])
            j += 1
    sorted_array += a[i:]
    sorted_array += b[j:]

    return sorted_array

#a = [1, 3, 4]
#b = [2, 4, 6]
#print(merge(a, b))

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    a = mergesort(arr[:middle])
    b = mergesort(arr[middle:])
    return merge(a, b)

print('Отсортированный массив чисел: ', mergesort(arr))
