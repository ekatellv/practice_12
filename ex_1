text = input('введите текст: ')
space = 0
max_space = 0
for i in range(len(text)):
    if text[i] == ' ':
        space += 1
    else:
        if space > max_space:
            max_space = space
        space = 0
if space > max_space:
    max_space = space
print(max_space)
