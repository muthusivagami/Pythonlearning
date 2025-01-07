#maximum of three numbers using if loop

x=int(input("enter the number1"))
y=int(input("enter the number2"))
z=int(input("enter the numberr3"))
if(x>y and x>z):
    print(x, "is maximum")
elif(y>x and y>z):
    print(y, "is maximum")
else:
    print(z, "is maximum")

 #another way
    a = 10
    b = 20
    c=30
    output = None
    if(a>b and a>c):
        output=a
    elif(b>a and b>c):
        output=b
    else:
        output=c
        print(output)