# chapter 8 : functions and recursion : practice set

# question 1 : find greatest of 3 nums

def greatest (n1, n2, n3):
    if (n1>n2 and n1>n3):
        print(n1, "is greatest")
    elif  (n2>n1 and n2>n3):
        print(n2, "is greatest")
    elif  (n3>n2 and n3>n1):
        print(n3, "is greatest")
    else:
        print("input invalid")

def main():
    n1 = int (input("Enter 1st num: "))
    n2 = int (input("Enter 2nd num: "))
    n3 = int (input("Enter 3rd num: "))
    greatest(n1,n2,n3)
if __name__ == "__main__":
    main()

# question 2 : convert celsius to fahrenhiet

def conv(celsius):
    farh = (celsius*(9/5))+32
    return farh
def main():
    celsius = int(input("Enter temp in celsius: "))
    print (conv(celsius))

if __name__ == "__main__":
    main()

# question 3 : prevent python print() func to print a new line at the end

# print(" ", end="")

# question 4 : recursive func : sum of n natural nums

def sum(n):
    if (n==1):
        return 1
    return (n+sum(n-1) )
def main():
    n = int(input("Enter n for sum: "))
    print (sum(n))

if __name__ == "__main__":
    main()

# question 5 : print below pattern

n = int (input("Enter num for summation: "))
for i in range(n,0, -1):
    star = "*"* i
    print (star)
# this can be printed in recursive or function type also

# question 6 : convert inch to cm

def conv(inch):
    cm = inch*(2.54)
    return cm
def main():
    inch = int(input("Enter inch: "))
    print (round(conv(inch), 2))

if __name__ == "__main__":
    main()

# question 7 : remove given word from list and strip it at same time

l=["le", "circle", "triangle", "square", "pentagon"]
def remove(l, word):
    emptylist = []
    for i in l :
        if not(i==word):
            emptylist.append(i.strip(word))
    return emptylist
def main():
    word = input("Enter shape to removed from the list: ")
    print (remove(l, word))

if __name__ == "__main__":
    main()
    
# question 8 : table using func

def table(n):
    for i in range (1,11):
        print (n*i)
    print("table ends here")
        
    
def main():
    n = int(input("Enter digit for table: "))
    (table(n))

if __name__ == "__main__":
    main()