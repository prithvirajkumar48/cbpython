## Lists - mutable

# basic List
l = [45,56,30,23,46,34,78,33,10,11]

#print full list
print(l)
#print one element based on index
print(l[4])
# print few elements with start end
print(l[2:6])
# print elements with step
print(l[2:6:2])

# changing values
print(l[1])
l[1]=100
print(l[1])

# adding elements at the end
print(l)
l.append(66)
print(l)
# add element at a location
l.insert(2,40)
print(l)

# remove element
l.remove(34)
print(l)
# search for an element
print(l.index(11))


# generate list with range function
l=list(range(1,30,5))
print(l)

## tuples - immutable
t = (33,24,32,43,55)
print(t)
