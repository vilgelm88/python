# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import deque

n1 = input('Введите первое число: ')
n1 = list(n1)
n2 = input('Введите второе число: ')
n2 = list(n2)

#print(n1, n2)

numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(n1) > len(n2):
    n1, n2 = n2, n1
#print(numbers)

j = -1
k = 0

n2 = deque(n2)
n2.reverse()
n2 = list(n2)

n3 = []
n3 = deque(n3)
#print(n3)


for i in n2:
    a = numbers.index(i)
    b = numbers.index(n1[j])
    n3.appendleft(numbers[(a + b + k) % 16])
    if (a + b) >= 15:
        k = 1
    else:
        k = 0
    j -= 1
    if j == -len(n1) - 1:
        break
delta = len(n2) - len(n1)

print(delta)
print('-delta:', [-delta])


if delta:
    for i in n2[-delta:]:
        n3.appendleft(numbers[(numbers.index(n2[-delta]) + k) % 16])
        if numbers.index(n2[-delta]) + 1 >= 15:
            k = 1
        else:
            k = 0
if k == 1:
    n3.appendleft('1')

print(n3)

