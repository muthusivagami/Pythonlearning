#filter(function,values)
numbers=[1,2,3,4,5,6,7,8,9,10]
def even(num):
    return num%2==0
filter_nos=filter(even,numbers)
print(filter_nos)   #print the filter object number
print(list(filter_nos))
