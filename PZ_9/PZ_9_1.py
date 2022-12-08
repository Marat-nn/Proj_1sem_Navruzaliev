# Сгенерировать словарь вида {0: 0, 1: 1,2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы. Отобразить исходный и удалить из него
# первый и последний элементы. Отобразить исходный и получившийся словарь.
# Использовать for, range

def multiply(num):
    outp = num
    for i in range(2):
        outp *= num
    return outp


numbers = dict()

for i in range(7):
    numbers[i] = multiply(i)

print(numbers)

del numbers[0]
del numbers[6]

print(numbers)