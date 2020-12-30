val = input("Enter your range: ") 
print(val) 
lst = []
for i in range(int(val)):
   lst.append(i)
print(lst)

#nested list
matrix = [] 
  
for i in range(int(val)): 
    #Append elements in list
    matrix.append(i) 

#Append empty list    
matrix.append([])
for j in range(int(val)-5): 
    matrix[-1].append(j) 

print(matrix)
#output:
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]