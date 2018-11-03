class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,head):
        self.head=head
        self.tail=head

    def addNode(self,node):
        self.tail.next=node
        self.tail=node

    def printList(self):
        curr=self.head
        while curr!=None:
            print(str(curr.value),end=' ')
            curr=curr.next
        print()

def reverseList(mylist):
    p1=mylist.head
    p2=mylist.head.next
    p1.next=None
    while p2!=None:
        t1,t2=p2,p2.next # Temp store
        p2.next=p1
        p1,p2=t1,t2
    mylist.head=p1
    
    return mylist

ip=str(input())

mylist=LinkedList(Node(ip[0]))
reversedList=LinkedList(Node(ip[0]))
for i in ip[1:]:
    mylist.addNode(Node(i))
    reversedList.addNode(Node(i))

reversedList=reverseList(reversedList)
 
'''
Compare the list to the reversed list and voila!
If you have the length of the list n beforehand,
you need compare only upto n//2.
'''

curr1=mylist.head
curr2=reversedList.head
b=0
while curr1!=None:
    if curr1.value!=curr2.value:
        b=1
        print('NO')
        break
    curr1=curr1.next
    curr2=curr2.next
    
if b==0:
    print('YES')
        
