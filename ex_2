text = input('введите текст: ')
letter = 1
max_letter = 1
for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        letter += 1
    else:
        if letter > max_letter:
            max_letter = letter
        letter = 1
if letter > max_letter:
    max_letter = letter
print(max_letter)
