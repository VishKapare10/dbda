#multilevel inheritance
class Person:
    # instance attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age
 
class Employee(Person):
    
    def __init__(self,name,age,basic_salary):
        # call super() function
        super().__init__(name,age)
        self.basic_salary = basic_salary

    def cal_salary(self):
        total_sal = self.basic_salary
        return total_sal

class Sales_employee(Employee):
    def __init__(self,name,age, basic_salary,bonus):
        self.bonus = bonus
        Employee.__init__(self,name,age,basic_salary)

    def cal_salary(self):
        total_sal = self.basic_salary + self.bonus
        return total_sal

       
# instantiate the emp class
emp = Employee("Vishwambhar",24,15000)
emp_salary = emp.cal_salary()
print("Employee salary is: {}".format(emp_salary))

#instantiate the sales emp class
sales_emp = Sales_employee("Vishwambhar",24,30000,5000)
emp_salary = sales_emp.cal_salary()
print("Sales employee salary is: {}".format(emp_salary))

'''
output:
Employee salary is: 15000
Sales employee salary is: 35000
'''