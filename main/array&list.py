i=[10,20,30,40]
for j in i:
    print(j)
    op:10
          #20
          #30
          #40
j=0
while j<len(i):
    print(i[j])
    j+=1 
    op:10
    20
    30
    40

                     
#single dimentional array 
print(i[0]) #op:10
print(i[1]) #op:20
print(i[2]) #op:30
print(i[3]) #op:40
i.append(50)
print(i) #op:[10, 20, 30, 40, 50]

#2d dimentional array 
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(a)



#list methods
#append(value)
i=[10,20,30,40]
i.append(50)
print(i) #op:[10, 20, 30, 40, 50]
#insert(index,value)
i.insert(4,60)
print(i) #op:[10, 20, 30, 40, 60, 50]

#H=index(specific index no.)
h=i.index(30)
print(h) #op:2

#remove(specific value)
i.remove(60)
print(i)#op:[10, 20, 30, 40, 50]
 
#sort(given list value convert into asscending value)
h=[90,50,30,50,60]
h.sort()
print(h)#op:[30, 50, 50, 60, 90]

#reverse(empty)
i.reverse()
print(i)#op:[50, 40, 30, 20, 10]

#pop(give index value)
i.pop(4)
print(i)#op:[50, 40, 30, 20]

#clear(empty)
i.clear()
print(i)#op:[]

#update[]
kh=[90,50,30,50,60]
kh[1]=66
print(kh)#op:90, 66, 30, 50, 60]


s1="listen"
s2="silent"

print(sorted(s1)==sorted(s2))