# chapter 5 : practice set

# question 1 : create dictionary of hindi words, values as english, user enters key name, value provided 

dict1 = {
            "kal":"tomorrow",
            "aaj": "present",
            "kal":"past"
        }
i = input ("enter a hindi word: ")
print(dict1.get(i))
# here even if u have 2 kal : the first valie will be overriden by new value

# question 2 : input 8 numbers from user, display all unique ones

s=set()

s1=int(input("enter a number: "))
s.add(s1)
s2=int(input("enter a number: "))
s.add(s2)
s3=int(input("enter a number: "))
s.add(s3)
s4=int(input("enter a number: "))
s.add(s4) #in similar way, input 8 values

print(len(s), s)


# question 3 : set with 18 int and 18 str?

s={18, "18"}
print(len(s), s)

# question 4 : what will be length of following set

s = set()
s.add(20)
s.add(20.0) # this means 20 only so it will not be printed in the set
s.add("20")
print(len(s), s) #2

# question 5 : s={} : which type
s={}
print(type(s))

# question 6 : create empty dict, allow 4 friends to enter their language as key and names as values, names are unique

d={}

d1=input("enter a language: ")
d2=input("enter a name: ")
d.update({d1 : d2})

d3=input("enter a language: ")
d4=input("enter a name: ")
d.update({d3 : d4})

d5=input("enter a language: ")
d6=input("enter a name: ")
d.update({d5 : d6})

d7=input("enter a language: ")
d8=input("enter a name: ")
d.update({d7 : d8})

print(len(d), d)

# question 7 : names of 2 friends same then what will happen in problem 6

# even if values same it will get inserted

# question 8 : languages of 2 friends same then what will happen in problem 6

# if keys are same, the key will override its current value with new value

# question 9 : can u change value of list contained in set s

s = {8,7,12,"harry",[1,2]}

# error : unhashable item, in mutable sets, only immutable values are allowed