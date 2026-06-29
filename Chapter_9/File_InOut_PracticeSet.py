# chapter 9 : file i/o : practice set

# question 1 : in poems.txt : read text and find whether twinkle word us there or not

with open("file.txt", "r") as f:
    content = f.read()
    position = (content.find("twinkle")) # one can use if else to check if twinkle is there or not for condition position!=-1
    print (position)
    # if "twinkle" in content:
        #print("twinkle present")


# question 2 : game() func : user plays and score as output: score stored in Hi-score.txt, if not there : user includes it else, update existing score to the new score

old_score = 45
new_score = 50
with open("Hi-score.txt", "r") as f:
    content = f.read()
copy_content = content
data=copy_content.find(str(old_score))
if (data!=-1):
    updated_score=copy_content.replace(str(old_score), str(new_score))
else:
    updated_score=str(new_score)
with open("Hi-score.txt", "w") as d:
        d.write(updated_score)
        
    

# question 3 : tables from 2-20, print in different files and store in folder for 13 year old

import os
folder_path = "all folders"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for j in range (2, 21):
    file_destination = os.path.join(folder_path, f"table_of_{j}.txt")
    with open(file_destination, "w") as f:
        for i in range (1, 11):
            a = (j*i)
            f.write(f"{j} x {i} = {a}\n")
    


# question 4 : in file: replace "Donkey" with "#####" , update same file

import re

with open("file.txt") as f:
            content = f.read()
updated_content=re.sub("Donkey", "#####", content, flags=re.IGNORECASE)
with open("file.txt", "w") as d:
        d.write(updated_content)


# question 5 : repeat above for list of such words

import re

l=["Donkey", "monkey"]

with open("file.txt") as f:
            content = f.read()
for i in l:
    content=re.sub(i, "#####", content, flags=re.IGNORECASE)
with open("file.txt", "w") as d:
        d.write(content)
    
# question 6 : mine a log file, check whether Python words is present or not

import re
with open("file.txt", "r") as f:
    content = f.read()
    find_word=re.findall("python", content, flags=re.IGNORECASE)
    if (find_word):
        print("python present")
    else:
        print("python absent")

# question 7 : find out line number where python is present in above question

found = False

with open("file.txt", "r") as f:
    # enumerate() takes multiple identifiers in one go : no need to separatly mention and/or update any vars
    for line_number, line in enumerate(f, start=1):
        
        # search for single occurence at a time
        if re.search("python", line, flags=re.IGNORECASE):
            print(f"python present on line {line_number}")
            found = True

if not found:
    print("python absent from the entire file")

# question 8 : make copy of "this.txt"

import shutil

# Copies "old_file.txt" and names the copy "new_file.txt"

#to copy file from different location or to place it to diff location

# shutil. copy(r"C:\Users\Name\Downloads\report.txt", r"C:\Users\Name\Desktop\backup.txt")

# one can copy entire folder

# shutil.copytree(source_folder, destination_folder)

shutil.copy("old_file.txt", "new_file.txt")

print("File copied successfully!")

# extra : pip install gitpython : to copy repo : 
#from git import Repo

# 1. Provide the URL of the Git repository you want to copy
#git_url = "

# rather than installation, one can use import subprocess : subprocess direct python's module

# question 8 : compare if file is identical or not

with open("file1.txt", "r") as f:
    content1 = f.read()
with open("file2.txt", "r") as f:
    content2 = f.read()
if (content1 == content2):
    print("content similar")
else :
    print("content dissimilar")

# question 9 : wipe out contents of file

with open("file1.txt", "w") as f:
    content1 = f.write("")
    # pass : this can also be written on a way that the file is laredy open to write, so if we pass the coee, the file will be empty
    
    # any existing file if opened in w mode itself clears the content if any

# question 10 : rename a file

import os

old = "old_file.txt"
new = "renamed_file.txt"

if os.path.exists(old): # here one could have directly used os.rename(old, new) if the user is sure about 2 constraint: old file exists, and the new name which will be given must be unique and should not exist earlier
    if not os.path.exists(new):
        os.rename(old, new)
        print("Rename complete!")
    else:
        print("Error: A file with the new name already exists.")
else:
    print("Error: The original file was not found.")