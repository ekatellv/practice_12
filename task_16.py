def brackets(text):
    count = 0
    for i in text:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


print(brackets('ппарар(парарар)раррара(мрр(пппара)ррар(про))'))
