# Даны строки S и S0. Проверить, содержится ли строка S0 в строке S.
# Если содержится,то вывести TRUE, если не содержится, то вывести FALSE

S = str(input())
S0 = str(input())

print(S.__contains__(S0))