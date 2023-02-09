
from view_file import for_export

def export_fun(file):
    file = open('Phonebook/user.csv', 'r')
    a = True
    c = for_export()
    while a:
        file_line = file.readline()
        b = file_line.split(' ')
        if c == b[0]:
            return b[1] + ' ' + b[2]
        if not file_line:
            a = False
    file.close()
