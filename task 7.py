# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника, составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
a = int(input('Введите значение стороны a треугольника: '))
b = int(input('Введите значение стороны b треугольника: '))
c = int(input('Введите значение стороны c треугольника: '))

if (a + b) <= c or (a + c) <= b or (b + c) <= a:
    print('Треугольник с такими сторонами не может существовать')
elif a!= b and b!= c and a != c:
    print('Это разносторонний треугольник')
elif a == b and b == c and a == c:
    print('Это равносторонний треугольник')
else:
    print('Это равнобедренный треугольник')