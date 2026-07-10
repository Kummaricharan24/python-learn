
#method creating dictionary 
i={"name":"charan","age":20,"colleage":"gnu"}
print(i)


#accessing dictionary 
i={"name":"charan","age":20,"colleage":"gnu"}
n_v=i["name"]
a_v=i["age"]
h_v=i["colleage"]
print(n_v)
print(a_v)
print(h_v)


#method update dictionary 
i={"name":"charan","age":20,"colleage":"gnu"}
i["address"]="hyd"
print(i) #op:{'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'


#method get()
i={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
print(i.get("name"))#op:charan

#'''method pop Removes the specified key-value pair from the dictionary.
#Returns the value of that key.'''
i={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
print(i.pop("address"))
print(i)#op:{'name': 'charan', 'age': 20, 'colleage': 'gnu'}



#method keys() is used print only keys values 
i={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
print(i.keys())#op:dict_keys(['name', 'age', 'colleage', 'address'])


#method items() here prints keys& values
i={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
print(i.items())#op:dict_items([('name', 'charan'), ('age', 20), ('colleage', 'gnu'), ('address', 'hyd')])


#method values() here only prints values of keys 
i={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
print(i.values())#op:dict_values(['charan', 20, 'gnu', 'hyd'])


#method of dict looping 
d={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}
for i in d.values():
    print(i)
for j in d.keys():
    print(j)
for i,j in d.items():
    print(i,j)




#method dict compherisions
d={'name': 'charan', 'age': 20, 'colleage': 'gnu', 'address': 'hyd'}

square_dict={d:d**2 for d in range(1,3) }
print(square_dict)