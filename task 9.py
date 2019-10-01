a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if c < a < b or b < a < c:
    print(f'Среднее число {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число {b}')
else:
    print(f'Среднее число {c}')

