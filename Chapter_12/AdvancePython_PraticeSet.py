# chapter 12 : oops : advanced : python : practice set

# question 1 : open 3 files, if any file not found : provide error withojt exiting the code

try:
    with ( open ("file1.txt") as f1, open ("file2.txt") as f2, open ("file3.txt") as f3):
        context1=f1.read()
    print(a)
except FileNotFoundError as fnf:
    print("file does not exist")
    print(fnf)
except Exception as e: # here even if error comes, the next line in program will get exevuted but will flash the error
    print("try different location, or filename")
    print(e)

print("thankyou statement post try and except")

# question 2 : print 3, 5, 7th element of a list using enumerate 

l = [1,2,3,4,5, 6]
for index, item in enumerate(l):
    if(index ==2 or index==4 or index==6):
        print (f"item at index{index} is {item}")


# question 3 : list comprehension using tables

l = [1,2,3,4,5, 6,7,8,9,10]
n=int(input("enter table num to be printed: "))
table=[i*n for i in l]
print(*table, sep="\n") # * operator in print is used for unpacking a list, sep : separator by putting next value in next line


# question 4 : a/b and th3 ZeroDivisionError

a=int(input("enter first number: "))
b=int(input("enter second number: "))
if (b==0):
    raise ZeroDivisionError("hey second number must not be zero")
else:
    print("division of first by second : ", a/b)
    # or either ways one can use try except blocks as well


# question 5 : store tables generated in problem 3 in tables.txt

l = [1,2,3,4,5, 6,7,8,9,10]
n=int(input("enter table num to be printed: "))
table=[i*n for i in l]
print(*table, sep="\n")
with open("tables.txt", "w") as t:
    for i in l:
        # calculate result for specific line
        result = i * n
        # clean math equation to the file
        t.write(f"{n} x {i} = {result}\n")