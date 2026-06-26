'''class his:
    def __init__(my,name):
        my.name=name
       
        my.next=None
head= his(10)
head.next=his(20)
head.next.next=his(30)

temp=head
while temp:
    print(temp.name  ,end="->") #op:10->20->30->Null
    
    temp=temp.next
print("Null")


#addding node to data at begging
class his:
    def __init__(my,name):
        my.name=name
        my.next=None

head=his(10)
head.next=his(30)


new_node=his(20)
new_node.next=head
temp=new_node
while temp:
    print(temp.name,end="->")#20->10->30->NULL
    temp=temp.next
print("NULL")




class his:
    def __init__(my,name):
        my.name=name
       
        my.next=None
head= his(10)
head.next=his(20)
head.next.next=his(30)
key=20
temp=head
prev=None
while temp and temp.name !=key:
    prev=temp
    temp=temp.next
    if temp==head:
        head=head.next
    else:
        prev.next=temp.next
    temp=head
    while temp:
        print(temp.name,end="->") #op:10->30->Null
        temp=temp.next

print("Null")

#double linked list
class his:
    def __init__(my,name):
        my.name=name
        my.previous=None
        my.next=None


head=his(10)
secound=his(20)
third=his(30)


head.next=secound


secound.previous=head
secound.next
third.previous=secound
temp=head
while temp:
    print(temp.name,end="")
    if temp.next is not None:
        print(" <-> ", end="")
    temp=temp.next
print("Null")#op:10 <-> 20Null


class his:
    def __init__(my,name):
        my.name=name
        
        my.next=None





head=his(1)
head.next=his(2)
head.next.next=his(3)
head.next.next.next=his(4)
head.next.next.next.next=his(5)


key=5
temp=head
while temp:
    if temp and temp.name ==key:
        print(temp.name)
        
    temp=temp.next

    #double linked list
class his:
    def __init__(my,name):
        my.name=name
        my.previous=None
        my.next=None


head=his(10)
secound=his(20)
third=his(30)


head.next=secound
secound.previous=head

secound.next=third
third.previous=secound


next_node=his(5)

next_node.next=head
head.previous=next_node
head=next_node

temp=head


while temp:
    print(temp.name,end="")
    if temp.next is not None:
        print(" <-> ", end="")
        
    temp=temp.next
print("null")#op:5 <-> 10 <-> 20 <-> 30null'''



class Node:
    def __init__(self, name):
        self.name = name
        self.previous = None
        self.next = None


# ---------------- CREATE LIST ----------------
head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.previous = head

second.next = third
third.previous = second


# ---------------- INSERT AT BEGINNING (5) ----------------
new_node = Node(5)

new_node.next = head
head.previous = new_node
head = new_node


# ---------------- DELETE NODE (20) ----------------
temp = head

while temp:
    if temp.name == 20:

        if temp.previous:
            temp.previous.next = temp.next

        if temp.next:
            temp.next.previous = temp.previous

        if temp == head:
            head = temp.next

        break

    temp = temp.next


# ---------------- PRINT LIST ----------------
temp = head

while temp:
    print(temp.name, end="")
    if temp.next:
        print(" <-> ", end="")
    temp = temp.next

print(" -> null")