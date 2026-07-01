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

# but what if i dont want to pass self entire obj as its nit being used in greet function ? so use @staticmethod

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
    
    @staticmethod
    def greet():
        print("morning")
harry=Emp() # obj instantiation
harry.lang = "java"
harry.greet() #it will run successfully as its declared as static method


# __init__ construtor = very helpful as it gets automatically called, no need to mention/call it separately

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
    
    
    def __init__(self):
        print("morning")
harry=Emp() # obj instantiation

# if no self is mentioned in init method, it will error out, 
# also after self, args can be initialized

class Emp(): # class : template for object
    lang = "py" # class attribute
    sal="12lpa"
    
    
    def __init__(self, name, lang, sal):
        self.name=name # self arg declaration needed and it is further called as name for simplification purpose.
        self.lang=lang
        self.sal=sal
        print(name, sal, lang) # this is needed to print the argument values
harry=Emp("harry", "py", "12lpa")