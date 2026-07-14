# chapter 12 : advanced python 2 : practice set

# question 1 : create virtual env and mimic first to second

pip install virtualenv 

virtualenv env1

.\env1\Scripts\activate.ps1 # for activation of env1

pip install pandas and pyjokes # installing modules

pip freeze > requirements.txt # a txt file with all modules of env1 is created

deactivate # deactivate env1

.\env2\Scripts\activate.ps1 # for activation of env2

pip install -r requirements.txt # whatever was installed in env1 was mentioned in txt fike which is then directly installed in env2 without installing separate modules by comparing envs


# question 2 : name, marks, phone of student using format func

a = "name of student is {}, his/her marks are {} and phone number is {}".format("sam", 98, 7362527829)
print (a) # all the above format values can be inputted separately using user input

# question 3 : table of 7 as lisy, convert to vertical

l=[7,14,21,28,35,42,49,56,63,70]
print(*l, sep="\n") # very easy for int list as normal join methods require str type

# alternate

l = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
a = "\n".join([str(x) for x in l])
print(a)

# else map func can be used as well

# question 4 : filter list  divisble by 5

l = [1,4,5,15,20,34,35]
def divisibleby5(n):
    if(n%5==0):
        return True
    return False
a=filter(divisibleby5, l) # task divisibleby5 getting assigned to arg l
print(list(a)) 

# question 5 : find max num in list using reduce func

l = [1,4,5,15,68,20,34,35]
from functools import reduce # this needs to be mentioned if reduce func needs to be used

def greatestnum(a,b):
    if a > b:
        return a
    else:
        return b
print(reduce(greatestnum, l)) 

# question 6 : run pip freeze for system interpretor : take requirements create similar venv

pip freeze > requirements.txt

# create new env, activate it, then :

pip install -r requirements.txt

# question 7 : flask module: create webserver using flask & python

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home/index page
@app.route('/')
def home():
    return "Hello, World! Your Flask web server is running."

# Start the server if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Open your web browser and navigate to http://127.0.0 to see your live web page.