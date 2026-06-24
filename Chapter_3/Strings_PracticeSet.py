#chapter 3 : strings : practice set
#question 1: print name post good afternoon message

name = "Good Afternoon"
username=input("Enter your name: ")
print (name +" " + username)

#question 2 : fill in letter template with name and date by user

sentence1 = "Dear"
usernameEmail = input("Enter your name: ")
userdate=input("Enter current date: ")
sentence2 = "\n Your are selected"
sentence3="\nDate: "
print(sentence1 + " " + usernameEmail + sentence2 + sentence3 + userdate)

#question 3 : detect double spacing in a string

stringspaced = "  hello  world  "
print(stringspaced.count("  "))

#question 4 : replace double spaces with single spaces

print(stringspaced.replace("  ", " "))

#question 5 : format following letter using escape sequence

letter = "Dear Harry, this python course is nice. Thanks!"

letter1 = "Dear Harry, \nthis python course is nice. \"Thanks!\""

print(letter1)