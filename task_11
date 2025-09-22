def winner(text):
    cities = text.split()

    if not cities:
        return 'Вася'
    for i in range(1, len(cities)):
        previous_city = cities[i - 1]
        current_city = cities[i]
        if previous_city[-1].lower() != current_city[0].lower():
            if i % 2 == 1:
                return 'Петя'
            else:
                return 'Вася'
    if len(cities) % 2 == 1:
        return 'Петя'
    else:
        return 'Вася'


print(winner('москва архангельск омск'))
