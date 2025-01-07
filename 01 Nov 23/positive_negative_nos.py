numbers=[-3,-2,-1,0,1,2,3,4]
def pos(num):
    return num>0
def neg(num):
    return num<0
#positive number
x=filter(pos,numbers)
print(x)
print(list(x))
#negative number
y=filter(neg,numbers)
print(list(y))