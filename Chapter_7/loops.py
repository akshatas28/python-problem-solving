# chapter 7 : loops : for and while

# for loop : can be applied to list, tuple or string as well

# range(start, end , skip)
    
for i in range (1,6):
    print (i)

for i in range (1,6, 2):
    print (i) 
    
lists= [1,2,3,"harry",6]
for i in (lists) :
    print(i)

t = (1,3,6,7)
for i in (t):
    print (i)

name = "amazing"
for i in (name):
    print(i)

# break , continue , pass

for i in (lists):
    pass # u dont want to write the loop or complete it then just use pass, the loop is skipped

for (i) in range (100):
    if (i == 34):
        break # post reaching 33 the loop ends, it will not execute anymore
    print (i)

for (i) in range (100):
    if (i == 34):
        continue # post reaching 33 the loop skips 34, again starts printing from 35
    print (i)

# while loop

j = 1 # initialize
while (j<5): #condition
    print (j)
    j+=1 #incrementation or decrementation

# both are same, but remember that for loop, everything is in one line, but for while loop : u have to initialize, then peovide condition and then provide increment or decrement condition as well