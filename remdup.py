#a=10,20,30,20,40,10,50
a=input().split(",")
h=[int(item) for item in a]
newl=[]
for i in h:
    if i in newl:
        continue# used to skip repeated values and print remaining numbers
    else:
        newl.append(i)# append() used to add elements to the list
print(newl)#[10, 20, 30, 40, 50]

#method 2 
#a=10,20,30,20,40,10,50
a=input().split(",")
h=[int(c) for c in a]
s=set(h)
newl=list(s)
newl.sort()
print(newl)