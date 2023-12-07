import random

random_int = random.randint(1, 100)
count = 0
new_game = 'y'

print('Добро пожаловать в числовую угадайку')


def is_valid(digit):
    return digit.isdigit() and 0 < int(digit) < 101


while new_game:
    number = input('Введите число от 1 до 100: ')
    check = is_valid(number)
    if not check:
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue
    my_digit = int(number)
    if my_digit < random_int:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        count += 1
        continue
    elif my_digit > random_int:
        print('Ваше число больше загаданного, попробуйте еще разок')
        count += 1
        continue
    else:
        print('Вы угадали, поздравляем!')
        print('Колличество затраченных попыток:', count)
        new_game = input('Введите y, если хотите начать сначала: ')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
