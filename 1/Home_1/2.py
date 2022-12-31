day_week = int(input('Введите номер дня недели (1-7): '))
if day_week <=5:
    print('Идем на работу(((, не выходной')
elif day_week == 6 or day_week==7:
    print('Ура, выходной!!! Отдыхаем!')
else:
    print('Эй, дружок, в неделе всего 7 дней!')


# all((not (x or y or z)) == (not x and not y and not z) for x in (True, False) for y in (True, False) for z in (True, False))