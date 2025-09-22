import keyword
import re


def name(text):
    if keyword.iskeyword(text):
        return 'нет, ключевое слово'
    if text[0].isdigit():
        return 'нет, начинается с цифры'
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', text):
        return 'нет, содержит недопустимые символы'
    else:
        return 'да, допустимое имя'


print(name('hello88'))
