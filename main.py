import random

answer = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я помогу тебе с ответами в своей жизни.')
print('Как тебя звать друг мой?')
name = input()
while True:
    ball = input('Задайте свой вопрос')
    print(random.choice(answer))
    again = input('Попробовать снова? Да или Нет?')
    if again == 'Нет' or again == 'нет':
        print('Буду ждать твоего возвращения<3')
        break
