# chapter 11 : oops : advanced : inheritance

# single level

class Prg(): # base class
    dept = "it"
    def getinfo(self):
        print("dept is: ", self.dept)
garry=Prg()
garry.getinfo()

class Emp(Prg):  # derived class
    def show(self, company):
        print("company is : ", company, "dept is: ", self.dept) # want to call something from other class, use self arg
haryy=Emp()
haryy.show("itc")

# multi level inheritance

class Prg(): # base class
    dept = "it"
    def getinfo(self):
        print("dept is: ", self.dept)
garry=Prg()
garry.getinfo()

class Emp(Prg): # derived class
    parent_company="alpha"
    def show(self):
        company= input("enter company: ")
        print("parent_company is : ", self.parent_company, "-- company is : ", company, "-- dept is: ",self.dept)
haryy=Emp()
haryy.show()

class EmpName(Emp): # sub-derived class
    def empname(self):
        
        name = input("enter name: ")
        print (name)
        print("name is: " , name, "parent_company is : ", self.parent_company, "dept is: ", self.dept)

sharry=EmpName()
sharry.empname()

# multiple inheritance

class Prg(): # separate class
    dept = "it"
    def getPrg(self):
        print("dept is: ", self.dept)
garry=Prg()
garry.getPrg()

class Emp(): # separate class
    company = "itc"
    def getEmp(self):
        print("company is: ", self.company)
harry=Emp()
harry.getEmp()

class both(Emp, Prg): # calling both classes
    
    def getboth(self):
        name = input("enter name: ")
        print (name)
        print("name is: ", name, "-- company is : ", self.company, "-- dept is: ",self.dept)
sharry=both()
sharry.getboth()

# to remember : only properties that have been defined in class at global class level will work further leading to getting fetched in subsequent classes

# super class

class PrgA():
    a=1
    def __init__(self):
        print("prgA is running ")

class PrgB(PrgA):
    b=2
    def __init__(self):
        print("prgB is running ")

class PrgC(PrgB):
    c=3
    def __init__(self):
        super().__init__()
        print("prgC is running ")
o=PrgA()
print(o.a)
o=PrgB()
print(o.a, o.b)
o=PrgC()
print(o.a, o.b, o.c)


# alternative to init func:

class PrgA():
    a=1
    def prga(self):
        print("prgA is running and value of a is: ", self.a)

class PrgB(PrgA):
    b=2
    def prgb(self):
        print("prgB is running and value of a is: ", self.a , "-- and value of b is: ", self.b)

class PrgC(PrgB):
    c=3
    def prgc(self):
        super().prgb()
        print("prgC is running and value of a is: ", self.a , "-- and value of b is: ", self.b, "-- and value of c is: ", self.c )
o=PrgA()
o.prga()
o=PrgB()
o.prgb()
o=PrgC()
o.prgc()

# class method

class Emp():
    a=1
    @classmethod # what this does is: whatever vakhe is given for a property in the class will be as it is, no one can override it! so value of a becomes 1!
    def show(self):
        print("value of a in class is: ", self.a)
harry=Emp()
harry.a=45
harry.show() # when this ran, the value 45 will be printed by default as instance attribute is given priority, but we introduce class method

# property and # setter getter method

class Emp():
    a=1
    @classmethod
    def show(cls):
        print("value of a in class is: ", cls.a)
    @property
    def showname(self):
        print ("first name is: ", self.fname)
    @showname.setter
    def showname(self, val):
        self.fname=val.split(" ")[0]
        self.lname=val.split(" ")[1]
harry=Emp()
harry.a=45
harry.show()
harry.showname="virat kohli"
harry.showname


# operator overloading | polymorphism

class Number():
    def __init__(self, n):
        self.n=n
    def __add__(self, num):
        return self.n + num.n
    def __sub__(self,num1):
        return self.n - num1.n
        # __mul__
        # __truediv__ = floating quotient
        # __floordiv__ = approx quotient
        # str__ - magical dunder
n=Number(1)
m=Number(2)
o=Number(8)
print (n+m)
print(o-n)