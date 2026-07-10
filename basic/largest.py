i=int(9)
j=int(6)
k=int(7)
great=0
if i>j:
    if i>k:
        great=i
    else:
        great=k
elif j>i:
    if j>k:
        great=j
    else:
        great=k
elif k>i:
    if k>j:
        great=k
    else:
        great=j


print(great)
