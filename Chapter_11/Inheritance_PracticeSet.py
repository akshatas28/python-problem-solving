# chapter 11 : oops : advanced : inheritance : practice set

# question 1 : create class 2D and use it to create another class 3D

class TwoDVector(): # base class
    i = input("enter i value: ")
    def getinfo2DVector(self):
        print("dept is: ", self.i)
garry=TwoDVector()
garry.getinfo2DVector()

class ThreeDVector(TwoDVector):  # derived class
    def getinfo3DVector(self, j):
        print("j value is : ", j, "i value is: ", self.i , "total is : " , (int(self.i)+int(j))) # want to call something from other class, use self arg
haryy=ThreeDVector()
haryy.getinfo3DVector("9")

# multi level inheritance

class Animals(): # base class
    animaltype = input("enter your animal preferance: dog or cat ")
    def getanimaltype(self):
        print("animal is: ", self.animaltype)
garry=Animals()
garry.getanimaltype()

class Pets(Animals): # derived class
    ispet="its a pet"
    def checkPets(self):
        nameofPet = input("enter your pet name: ")
        print("animal is : ", self.animaltype, "-- name of pet : ", nameofPet, "-- status of animal to be pet or not : ", self.ispet)
haryy=Pets()
haryy.checkPets()

if self.animaltype == "dog":
    dogs1=Dogs()
elif (self.animaltype=="cat"):
    cats1=Cats()
else:
    print("invalid animal pet")

class Dogs(Pets): # sub-derived class
    voice = "barks"
    def dogsinfo(self):
        print("dog name is: " , self.nameofPet, "sound of dog is : ", self.voice)
class Cats(Pets): # sub-derived class
    voice = "meows"
    def dogsinfo(self):
        print("cat name is: " , self.nameofPet, "sound of cat is : ", self.voice)


# question 3 :

class Employee:
    
    def __init__(self):
        self.salary=int(input("enter salary: "))
        self.hra=int(input("enter hra: "))
        self.bonus=int(input("enter bonus: "))
        
    @property
    def annual(self):
        return self.salary + self.hra + self.bonus
    @property
    def inhandsalary(self):
        return (self.annual)
    @inhandsalary.setter
    def inhandsalary(self, value):
        if (value <= 30000):
            self.salary=self.salary+value
            print (self.salary , " - is the new salary")
        
        
a=Employee()
a.inhandsalary=5000


# question 4 : complex class, overload + and *

class ComplexNum:
    def __init__(self, i=None, j=None):
        if i is not None and j is not None:
            self.i = i
            self.j = j
        else:
            self.i = int(input("provide i value: "))
            self.j = int(input("provide j value: "))

    def __add__(self, other):
        m= self.i+other.i
        n= self.j+other.j
        print("addition result" , m, n)
        return
    def __mul__(self, other):
        o= (self.i * other.i) - (self.j * other.j)
        p=(self.i * other.j) + (self.j * other.i)
        print("multiplication result" , o,p)
        return
    #def __str__(self):
        #sign = "+" if self.j >= 0 else "-"
        #return f"{self.i} {sign} {abs(self.j)}j"

        
a=ComplexNum()
b=ComplexNum()
(a+b)
(a*b)


# question 5 : vector class: vector of m dimensions, overload sum and dot product

class Vector:
    def __init__(self, x, y,z):
        self.x=x
        self.y=y
        self.z=z
    def __add__(self, other):
        result = Vector(self.x + other.x  , self.y+other.y, self.z+other.z)
        return result
    def __mul__(self, other):
        result = Vector(self.x*other.x  , self.y*other.y, self.z*other.z)
        return result
    def __str__(self):
        return f"{self.x}i + {self.y}j - {self.z}k"

a=Vector(1,2,3)
b=Vector(4,5,6)
c=Vector(7,8,9)

print(a+b+c)
print(a*b*c)


# question 6 : same as above

# question 7 : len method

class Vector:
    def __init__(self, l):
        self.l=l
    def __len__(self):
        return len(self.l)

a= Vector((1,2,3))
print(len(a))