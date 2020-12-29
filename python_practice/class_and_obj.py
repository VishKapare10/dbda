class Person:

    # class attribute
    species = "Human"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def drive(self, speed):
        print("{} is driving at speed of {}".format(self.name,speed))  
        return (self.name,speed)  #use of tuple to return mutiple values    
    

# instantiate the Person class
p1 = Person("Vishwambhar", 24)

# access the class attributes
print("Class attribute is : {}".format(p1.__class__.species))

# access the instance attributes
print("{} is {} years old".format(p1.name,p1.age))

#call to drive function
vals = p1.drive(50)
print(vals)