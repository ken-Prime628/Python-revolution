# Parent class/Super class/Base class - This is the class that we are borrowing from
class Animal:
    isMammal = True

    def speak(self):
        print("Animal is speaking")

    def move(self):
        print("Animal is moving")

 # Child class/Sub class/Derived class - the class that has borrowed from the parent class
class cat(Animal):
    def sound(self):
        print("Cat is meowing")

    def climb(self):
        print("Cat is climbing a tree")


class horse(Animal):
    hasTail = True

    def speak(self):
        print("Horse is speaking")


    def neigh(self):
        print("Horse is neighing")


a =Animal()
c =cat
h=horse()