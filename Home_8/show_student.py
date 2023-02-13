
def s_s(word):
    f = open('Home_8/magazine.txt', 'r+')
    for line in f:
        if word in line:
            print(line)
    f.close()