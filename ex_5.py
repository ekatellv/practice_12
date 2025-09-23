str_1 = set(input('введите строчку 1: '))
str_2 = set(input('введите строчку 2: '))
str_3 = set(input('введите строчку 3: '))
only_1 = str_1 - str_2 - str_3
only_2 = str_2 - str_1 - str_3
only_3 = str_3 - str_1 - str_2
print(only_1 | only_2 | only_3)
