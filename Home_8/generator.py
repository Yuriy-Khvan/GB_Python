
names = ['Kevin', 'Piter', 'Bob', 'Evgen', 'Doom', 'Aristotel', 'Mark','Jon', 'Conor', 'Anderson']
lastnames = ['Silva', 'Smith', 'Uragun', 'Poker', 'Hooker', 'Zoomer', 'Alhogol','Smile', 'Niner', 'Ten']

def students_generate():
    file = open('Home_8/students.txt', 'w')
    for name in names:
        for lastname in lastnames:
            result = f'{name} {lastname}\n'
            file.write(result)
    file.close()
 
# students_generate()