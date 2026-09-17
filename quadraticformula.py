import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = float(b**2 - 4*a*c)
if d == 0:
    x = float((-b)/(2*a))
    print(f"There is one solution: x = {x}")
elif d > 0:
    x1 = float(((-b)+math.sqrt((d)))/(2*a))
    x2 = float(((-b)-math.sqrt(d))/(2*a))
    print(f"There is two solutions: \n x1 = {x1} \n x2 = {x2}")
else:
    print("There is no solutions.")




