# Дан список размера N и целое число К (1 < К < N). Осуществить сдвиг
# элементов списка вправо на К позиций (при этом А1 перейдёт в Ак+1,
# А2 - в Ак+2, ..Аn+k - в An, а исходное значение К последних элементов будет потеряно).
# Первые К элементов полученного списка положить равными 0.
from random import random

N = int(input("Введите размер списка "))
K = int(input("Введите целое число "))
A = []
B = []
if 1 < K < N:
    for i in range(N):
        A.append(int(random() * 20))
        B.append(0)
    c = 0
    while N > K:
        B[K] = A[c]
        K += 1
        c += 1

print(A)
print(B)
