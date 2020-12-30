r = input("Enter range:")

ex_set1 = {} #empty dictionary

ex_set1 =set() #make it as set

print(type(ex_set1))
#output: <class 'set'>

for i in range(int(r)):
    ex_set1.add(i) #add elements to set

print(ex_set1)
