# Дан список A размера N. Сформировать новый список В того же размера по следующему правилу:
# элемент Вк равен сумме элементов списка А с номерами от 1 до К
from random import random


def createlistb(c):
    d = 0
    e = c
    while e >= 0:
        d += A[e]
        e -= 1
    B.append(int(d))


N = int(input("Введите размер списка "))
A = []
B = []

for i in range(N):
    A.append(int(random() * 20))

print(A)

e = 0
while e < len(A):
    createlistb(e)
    e += 1

print(B)
