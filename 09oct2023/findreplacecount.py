#replace
text= "hello welcome"
gentext = text.replace("welcome","python")
print(gentext)

#find - lowest index of the substring in a string - return -1 if substring is not found

h1= "hello world"
r1=h1.find("world")
print(r1)  #it will print the index of world - w starts with index 6

#count
r2=h1.count("l")
print(r2) #count the number of l in h1
