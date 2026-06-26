'''#aarry travveral method
i=[10,20,30,40]
for j in i:
    print(j)
op:
10
20
30
40

min=10
max=10
for j in i: #the loop used in treveral to visit all element in sequence
    if j >max:
       max=j
print("max:",max)# need tp print out side of loop then we get ouput like->op:40
for j in i:
    if j<=min:
        min=j
print("min:",min)#op:10


#find sum 
j=[10,20,30,40]
sum=0
for i in j:
    sum+=i
print("sum of list:",sum) #op:sum of list: 100

#cound even numbers
k=[1,2,3,4,5,6,7]
for i in k:
    if i%2==0:
        print(i)
#op:
2
4
6


#insertion in array
arr = [10, 20, 40]

arr.insert(2,30)
print(arr) #op:[10, 20, 30, 40]
#using loop 
arr = [10, 20, 40]
index = 2
value = 30

new_arr = []

for i in range(len(arr)):
    if i == index:
        new_arr.append(value)
    new_arr.append(arr[i])

print(new_arr) #op:[10, 20, 30, 40]
 
#inset at begging
i=[10, 20, 30, 40]
i.insert(0,5)
print(i)#op:[5, 10, 20, 30, 40]
i.insert(3,60)
print(i)#op:[5, 10, 20, 60, 30, 40]
i.insert(-1,80)
print(i)#op:[5, 10, 20, 60, 30, 80, 40]


#deletion

i.remove(20) #specific value
print(i)#op:[5, 10, 60, 30, 80, 40]
i.pop(0) #remove forst element
print(i)#op:[10, 60, 30, 80,40]
i.pop(-1)#remove last element 
print(i)#op:[10, 60, 30, 80]
#unique identifer
a=10,20,10,30,20
h=[(int(c)) for c in a]
s=set(h)
newl=list(s)
print(newl)#op:[10, 20, 30]'''


#serching method
arr = [5,8,3,10]

key = 3

for i in range(len(arr)):
    if arr[i] == key:
        print("Found")


        