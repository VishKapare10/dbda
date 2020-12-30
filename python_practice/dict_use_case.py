class my_dict_use(dict):  
  
    # __init__ function  
    def __init__(self):  
        self = dict()  
          
    # Function to add key:value  
    def add(self, key, value):  
        self[key] = value  

user = my_dict_use()
j = 5
for i in range(10):
    while(j<10):
        user.add(i,j)
        i += 1
        j += 1

print(user)

n = 10
while(n<100):
    user.add(n,n+10)
    n +=1

print(user)
#print(user.keys())
#print(user.values())
print(user.get(10))  #get value where key == 292
print(user[10]) #get value where key == 292

for key, value in user.items():
         if key == 90:
             print(value)

for key, value in user.items():
         if value == 100:
             print(key)

#Tuple as a key in dictionary
employees = [("Vishwambhar", "Kapare"), ("Akshay","kakade"), ("Shubham","Joshi"), ("Isha","k")]
basic_sal = 10000
salary = []
for i in range(len(employees)):
    salary.append(basic_sal)
    basic_sal = basic_sal + 1000



emp = my_dict_use() #create dict
for i in range(len(employees)):
    emp.add(employees[i],salary[i])
      
for key,value in emp.items():
    print("Emp_name: {}, salary: {}".format(key,value))