
number = int(input("Enter your number: "))
row1_column1 = 0
row1_column2 = 0
row2_column1 = 0
row2_column2 = 0
if number == 1:
    row1_column1 = 1
    row1_column2 = 2
    row2_column1 = 2
    row2_column2 = 1
elif number == 2:
    row1_column1 = 2
    row1_column2 = 1
    row2_column1 = 1
    row2_column2 = 2
else:
    print("Doesn't exist, please enter number 1 or 2")
print(f"Here is your sudoku board:\n{row1_column1} {row1_column2}\n{row2_column1} {row2_column2}")
