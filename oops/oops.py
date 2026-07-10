'''class Student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    def Hello(self):
            print("hello",self.name)
    def Marks(self):
        print("mark for  ",self.age)

s1=Student("charan",97)
s1.Hello()
s1.Marks()
print(s1.name)
print(s1.age)
s2=Student("kishor",88)
print(s2.name)
print(s2.age)
s2.Hello()
s2.Marks()

class Student:
    @staticmethod
    def Colleage():
        print("hello")
    def __init__(self,name,python,java,dsa):
        self.name=name
        self.python=python
        self.java=java 
        self.dsa=dsa
    

    def sum_avg(self):
        sum=s1.python+s1.java+s1.dsa
        sum_avg=(sum)/3
        print(sum_avg)
    
        
s1=Student("charan",85,67,89)
s1.sum_avg()
s1.Colleage()
print(s1.name)
print("my python marks is:",s1.python)
print("my java marks is :",s1.java)
print("my dsa credit score:",s1.dsa)
op:80.33333333333333
charan
my python marks is; 85
my java marks is : 67
my dsa credit score: 89
   



class bank:
    def __init__(self,balance,accno):
        self.balance=balance #10,000
        self.accountno=accno
   
    def debit(self,amount):
        self.balance-=amount
        print("debited:",amount) #10000-1000=90000
        print(self.balance)#=90000
    def credit(self,amount):
        self.balance+=amount
        print("credited :",amount) #9000+2000
        print(self.balance)#=11000
     
        
s1=bank(10000,1234567)
s1.debit(1000)
s1.credit(2000)
s2=bank(20000,1234567)
s2.debit(1000)
s2.credit(2000)
s3=bank(50000,1234567)
s3.debit(1000)
s3.credit(2000)



debited: 1000
9000
credited : 2000
11000
debited: 1000
19000
credited : 2000
21000
debited: 1000
49000
credited : 2000
51000


#delete an object from class 
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("charan", 80)

print(s1.name)
print(s1.age)

del s1.name


print(s1.name)

#praviate keyy "__" twp under scores are used praviate 

class Account:
    def __init__(self,accno,accpass):
        self.accno=accno
        self.__accpass=accpass
    def rest_pass(self):
        print(self.accpass) #op:12345
Acc1=Account("12345","abcd")
print(Acc1.accno)
#print(Acc1.accpass)# its shows like  print(Acc1.accpass) AttributeError: 'Account' object has no attribute 'accpass'

#print(Acc1.rest_pass)#op:<bound method Account.rest_pass of <__main__.Account object at 0x1003006e0>>


#inheritance "class conect to another class "
class Car:
    @staticmethod
    def start():
        print("car started ")
        return
    @staticmethod
    def stop():
        print("car stop ")
        return
    
class toyota(Car):
    def __init__(self,name):
        self.name=name

car=toyota("shift")
print(car.name) 
print(car.start())
result=car.stop()
print(result)
0p:shift
car started 
None
car stop 
None

#inheritance type 2 "single parent class" "single parent child class" and "child class"

class Car:
    @staticmethod
    def start():
        print("car started ",end="")
        return
    @staticmethod
    def stop():
        print("car stop ")
        return
    
class toyota(Car):
    def __init__(self,name):
        self.name=name
class model(toyota):
    def _init__(self,brand):
        self.brand=brand

car=model("shift")
print(car.name) 
print(car.start())
print(car.name)
#op:shift
car started None
shif

#multiple inheritance logic

class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class Power:
    def __init__(self, power):
        self.power = power


class Toyota:
    def __init__(self, name):
        self.name = name


class Model(Car, Toyota, Power):
    
    def __init__(self, name, power, brand):
        Toyota.__init__(self, name)
        Power.__init__(self, power)
        self.brand = brand


car = Model("Shift", "150 HP", "Toyota")

print(car.name)
print(car.power)
print(car.brand)

car.start()
car.stop()
#op:
# Shift
150 HP
Toyota
Car started
Car stopped


class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Power:
    def __init__(self, Power):
        self.Power = Power


class brand(Power,Car):
    def __init__(self,name,type,Power):
       
        super().__init__(Power)
        
#here not __init__ are work like twice they dont know how to the call the class so  first parameter calls first they excute early 
        super().stop()
        self.name=name

car1=brand("shift","lb","50")
print(car1.name)
#print(car1.type)
print(car1.Power)
#op:Car stopped
shift
50

#class method "change the class with attribute"
class Person:
    name="charan"
    def changeName(self,name):
        self.name=name #op:cherry
        'Person.name=name #op:cherry
        self.__class__.name=name#op:cherry
    @classmethod
    def changeName2(cls,name):
        cls.name=name#op:cherry

hi=Person()
#hi.changeName("hairsh")
hi.changeName2("cherry")

print(hi.name)
print(Person.name)#op:name="charan"

#@property uses to change automaticall when change attribute in class
class marks:
    def __init__(self,pyh,chem,java):
        self.pyh=pyh
        self.chem=chem
        self.java=java
    @property
    def percentage(self):
        sum= ((self.pyh+self.chem+self.java)/3)
        print(sum)
s1=marks(70,75,80)
s1.percentage #op:75.0
s1.pyh=94
s1.percentage #op:83.0

#polymarphism method
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def Number(self):
        print(f"{self.real}+{self.img}i")

    def __add__(self,s2):
        newReal=self.real+s2.real
        newImg=self.img+s2.img
        return Complex(newReal,newImg)
        #return newReal newImg
    def __sub__(self,s2):
        newReal=self.real-s2.real
        newImg=self.img-s2.img
        return Complex(newReal,newImg)
    
s1 = Complex(10, 8)
s2 = Complex(5, 4)

print("First Complex Number:")
s1.Number()

print("Second Complex Number:")
s2.Number()

print("Addition:")
s3 = s1 + s2
s3.Number()

print("Subtraction:")
s4 = s1 - s2
s4.Number()
First Complex Number:
10+8i
Second Complex Number:
5+4i
Addition:
15+12i
Subtraction:
5+4i'''