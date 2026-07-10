a=[15,2,7,25,20]
a.sort()
min=a[0]
print(f"Minimum:{min}")
max=a[-1]
print(f"Maximum:{max}")





a=[15,2,7,25,10]
min=15
max=15
for i in a:
    if max <i :
        max=i
        print(max)
for i in a:
    if  min >i:
        min=i
        print(min)



b = [15,2,7,25,10]

min_num = 15
max_num = 15

i = 0

while i < len(b):

    if max_num < b[i]:
        max_num = b[i]

    if min_num > b[i]:
        min_num = b[i]

    i += 1

print("Max =", max_num)
print("Min =", min_num)

