import random


ANSWERS = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

new_game = 'y'

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут?')
print(f'Привет {name}.')

while new_game=='y':
    question = input('Скажи свой вопрос.')
    print(random.choice(ANSWERS))
    new_game = input('У тебя остались вопросы?(y/n)')

print('Возвращайся если возникнут вопросы!')
