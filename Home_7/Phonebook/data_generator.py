
from random import randint


names = ['Kevin', 'Piter', 'Bob', 'Evgen', 'Doom', 'Aristotel', 'Mark','Jon', 'Conor', 'Anderson']
lastnames = ['Silva', 'Smith', 'Uragun', 'Poker', 'Hooker', 'Zoomer', 'Alhogol','Smile', 'Niner', 'Ten-ten']

def user_generate():
    file = open('Phonebook/user.csv', 'w', encoding='utf-8')
    id = 1
    title = f'id; имя; фамилия; Номер телефона\n'
    phone: int
    for name in names:
        for lastname in lastnames:
            result = f'{id} {name} {lastname} {randint(9000000000, 9999999999)}\n'
            file.write(result)
            id += 1
    file.close()