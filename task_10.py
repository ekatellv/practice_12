words = input('Введите предложение: ').split()
for i in range(1, len(words)):
    if words[0] != words[i] and len(set(words[i])) == len(words[i]):
        print(words[i])
