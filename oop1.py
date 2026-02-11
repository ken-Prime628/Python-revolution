class employee:

   #Attributes
    def __init__(self,fullname,position,status,age):
        self.fullname = fullname
        self.position = position
        self.status = status
        self.age = age

    def work(self):
        print(self.fullname,"is working")


employee1 =employee("James Mwenda","MD","Married",54)
print(employee1.fullname,employee1.position,employee1.status,employee1.age)
employee1.work()


employee2 =employee("Jean Kamau",'Program Manager',"Single",34)
employee3 =employee("Mark Joe","lecturer","Single",44)
