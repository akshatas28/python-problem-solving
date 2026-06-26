#chapter 4 list and tuple

#list

#listeg=container of all datatype 

listEg = ["amazing", True, 78, 78.9, "Grapes"]
print (len(listEg))
print (listEg[1])
print (listEg)

#list methods

print(type(listEg))
listEg.append(98)
print (listEg)
listEg.insert(3, 4)
print(listEg)
listEg.reverse()
print (listEg)

print(listEg.pop(2))
listEg.remove("Grapes")
print(listEg)
#print(listEg.sort()) : it will sort only if same datatype


#tuple

#tupleeg=(1, ) : because if comma is not given then it will be an int type

tupleEg = (78, "amazing", True, 78, 78.9, "Grapes",78)

#tuple methods
print(type(tupleEg))
print(tupleEg.count(78))
print(tupleEg.index("amazing"))
# concatenation = tuple1+tuple2
#repetition=tuple1*3
#membership=(1 in tuple1) : true or false
#length=len(tuple1)
#min max slicing unpacking