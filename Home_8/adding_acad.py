

def add_acad(word):
    f = open('Home_8/magazine.txt', 'r+')
    for line in f:
        if word in line:
            print(line)


add_acad("Piter Hooker")