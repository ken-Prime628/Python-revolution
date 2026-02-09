# Functions/Methods -A block of code used tu perform a task

# Standard - Library Functions / Inbuilt
y = max(45,78,89,43,2,456,2334,34,98)
print("The maximum number is",y)

x = min(45,78,89,43,2,456,2334,34,98)
print("The minimum number is",x)

print()

# User - defined Functions
def name():
    print("kennedy")

 # calling the function which is important
name()

print()

def add():
    print(10+20)

add()

print()

def dog(): # limits me to only this details below
    name ="Bob"
    breed ="Siberian Husky"
    age =4
    print(name,breed,age)

print()

# Parameter/Variables passed in the brackets of the function
# Arguments - Values passed when Calling a function
def dog(name,breed,age):
    print(name,breed,age)

dog("Bob","German Shepherd",5)
dog("Mary","Chihuahua",2)
dog("Peter","Siberian Husky",4)


# A program to display details of five employees at eMobilis

# Use a user-defined function with the help of parameters and arguments.

# Details - Fullname, position, gender, age

print()


def employee(fullname,position,gender,age):
    print(fullname,position,gender,age)

employee("Kennedy","Director","Male",34)
employee("Philip","CEO","Male",32)
employee("Suzan","Secretary","Female",30)
employee("James","Manager","Male",31)
employee("Grace","Receptionist","Female",33)





