#2*1=2
#STRING FORMAT

row1="2*1={}".format(2*1)
print(row1)
row2="2*1={}".format(2*2)
print(row2)
row3="2*1={}".format(2*3)
print(row3)
row4="2*1={}".format(2*4)
print(row4)
row5="2*1={}".format(2*5)
print(row5)

#another way
n = int(input("enter the number\n"))
print(f'Table of {n} is')
print(f'{n} x 1 = {n*1}')
print(f'{n} x 2 = {n*2}')
print(f'{n} x 3 = {n*3}')
print(f'{n} x 4 = {n*4}')
print(f'{n} x 5 = {n*5}')