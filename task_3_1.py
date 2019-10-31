#Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random
from collections import deque

m = int(input('Введите m: '))
SIZE = 2 * m + 1
print(SIZE)

MIN = -100
MAX = 100

arr = [random.randint(MIN, MAX) for _ in range(SIZE)]
print('Сгенерированный массив чисел: ', arr)

def gnom_sort(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1
            if i == 0:
                i = 1
    return arr

arr = gnom_sort(arr)
print('Отсортированный массив чисел: ', arr)

def median(arr):
    i = int(len(arr) / 2)
    med = arr[i]
    return med

med = median(arr)
print('Медиана массива: ', med)