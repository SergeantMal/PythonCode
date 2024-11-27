from math import sqrt

#Объявление функции

def square(x):
    S = x**2
    P = 4*x
    d = sqrt(2)*x
    return S, P, d

#Ввод данных
storona = float(input('Введите длину стороны квадрата: '))

#Вызов функции

a, b, c = square(storona)
print(f'Площадь квадрата = {a}\nПериметр квадрата = {b}\nДиагональ квадрата = {c}')
