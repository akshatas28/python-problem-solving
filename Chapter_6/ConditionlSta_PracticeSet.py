# chapter 6 : conditional statements : if else elif ladder : practice set

# question 1 : find greatest of 4 nums entered by user
    
n1 = int(input("Enter 1st num: ")) 
n2 = int(input("Enter 2nd num: ")) 
n3 = int(input("Enter 3rd num: ")) 
n4 = int(input("Enter 4th num: ")) 
if (n1>n2 and n1 >n3 and n1>n4):
    print (n1 , "is greatest")
elif (n2>n1 and n2>n3 and n2>n4):
    print (n2 , "is greatest")
elif (n3>n1 and n3>n2 and n3>n4):
    print (n3 , "is greatest")
elif (n4>n1 and n4>n2 and n4>n3):
    print (n4 , "is greatest")
else :
    print("reenter input")
print("program ends here")

# question 2 : student passed if overall marks are 40% and 33% in each subject, assume 3 subhect and take marks as input from user

n1 = int(input("Enter 1st subject marks: ")) 
n2 = int(input("Enter 2nd subject marks: ")) 
n3 = int(input("Enter 3rd subject marks: ")) 

if (((n1 /100)*100)>=33 and ((n2 /100)*100)>=33 and ((n3 /100)*100)>=33 ) :
    if (((n1+n2+n3)/300)*100 >= 40):
        print ("Student passed")
    else:
        print("passed in subject : but for overall result : need to try again")
else :
    print("kid retry again")
print("program ends here")
    
# question 3 : spam comment contains : "make a lot of money" , "buy now" , "subscribe this" , "click this", write program to detect these spams

spamcheck = input("Enter email subject or body: ")
if (spamcheck.find("make a lot of money") or spamcheck.find("buy now") or spamcheck.find("subscribe this") or spamcheck.find("click this") ):
    print ("its a SPAM!")
else :
    print ("not a spam")


# question 4 : find whether a username containes 10 chars or not?

username = input("Enter your username: ")
if(len(username)<10):
    print ("invalid username")
else :
    print ("username accepted")

# question 5 : find whether given name is present in list or not


namelist = ["sara", "noah", "alex", "keith" ]
username= input("Enter your username: ")
if username in namelist:
    print ("username present")
else:
    print ("enter ur name in the list")


# question 6 : calculate grade of students from his marks

marks = int(input("Enter students marks: ")) 
if (marks >90 and marks <=100):
    print("grade excellent")
elif ( marks>80 and marks<=90 ):
    print("grade A")
elif ( marks>70 and marks<=80 ):
    print("grade B")
elif ( marks>60 and marks<=70 ):
    print("grade C")
elif ( marks>50 and marks<=60 ):
    print("grade D")
elif ( marks>0 and marks<=50 ):
    print("grade F")
else:
    print ("invalid input")


# question 7 : whether a given post contains Harry or not

post= input("Enter your post statements: ")
#post = "i am harry"
name = "harry"
if name in post:
    print ("harry present")
else :
    print ("harry absent")