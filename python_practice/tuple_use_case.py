#Adding values to a tuple by changing its type to list
ex_tuple = (1,10,7,8)
print(ex_tuple)
exl = list(ex_tuple)
print(exl)

for i in range(41,50):
    exl.append(i)

print(tuple(exl))