'''class cricle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        sum=(22/7)*self.radius**2
        print(sum) #op:1384.0

    def perimeter(self):
        sum= 2*(22/7)*self.radius
        print(sum)#op:131.0
131.88
s1=cricle(21)
s1.area()
s1.perimeter()

#question 2
class Emp:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

        
class Engineer(Emp):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("engineer","it","65,000") 
eng1=Engineer("charan","25")
eng1.showDetails()
print(eng1.name)
print(eng1.age)
op:role= engineer
dept= it
salary= 65,000
charan
25'''

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price > ord2.price
        
        
ord1=Order("chips",30) 
ord2=Order("banana",20)
print(ord1>ord2)#op:True

