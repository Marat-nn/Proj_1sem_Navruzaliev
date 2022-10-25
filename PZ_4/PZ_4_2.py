n = int(input("Введите число: "))
a = n
i = 0

rezult = False

while a >= 1:
    i += 1
    r = a % 10
    if r == 2:
        rezult = True
        break
    a = int(a / 10)

print(rezult)
