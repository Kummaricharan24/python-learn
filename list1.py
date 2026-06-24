place=[1,2,3,4,5]
print(place[1:4])
print(place[:])

fruits=["apple","mango","cherry"]
fruits[0]="orange"
print(fruits)

fruits=["apple","mango","cherry"]
print(fruits[0])
print(fruits[1])

#methodsort
l=[32,56,2,5,89]#[a,s,d]
def sort(l):
    
    l.sort()
    return l
sort(l)
print(l)
#method append
l=[32,56,2,5,89]
l.append(10)# 10 added too the end 
print(l)
#metho insert
l=[32,56,2,5,89]
l.insert(4,8) #adding value in middle of the list
print(l)
#method index
l=[32, 56, 2, 5, 8, 89]
print(l.index(8)) #index  value in says middle of the list
#method remove
l=[32, 56, 2, 5, 8, 89]
(l.remove(8)) #remove value in middle of the list
print(l)
#metho pop
l=[32, 56, 2, 5,11 ,8, 89]
l.pop(4) #removeing with index value form the list
print(l)
#metho count
l = ["charan", "raj", "charan", "kiran","raj"]
print(l.count("charan")) #it counts how many   value are there in list
print(l.count("raj"))
#method reverse
l=[32,56,2,5,89]
l.reverse() #reverseing  of the list o/p=[89, 5, 2, 56, 32]
print(l)
#list of concatenation
l1=[1,2,3]
l2=[4,5,6]
def comb(l1,l2):
    comb_l=l1+l2#concatenation used to add two sets 
    return comb_l
comb_l=comb(l1,l2)
print(comb_l)#op:[1, 2, 3, 4, 5, 6]
#method list comprehensions
i=int(input())
list=[i**2 for i in range (1,i+1)]#manaki large number kavali anapudu comprehension use chestamu like operators
print(list)