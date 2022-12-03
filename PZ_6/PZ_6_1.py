# Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся в списке,
# на исходное значение первого четного числа. Если четные числа в списке отсутствуют,
# то оставить список без изменений
from random import random

size = int(input("Введите размер списка "))
N = []

for i in range(size):
    N.append(int(random() * 100))

print(N)


def tofindfirsteven():
    first_even = 0
    n = 0
    c = True
    while c:
        if N[n] % 2 == 0:
            first_even = N[n]
            c = False
        n += 1
    return first_even


even_number = tofindfirsteven()
print(even_number)
for i in range(len(N)):
    if N[i] % 2 == 0:
        N[i] += even_number

print(N)
