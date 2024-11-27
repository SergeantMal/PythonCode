# Объявление функции
def sum_range(start, end):
    result = 0
    for i in range(start, end + 1):
        result += i
    return result

# Ввод переменных
a, b = int(input('Введите начало диапазона: ')), int(input('Введите конец диапазона: '))

# Вывод результата
print(f'Сумма чисел в диапазоне от {a} до {b} равна {sum_range(a, b)}')  
