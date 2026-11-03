two_var = [[True,True],
           [True, False],
           [False, True],
           [False,False]]

and_con = [[True, True, True, True, True],
           [True, True, False, True, False],
           [True, False, False, False, True],
           [True, False, True, False, True],
           [False, True, True, False, True],
           [False, True, False, False, True],
           [False, False, False, False, True],
           [False, False, True, False, True]]

three_col = [[True,True,True],
            [True,False,True],
            [True,True,False],
            [True,False,False],
            [False,True,True],
            [False,False,True],
            [False,True,False],
            [False,False,False]]

def formular_1_ex():
    for i in three_col:
        if i[0] == True and i[1] == True:
            i.append(True)
        else:
            i.append(False)
        if i[3] == False or (i[2] == True and i[3]== True):
            i.append(True)
        else: 
            i.append(False)

        print(i)

formular_1_ex()
