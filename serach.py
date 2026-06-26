i=[90,50,30,50,60]
key=50
j=0
for j in range(len(i)):
    if i[j]==key:
        print(f"its find:{j}")
        
#op:its find:1
#its find:3
        
#2d matrics
a=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sum=0
for i in range(len(a)):
    for j in range(len(a[i])):
        sum +=a[i][j]
    print(i,"=",sum)
        
