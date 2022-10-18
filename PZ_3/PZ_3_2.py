a, b, c, d, = input("Введите первое число: "), \
              input("Введите второе число: "), \
              input("Введите третье число: "), \
              input("Введите четвертое число: ")

if a == b and b == c:
    print(4)
else:
    if a == b and a == d:
        print(3)
    else:
        if a == c and a == d:
            print(2)
        else:
            if b == c and b == d:
                print(1)

