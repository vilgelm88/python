#Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN = -100
MAX = 100

arr = [random.randint(MIN, MAX) for _ in range(SIZE)]
print('Сгенерированный массив чисел: ', arr)

def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        i += 1
        #print(arr)
    return(arr)


print('Отсортированный массив чисел: ', bubblesort(arr))
