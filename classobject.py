# A Class is a blueprint of an object.
#Object is an instance of a class

class student:  # Has two members attribute and behaviour
    #Attributes - they are simply the characteristics
  name ="Kennedy"
  age =18
  gender ="Male"
  course ="MIT"


    #Behaviour - Writen as Functions
  def study(self):
      print("Student is studying")


student1 =student() # Creating an object
student1.study()
print(student1.name)

student2 = student()

student3 = student()
