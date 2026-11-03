table_col = [[True, True, True],
         [True, False, True],
         [True, True, False],
         [True, False, False],
         [False, True, True],
         [False, False, True],
         [False, True, False],
         [False, False, False]]

def prop_1():
    for i in table_col:
        if i[0] == True and i[1] == True:
            i.append(True)
        else: 
            i.append(False)
        if (i[2] == True and i[3] == True) or (i[2] == False and i[3] == False):
            i.append(True)
        else:
            i.append(False)
         
        print(i)

prop_1()

