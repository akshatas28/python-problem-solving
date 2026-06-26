#chapter 5 dict and set

# dictionary

dict1={"harry":34,
          "rohan":54,
          "sameer":78
          }
print(dict1.items())
print(dict1.values())
print(dict1.keys())
dict1.update({"harry": 56})
print(dict1)
print(dict1.get("harry")) # this is preferred as if value not presenr, then it will return none but below one will error out
print(dict1["harry"])
print(len(dict1))

# sets

s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(len(s1), s1)
print(len(s2), s2)

# clear , pop , remove
# issuperset , issubset

# union , intersection
print(s1.union(s2))
print(s1.intersection(s2))