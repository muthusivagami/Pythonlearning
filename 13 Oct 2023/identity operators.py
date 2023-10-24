#Identity operators
#is returns true if both variables are the same object
#is not returns true if both variables are not the same object
x =[1,2,3]
y=[1,2,3]
print (x is y)
print(x is not y)
print(id(x)) #id is a unique number - returns the identity of the object
print(id(y))