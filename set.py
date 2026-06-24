#method union
s2={1,2,3}
s1={3,4,5,6}
d=s1.union(s2) #union used to add sets  and remove repeated values 
print(d) #op:{1, 2, 3, 4, 5, 6}
#method intersection
s2={1,2,3}
s1={3,2,6,7}
d=s1.intersection(s2) #intersection used to shows repeated values 
print(d) #op:{2, 3}
#method differnce
s2={1,2,3}
s1={3,2,6,7}
d=s1.difference(s2) #Returns only the elements that are in s1 but not in s2.
print(d) #op:{6, 7}
#method symmetric difference
s2={1,2,3}
s1={3,2,6,7}
d=s1.symmetric_difference(s2) #used to removes similar values and print unqie values 
print(d) #op:{1,6, 7}


#method membership & length 

s1={3,2,6,7}

print(3 in s1)#op:True "the set value there are in set if  there return true"
print(5 in s1)#op:False "the set value there are in set if not there return false"

print(len(s1)) #op: 4 length of the set


#method frozen set
i={1,2,3}
f_s=frozenset(i)
print(f_s)


#set comprehension
i=int(5)
su={i**2 for i in range(1,5)}
print(su)


#method  clear()
i={1,2,3}
i.clear()
print(i)


#method copy()
new_set={1,2,3}
print(new_set)



#method update()
i={1,2,3}
i.update({4})
print(i)


#method pop()
i={2,3,4,5}
i.pop()
print(i)
