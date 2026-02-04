
age =18     #Integer

weight =55.4     #Float

greeting ="Hello There"   #String

isMammal =True   #Boolean

#Data Structures - Multiple Elements in One Variable
fruits =["Banana","Mango","Cherry"]    #List - It is Ordered And Changeable - Different Datatypes

courses =["MIT","DataScience","CyberSecurity"]  #Array - Carries Similar Datatypes

cars =("ford","G-Wagon","Mazda","Mitsubishi")    #Tuple -Elements Are Ordered and Unchangeable

countries ={"Tanzania","India","Italy"}  #Set -Elements are Unordered and Unchangeable

student ={
    "Firstname" : "Kennedy",
    "course" : "MIT",
    "age" :18,
    "nationality":"Kenyan"
}  #Dictionery -Key Value Pair


print("student is",age,"years old")
print(weight)
print("Is animal a mammal?:",isMammal)
print(fruits)
print(countries)



#Typecasting - This is Converting One Datatype into another
print(float(age))
print(int(weight))