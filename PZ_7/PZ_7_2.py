# Дана строка, состоящая из русских слов, набранных заглавными буквами
# и разделенных пробелами (одним или несколькими). Найти количество слов,
# которые начинаются и заканчиваются одной и той же буквой.

line = input("введите строку: ")
list_lines = list(line.split())
count_word = 0
for count in range(0, len(list_lines)):
    temp = list_lines[count]
    if ord(temp[0]) == ord(temp[len(temp) - 1]):
        count_word += 1
print(count_word)
