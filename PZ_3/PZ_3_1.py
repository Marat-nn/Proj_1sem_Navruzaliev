a, b, c = input("Введите первое число: "), input("Введите второе число: "), input("Введите третье число: ")
if type(a) != int and type(a) != int and type(a) != int:
    if a == b and b == c and a == c:
        print("Треугольник равносторонний")
    else:
        print("Треугольник не равносторонний")
else:
    print("Введите целые числа")
    