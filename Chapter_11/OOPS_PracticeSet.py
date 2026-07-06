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


# question 3 :