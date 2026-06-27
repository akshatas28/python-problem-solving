# chapter 7 : loops : for and while

# question 1 : multiplication table using for loop

num = int (input("Enter num for table: "))
for i in range (1,11):
    print (num*i)

# question 2 : greet all person stored in list l for only person : whose name start with s

l = ["harry", "soham", "sachin", "rahul"]
for i in (l):
        if (i.startswith("s")):
            print ("good morning ", i)
            break

# question 3 : attempt problem 1 using while loop

num = int (input("Enter num for table: "))
i = 1
while (i<11):
    print (i*num)
    i+=1

# question 4 : find whether given num is prime or not

from math import isqrt

num = int (input("Enter num to check: "))
if (num==2):
    print ("prime")
if (num%2==0):
    print ("composite")
    exit()

for i in range (3,isqrt(num), 2):
    print ("composite")
    break
else :
    print ("prime")


# question 5 : sum of first n natural numbers using while loop

num = int (input("Enter num for summation: "))
i = 1
a=num
while (i<num):
    a=a+i
    i+=1
print (a) 

# question 6 : factorial of num using FOR loop

num = int (input("Enter num for factorial: "))
for i in range(1, num):
    num*=i
print(num)

# question 7 : print pattern for n =3

n=3
for i in range(1,4):
    k = n-i
    k=" "*k
    star = "*"* i
    star2 ="*"* (i-1)
    print (k + (star) + star2)
    
    
# question 8 : print following star pattern

n=3
for i in range(1,4):
    star = "*"* i
    print (star)

# question 9 : print following pattern

n=3
for i in range(1,4):
    for j in range(1,4):
        if (i == n or i==1 or j == n or j==1):
            print("*", end="")
        else :
            print (" ", end="")
    print()

# question 10 : table in reverse order

num = int (input("Enter num for factorial: "))
for i in range (10, 0, -1):
    print (num*i)