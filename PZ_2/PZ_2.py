print("Введите положительное число")
days = ['вс', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб']
day = (input())

try:
    day = int(day)
    if day > 365 or day <= 0:
        print("Неправильно ввели")
    else:
        print(days[(day + 3) % 7])
except ValueError:
    print("Неправильно ввели")
