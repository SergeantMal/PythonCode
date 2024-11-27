#Объявление функции

def bank(a, years, procent = 10):
    for _ in range(years):
        a += a * (procent / 100)
    return a

#Ввод данных

a = float(input('Введите сумму вклада: '))
years = int(input('Введите количество лет: '))

#Вывод данных

print(f'Сумма вклада через {years} лет составит {bank(a, years)}')