import random


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'

chars = ''

cntPw = input('Укажите количество паролей для генерации:')
lenPw = input('Укажите длину одного пароля:')
digOn = input('Включать ли цифры 0123456789? (y/n)')
ABCon = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n)')
abcOn = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n)')
chOn = input('Включать ли символы !#$%&*+-=?@^_? (y/n)')
excOn = input('Исключать ли неоднозначные символы il1Lo0O? (y/n)')

for _ in range(5):
    if cntPw == 'y':
        chars += DIGITS
    if ABCon == 'y':
        chars += UPPERCASE_LETTERS
    if abcOn == 'y':
        chars += LOWERCASE_LETTERS
    if chOn == 'y':
        chars += PUNCTUATION
    if excOn == 'y':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    return password

for _ in range(int(cntPw)):
    print(generate_password(int(lenPw), chars))