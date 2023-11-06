x1=float(input("enter the side1"))
x2=float(input("enter the side2"))
x3=float(input("enter the side3"))
if(x1==x2==x3):
    print("It is a equilateral traingle")
elif(x1==x2 or x1==x3 or x2==x3):
    print("It is a isoceles triangle")
elif(x1!=x2!=x3):
    print("it is a scalene triangle")
