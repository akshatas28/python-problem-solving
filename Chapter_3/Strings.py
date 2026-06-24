#chapter 3 string, string slicing

name = "amazing"
print (len(name))
print (name[1:3])
print (name[:3])
print (name[1:])
print(name[4])
print (name[1:6:2])
print(name.endswith("ing"))
print(name.startswith("am"))
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.title())
print(name.count("a"))

print(name.find("g"))

print(name.zfill(11))

print(name.isalpha())
print(name.isalnum())
print(name.isdigit())


name1="hello world"
print(name1.split())
print(name1.replace("world", "all"))


name2 = '["a", "b", "c"]'
print(", ".join(["a", "b", "c"]))

name3 = "  hello  "
print (name.strip())
print (name.lstrip())
print (name.rstrip())
print(name3.isspace())

print(str(123))

#escape sequencing

name4 = "He is a bad \nboy"
print(name4)

name5 = "He is a bad \"boy\""
print(name5)

name6 = "He is a bad \tboy"
print(name6)