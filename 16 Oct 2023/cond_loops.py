#condition - set of rules

#ifloop
age = int(input("Enter the age"))
if age >= 18:
    print("You can watch the movie")
else:
    print('You cant')
#if loop with elseif
x=int(input("enter the number1"))
y=int(input("enter the number2"))
if x>y:
    print(x, "is greater than" ,y)
elif x<y:
    print((x, "is lesser than" ,y))
else:
    print((x, "is equal to", y))