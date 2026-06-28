# chapter 8 : functions and recursion

# function : set if code that can be used repetitively by calling the function

# func with no args, direct call and it will print

def avg():
    n1 = int (input("Enter 1st num "))
    n2 = int (input("Enter 2nd num "))
    avrg=(n1+n2)/2
    print (avrg)

avg()

# func with arguments : here it will return the value which can then be stored in other var or can be printed directly
            
def avg(n1, n2):
    avrg=(n1+n2)/2
    return (avrg)

print(avg(4,5))

# func with default arg values : same as above only here, default is kept in a way that even if nlthing is passed, then too the func must not stop working

def avg(n1, n2=10):
    avrg=(n1+n2)/2
    return (avrg)

print(avg(4))
    
# recursion : func calling itself

def fact(n):
    if (n==1 or n==0): # base condition : must return 0 or 1 or 2 depends.
        return 1
    return n*fact(n-1) # func calling itself creating a stack method, every iteration : one decrements until base case reaches, then stack gets cleared resulting in printing of ultimate end value

print(fact(7))