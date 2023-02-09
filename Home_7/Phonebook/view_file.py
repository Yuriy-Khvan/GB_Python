
def choose():
    a = input('Хотите добавить или получить контакт? (+ добавить, - вывести): ')
    if a == "+":
        return "+"
    else:
        return "-"

def for_export():
    a = input('Введите ключевое слово: ')
    return a

def for_import():
    a = input('Введите  id имя фамилия номер телефона(без +7 и 8): ')
    return a

def print_export(a):
    print(a)