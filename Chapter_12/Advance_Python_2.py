# chapter 12 : advanced python 2

# virtual env
pip install virtualenv # creation of virtual environment for python projects/tasks

pip freeze # enlists all the modules with their versions

pip freeze > requirements.txt # creates a file and it that it enlists all the modules with their versions

# lamda function

square=lambda n:n*n # lambda args:expr
sum= lambda a,b,c:a+b+c # no need to mention everything separately, using lambda all can be done in one go
print(square(4))
print(sum(1,2,3))

# join method

l=[1,2,3,3,4,4,4]
a="::".join(str(l))
print(a) # this is an exception but mostly.join method works on str type

# alternate

l=["harry","rohan"]
a="::".join(l)
print(a) # unpacking is done and the words are joined together with whatever is mentioned in double quotes before join method

# format method : in mldern ways this is replaced using f keyword

a = "{} is a good {}".format("sam", "boy")
print (a) # same gets in first curly and boy in second 

a = "{0} is a good {1}".format("sam", "boy")
print (a) # this is similar to above code - even if any index is provided or not it will work

a = "{1} is a good {0}".format("sam", "boy")
print (a) # here the indexes are jumbled yet the code executes but the result is a jumbled statement

# map, reduce and filter

l=[1,2,3,4,5]
square= lambda x:x*x
sqlist=map(square, l) # here the square task is getting assigned to arg l
print(list(sqlist)) # needed to map list items to another list

# filter func

def even(n):
    if(n%2==0):
        return True
    return False
a=filter(even, l) # task even getting assigned to arg l
print(list(a)) # needed to filter certain elements from rest using specific conditions

# reduce func

from functools import reduce # this needs to be mentioned if reduce func needs to be used

l1=[1,2,3,4]
def sum(a,b):
    return a+b 
mul=lambda a,b:a*b
print(reduce(sum, l1)) # task sum getting assigned to arg l1
print(reduce(mul, l1)) # task mul getting assigned to arg l1
# reduce is needed to reduce a list of n elements to least numbered elements in this case 2 as 2 args are needed at the end to be added or multiplied
# 1,2,3,4 -> 1+2 =3 : 3,3,4 -> 3+3=6 : 6,4 -> 10 : nothing pending to add so this is the output.