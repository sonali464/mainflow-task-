#creating a list
list=[1,2,3,4,5]

#adding an element to the list
list.append(6)

print(list)
#removing an element from the list
list.remove(3)
print(list)

#modify an element in the list
list[0]=10
print(list)

print("updated list",list)

#creating a dictionary
dict={'name':'Anuj','age':25,'city':'Delhi'}
print(dict)

#adding 
dict['gender']='Male'
print(dict)

#removing 
del dict['age']
print(dict)

#modifying 
dict['city']='Mumbai'
print(dict)

print("updated Dictionary:",dict)


#creating a set
set={1,2,3,4,5}
print(set)

#adding 
set.add(6)
print(set)

#removing 
set.remove(3) 
print(set)

#modifying 
set.discard(1)
set.add(10)
print(set)

print("updated set:",set)