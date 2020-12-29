#List (Mutable)
a = [1,3,4,5,66,77,79,900] #simple list 
b = [44,50,"ABC"] #List with diffrent data types
c =[20,21,"hello",[1,9]] #nested list

print(a[0]) #prints first element

print(c[3][0]) #printing element from nested list

print(a[-1]) #prints last element
print(a[0:3]) #Slice: returns value at index 0. 1 and 2
print(a[:4]) #Slice: returns elements from 0 to 3
print(a[5:]) #Slice: returns elements from 5 to last element
print(c[:]) #Slice: returns all elements    

print(a+b) #List Concatenation of a and b list
print(a*2) #- * repeats the list given no of times
a.append(10) #append a value in a list
a.extend(b) #adds values from 2 lists
a.pop() #pops the last element from list (LIFO manner)
a.reverse() #reverses a list
a.sort() #sorts list
a.remove(10) #removes element from a list

