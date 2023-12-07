direction = input('шифрование??(+ = yes/- = no): ')
_direction = True if direction == '+' else False
_language = input('язык алфавита(ru/en): ')
_step = int(input('шаг сдвига (со сдвигом вправо): '))
user_string = input('Введите ваш текст: ')


def code_caesrs(direction, language, step, text):
    cripted_string = ''
    step = step if direction else step*-1
    for letter in text:
        if letter == ' ':
            cripted_letter = letter
        else:
            cripted_letter = chr(ord(letter) + step)
        cripted_string += cripted_letter
    print(cripted_string)


code_caesrs(_direction, _language, _step, user_string)
