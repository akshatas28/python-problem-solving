# chapter 9 : file i/o

# ram : volatile, no storing of data, fast retrieval
# hdd : non volatile meaning storing of data, slow retrieval
# persist : mean saving of data

f = open("file.txt") # by default it is r meaning open("file.txt", "r") : read mode
print(f.read())
f.close()

# no file createe, no worries, use write method, file will be created with respective content

f = open("file.txt", "w") # write mode
f.write("this is my file")
f.close()

f = open("file.txt") 
data=f.readlines() # read one line at a time but prints everything in a list datatype
# f.readline()  - prints one line at a time : once file lines are read, pist that program will exevute but with empty output
print(data, type(data))
f.close()


# modes to open file, r: read, w:writw, a:append, +:update, rb:read in binary type, rt: read in txt form

f = open("file.txt")
line=f.readline()
while(line!=""):
    print(line)
    line=f.readline()
f.close()

# using with statement : file is opened and closed automatically

with open("file.txt", "r") as f:
    print(f.read())