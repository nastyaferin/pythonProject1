import random

numr = random.randint(0, 100)
attempt = 0
print('Угадай число от 1 до 100! У вас есть 10 попыток')
for i in range(1, 11):
    num = int(input(f'Введете число: '))
    if num < numr:
        print('больше')
    if num > numr:
        print('меньше')
    if num == numr:
        print(f'Ваше число {numr} Вы угадали с {i} попытки!')
        break
    attempt += 1
    if attempt >= 10:
        print(f'Вы исчерпали 10 попыток! Было загадано число {numr}!')

