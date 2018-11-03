'''
I want to use the same technique used in Quicksort.
In order to do that I need to be able to move forward
and backward in the list. Hence I am creating a second
list that is the reverse of the original list. There
might be a simpler solution but I didn't want to see
the hints :)
'''

class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, head):
        self.head=head
        self.tail=head

    def addNode(self, node):
        self.tail.next=node
        self.tail=node

    def printList(self):
        curr=self.head
        while curr!=None:
            print(str(curr.value),end=' ')
            curr=curr.next
        print()

def printAns(mylist,reversedList,left,right):
    curr=mylist.head
    for i in range(left):
        print(str(curr.value),end=' ')
        curr=curr.next
    curr=reversedList.head
    for i in range(right+1):
        print(str(curr.value),end=' ')
        curr=curr.next

n=int(input()) # Lenght of the list
ip=list(map(int,input().split())) # List elements
key=int(input()) # Partition key

mylist=LinkedList(Node(ip[0]))
reversedList=LinkedList(Node(ip[0]))
for i in ip[1:]:
    mylist.addNode(Node(i))
    reversedList.addNode(Node(i))
    
p1=reversedList.head
p2=reversedList.head.next
p1.next=None
while p2!=None:
    t1,t2=p2,p2.next # Temp store
    p2.next=p1
    p1,p2=t1,t2
reversedList.head=p1

left=0
right=0
p1=mylist.head
p2=reversedList.head
while True:
    while p1.value<key and n-right-1>left:
        p1=p1.next
        left+=1
    while p2.value>=key and n-right-1>left:
        p2=p2.next
        right+=1
    if n-right-1<=left:
        printAns(mylist,reversedList,left,right)
        break
    p1.value,p2.value=p2.value,p1.value

    

    
    
    

