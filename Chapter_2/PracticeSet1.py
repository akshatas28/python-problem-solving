# chapter 2 : practice set
# question 1 = pg to add 2 numbers

c=int(input("Enter int 1: "))
d=int(input("Enter int 2: "))
print("int concat is: ", c+d)

# question 2 = pg to find remainder when a number is divided by z
a = int(input("Enter dividend : "))
b = int(input("Enter divisor : "))
print ("remainder is: ", a%b)

# question 3 = check type of var assigned using input function

var = input("Enter any var : ") #for this input all will be string, for int, declare int in front of input, similar for float, bool, none
print ("Type of var : ", type(var))


# question 4 = compare 2 operators and check if 1st is greater or not

num1 = 34
num2 = 80
print ("is num1 greater than num2: " ,num1>num2)

# question 4 = avg of 2 numbers by user

avg1 = int(input("Enter first num : "))
avg2 = int(input("Enter second num : "))
print ("average of avg1 and avg2: ", (avg1+avg2) / 2)

# question 5 = calc sq of number by user

sqnum = int(input("Enter num to be squared : "))
print ("square of num is : ", (sqnum**2))
# one can use math.pow() or pow()