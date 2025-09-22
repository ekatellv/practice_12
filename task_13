count = 0
while True:
    ticket = input('введите номер билета: ')
    count += 1
    if len(ticket) % 2 != 0:
        continue
    half = len(ticket) // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    f_sum = sum(int(x) for x in first_half)
    s_sum = sum(int(x) for x in second_half)
    if f_sum == s_sum:
        print(count)
        break
