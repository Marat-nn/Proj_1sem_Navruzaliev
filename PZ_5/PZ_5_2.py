# Описать функцию Minmax(X, Y), записывающую в переменную Х минимальное из значений X Y, а в переменную Y - максимальное из этих значений
# (X Y - вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из данных чисел A,B,C,D.


def numbers():
    a, b, c, d = int(input("Введите число А: ")), \
                 int(input("Введите число B: ")), \
                 int(input("Введите число C: ")), \
                 int(input("Введите число D: "))
    return list([a, b, c, d])


def minValue():
    minNum = numbersList[0]
    for i in numbersList:
        if minNum >= i:
            minNum = i
    print(minNum)


def maxValue():
    maxNum = numbersList[0]
    for i in numbersList:
        if maxNum <= i:
            maxNum = i
    print(maxNum)


numbersList = list

try:
    numbersList = numbers()
    maxValue()
    minValue()
except ValueError:
    print("Вводите целые числа")
