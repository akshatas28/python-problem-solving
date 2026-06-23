# chapter 1 : practice set
#question 4

# print contents of a directory using os module : search online for the function that does this

# question 5 : label the prg written in question 4 with comments meaning for each step, write a small comment on what is being done

import os
#listing path - question 5th done
directory_path = '/path'
#listing folders in the path
contents=os.listdir(directory_path)
#printing all folders using loop
for i in contents:
    print(i)
    