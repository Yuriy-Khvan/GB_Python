
from view_file import for_import

def import_fun(a):
    file = open('Phonebook/user.csv', 'a')
    file.write(a + '\n') 
    file.close()