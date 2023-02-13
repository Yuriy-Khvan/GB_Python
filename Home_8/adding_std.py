



def add_std(a):
    f1 = open('Home_8/magazine.txt', 'a')
    f2 = open('Home_8/subjects.txt', 'r')
    f3 = open('Home_8/students.txt', 'a')
    f3.write(f'\n{str(a)}')
    b = ''
    for f2.read in f2:
        c = f2.read.splitlines()
        b = b + str(c)
    f1.write(f"['{str(a)}']{str(b)} \n")
    f1.close()
    f2.close()
    f3.close()


add_std('Ivan Petov')