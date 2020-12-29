#sets (Mutable)
s1 = {} #Iniatlize with a {}
print(type(s1)) #output: <class 'dict'>
s1 = set() 
print(type(s1)) #output: <class 'set'>

s2 = {1,2,35,35,67,78,88,99} #set cannot have duplicate items
print(s2) #output: {1, 2, 67, 35, 99, 78, 88}

s3 = {1.0, "Hello", (1, 2, 3)} #set of mixed data types

#set from a list output
set3 = set([3,6,7,8,8])
print(set3) #output: {8, 3, 6, 7}

#modifying a set
#my_set = {1, 2, [3, 4]} #set cannot have mutable items

s2.add(100) #adds an element

s2.update([200,344]) # adds multiple elements
s2.update([788,899], {677,911}) # adds list and set
print(s2)

s2.discard(67) #discards specified element 

s2.remove(899) #removes specified element
#removes throws error if element is not present, 
#while discards does'nt throw any error and keeps the set unchanged.

print(s2) #output: {1, 2, 35, 99, 100, 344, 200, 677, 78, 911, 788, 88}

print(s2.pop()) #returns first element
print(s2.clear()) #removes all elements of a set


#set operarations
a = {1,4,5,6,66}
b= {90,45,66,78}
print(a.union(b)) #makes union of 2 sets 
#output: {1, 66, 4, 5, 6, 45, 78, 90}

print(a.intersection(b)) #makes intersection
#output: {66}

print(a-b) #takes difference of elements which are in set a but not in b
#output: {1, 4, 5, 6}

print(a.symmetric_difference(b)) #elements in and b but not in both
#output: {1, 4, 5, 6, 45, 78, 90}

print(1 in a) #checks if element 1 is present in set a
#output: True

#Iterating through a set
for ele in a:
    print(ele)



#Frozenset (Immutable)
#Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
#While tuples are immutable lists, frozensets are immutable sets.

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([8, 9, 4, 6])

print(A.difference(B))
#output: frozenset({1, 2, 3})
