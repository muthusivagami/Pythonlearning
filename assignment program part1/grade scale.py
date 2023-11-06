x=float(input("enter the number"))
if 90 <= x <= 100:
    print( 'A')
elif 80<= x <=89:
    print('B')
elif 70<=x<=79:
    print('C')
elif 60<=x<=69:
    print('D')
elif 50<=x<=59:
    print('E')
else:                          #we can also write as elif 0<=x<=49
    print('F')