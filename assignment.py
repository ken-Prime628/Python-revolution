
#A python Program that prompts a user to enter
#a number and checks whether the number is
#even or odd

number =int(input("enter a number :"))

if number==0:
    print("Number is neutral")

elif number %2==0:
    print("Number is even")
else:
    print("Number is odd")