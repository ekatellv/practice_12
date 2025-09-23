from collections import Counter
symbols = Counter(input('введите текст: '))
for i,j in symbols.items():
    if j == 3:
        print(i)
