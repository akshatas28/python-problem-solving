# chapter 6 : conditional statements

# only if, elif, else ladders

age = int(input("Enter your age: "))

if (age%2==0):
    print("age is even")
    
# multiple ifs are ok, every if will run on its own, if are independent
# but else and elif are dependent on if

if(age>=18):
    print("above age 18")
# one can inclide elif for check if age==0 or age<0

# relational and logical opeeators need to be studied for this

else:
    print("below age 18")