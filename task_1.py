#Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
#для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
#и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

import collections

n = int(input('Введите количество предприятий: '))
companies = {}
avg_total = 0
for i in range(n):
    c_name = input(f'\nВведите название {i+1}-го предприятия: \n')
    sum_cash = 0
    for j in range(0, 4):
        quarter = int(input(f'Введите прибыль {i+1}-го предприятия за {j + 1}-ый квартал года: '))
        sum_cash = sum_cash + quarter
    avg_company = sum_cash / 4
    companies[c_name] = avg_company
    avg_total = avg_total + avg_company
avg_total = avg_total / n

print('\nСредний показатель прибыли по всем компаниям: ', avg_total)

print('\nКомпании со средним показателем прибыли выше среднего:\n')
for i in companies:
    if companies[i] > avg_total:
        print(i)

print('\nКомпании со средним показателем прибыли ниже среднего:\n')
for i in companies:
    if companies[i] < avg_total:
        print(i)





