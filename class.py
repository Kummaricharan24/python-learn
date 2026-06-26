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
   
'''


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



'''debited: 1000
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
51000'''