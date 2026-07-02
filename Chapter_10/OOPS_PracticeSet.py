# chapter 10 : oops : class, object : practice set

# question 1 : class programmer : store info of few prgs

class Programmer(): # class : template for object
    def __init__(self, name, dept ,exp):
        self.name=name
        self.dept = dept # class attribute
        self.exp=exp
        print(name, dept, exp)
harry=Programmer("harry", "sde", 4 ) # obj instantiation
aks=Programmer("aks", "devops", 3 ) 
rohan=Programmer("rohan", "ei", 7 ) 
# object called with attribute

# question 2 : class calculator : square cube and sqare root

import math

class calculator():
    def squaring(n):
        sqresult = n**2
        print (sqresult)
    def cubing(n):
        cuberesult = n**3
        print (cuberesult)
    def sqroot(n):
        sqrroot = math.sqrt(n)
        print(round(sqrroot, 2))
squarenum1=calculator.squaring(3)
squareroot1=calculator.sqroot(8)
cubenum1=calculator.cubing(3)

# question 3 : class attribute a : create object of class and replace value of a with o , does this change class attribute?

class tp():
    a = "haryy"
garry=tp()
garry.a="o"
print(tp.a)
print(garry.a) # no the class attribute value will not change : it will be there, only part is, instance attribute is also initiated, so now also, class attribute can be printed

# question 4 : in question 2 : add static method to greet user with hello

import math

class calculator():
    def squaring(n):
        sqresult = n**2
        print (sqresult)
    def cubing(n):
        cuberesult = n**3
        print (cuberesult)
    def sqroot(n):
        sqrroot = math.sqrt(n)
        print(round(sqrroot, 2))
    @staticmethod
    def greet():
        print("hello")
squarenum1=calculator.squaring(3)
squareroot1=calculator.sqroot(8)
cubenum1=calculator.cubing(3)
greeting=calculator.greet()

# question 5 : book ticket status(no of seats, info of train 

class train():
    def booking():
        name=input("Enter name: ")
        age=int(input("Enter age: "))
        seatchoice=input("Enter seat choice: ")
        print("name: ", name, "Age: " , age, "Seatchoice: " , seatchoice , "-> seat booked")
    def trainstatus():
         seatsfilled=56
         seatsremaining=89
         print ("seats filled: ", seatsfilled, ", seats remaining: " , seatsremaining)
    def traininfo(trainname, trainspeed):
        # trainname=trainname
        # trainspeed = trainspeed
        print("train name: ", trainname, ", train speed: ", trainspeed)

harry = train.booking()
harrry = train.trainstatus()
harrrry= train.traininfo("shatabdi", 56.78)


# question 6 : can u change self param inside class to something say "harry", try changing self to slf or harry:
    
class checking():
    def curiosity (slf):
        # name=slf
        print("name is: " , slf)
    def __init__(slf, dept):
        slf.dept= dept
        print("department is: ", dept)

harry=checking.curiosity("harry")
harry=checking("sde") # here for init method directly inside class, value can be passed which will be further picked by init method