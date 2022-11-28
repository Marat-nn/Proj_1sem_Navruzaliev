# Описать функцию Minmax(X, Y), записывающую в переменную Х минимальное из значений X Y, а в переменную Y - максимальное из этих значений
# (X Y - вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из данных чисел A,B,C,D.


def numbers():
    a, b, c, d = int(input("Введите число А: ")), \
                 int(input("Введите число B: ")), \
                 int(input("Введите число C: ")), \
                 int(input("Введите число D: "))
    return list([a, b, c, d])


numbersList = list

try:
    numbersList = numbers()
    print(min(numbersList))
    print(max(numbersList))
except ValueError:
    print("Вводите целые числа")
