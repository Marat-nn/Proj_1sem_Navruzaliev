# Дано целое число N(>0). С помощью операций деления нацело и взятия остатка от деления определить,
# имеется ли в записи числа N цифра "2".
# Если имеется, то вывести TRUE, если нет - вывести FALSE.

n = int(input("Введите число: "))
a = n
i = 0

result = False

while a >= 1:
    print(1)
    i += 1
    r = a % 10
    if r == 2:
        result = True
        break
    a = int(a / 10)

print(result)
