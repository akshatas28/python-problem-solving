# chapter 2 : vars and datatypes
#variables - identifiers a =5 identifier=value
# datatypes : int-7, str-"aks", bool-True or False, float-5.66, None

# rules for variables: underscores and alphabest ok, digits - shoukd not be used at start, but mid or end ok, but no special chars.

# operators - arithmetic, assignment, logical, comparison

# try below 
a = 5
b=6
c=a+b
#print (a+b) a and b are operands and c is result and plus symbol is operator
print(c)

#for example increment b by 3 and assign it to b
b+=3
print (b)

#comparison
g=a<b
print (g)

#logical
print (not(True))

#type() and typecasting
print (type(a))

h=float(a) #change any datatype to other datatype - but the connversion must be valid, alphabet string cant be converted to int or str
print (h)