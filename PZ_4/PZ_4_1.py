n = int(input("Введите число: "))
a = 0.0
for i in range(1, n + 1):
    b = (1 + i * 0.1) * (-1) ** (i + 1)

    a += b

print(a)
