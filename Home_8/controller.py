import view, adding_std, adding_sub, show_student, show_all_std

def button():
    flag = True
    while flag == True:
        a = view.viewer()
        if a == 1:
            adding_std.add_std(view.std_name())
        if a == 2:
            adding_sub.add_sub(view.sub_name())
        if a == 3:
            pass
        if a == 4:
            show_all_std.s_a_s()
        if a == 5:
            show_student.s_s(view.std_name())
        if a == 4:
            pass
        if a == 0:
            flag = False

        

button()