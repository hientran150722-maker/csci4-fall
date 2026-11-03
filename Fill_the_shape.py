
def fill(a:int, b:int)->int:
    distance=abs(a[0]-b[0])
    for i in range(0,distance):
        p=a[0]+i
        print(p)
c=[2,0]
d=[9,0]
print((fill(c,d)))







