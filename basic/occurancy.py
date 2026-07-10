
h=[int(c) for c in input().split(",") ]
n=int(input())

c=0
for i in h:
    if i==n:
        c +=1
        
print(c)








#1,2,3,2,1,4,2,5
a=1,2,3,2,1,4,2,5
#h=[int(c) for c in a]
count=a.count(2)
print(count)