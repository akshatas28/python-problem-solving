# chapter 10 : oops : class, object
# dry principle : don't repeat yourself

# class

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
harry=Emp() # obj instantiation
print(harry.lang, harry.sal) # object called with attribute

# object attribute

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
harry=Emp()
harry.name = "xyz" # object attribute
harry.lang="java" # object attribute
print(harry.name, harry.lang, harry.sal)
# here the attribute can also be initiated and printed
# object attribute id given preferance over class attribute 

# obje attribute is called as "INSTANCE ATTRIBUTE"

# one can include def method with self args, because if self is not given then whatever object value is passed as an argumenr will not be parsed in def method

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
    def getinfo(self):
        print(f"lang is {self.lang} and sal is {self.sal}")
    def greet(self):
        print("morning")
harry=Emp() # obj instantiation
harry.lang = "java"
harry.getinfo() # object called with method
harry.greet()
# Emp.getinfo(harry) : this is also a way to call the method with obj arg