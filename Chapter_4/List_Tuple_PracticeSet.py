#chapter 4 list and tuple - practice set

# question 1 : 7 fruits entered by user in list
fruit=[]

f1 = input("Enter 7 fruits: ")
fruit.append(f1)
f2 = input("Enter 7 fruits: ")
fruit.append(f2)
f3 = input("Enter 7 fruits: ")
fruit.append(f3)
f4 = input("Enter 7 fruits: ")
fruit.append(f4)
f5 = input("Enter 7 fruits: ")
fruit.append(f5)
f6 = input("Enter 7 fruits: ")
fruit.append(f6)
f7 = input("Enter 7 fruits: ")
fruit.append(f7)

print(fruit)

# question 2 : accept marks of 6 students and display in sorted manner

marks=[]

f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)
f5 = int(input("Enter marks here "))
marks.append(f5)
f6 = int(input("Enter marks here: "))
marks.append(f6)

marks.sort()

print(marks)

# question 3 : tuple cannot be changed in python

#yes it can't beas tuple is immutable

# question 4 : sum a list with 4 numbers
marks=[]

f1 = int(input("Enter marks here: "))
marks.append(f1)
f2 = int(input("Enter marks here: "))
marks.append(f2)
f3 = int(input("Enter marks here: "))
marks.append(f3)
f4 = int(input("Enter marks here: "))
marks.append(f4)

print(marks)


print(marks[0]+marks[1]+marks[2]+marks[3])

#or
print(sum(marks))

# question 5 : count 0s in tuple

a = (7,0,8,0,0,9)
print(a.count(0))