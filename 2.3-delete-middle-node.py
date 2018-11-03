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

def getKthPointer(k, mylist):
    current=mylist.head
    count=1
    while count<k:
        current=current.next
        count+=1
    return current

ip=list(map(int,input().split()))
k=int(input())

mylist=LinkedList(Node(ip[0]))
for i in ip[1:]:
    mylist.addNode(Node(i))
    
'''
We can't get the pointer to the node via stdin,
hence I will use the getKthPointer() function
which returns the pointer to the Kth node.
'''
node=getKthPointer(k,mylist)

'''
We have access to the node we want to delete and
nothing else, ie, we don't have access to the node
before it to set its 'next' pointer to the node
after it. So, we have to use a different method here,
copy all the elements to the right of the given node
and delete the last node.
'''

p1=node
p2=node.next

while p2.next!=None:
    p1.value=p2.value
    p2=p2.next
    p1=p1.next

p1.value=p2.value
p1.next=None

p1=mylist.head
while p1!=None:
    print(p1.value, end=' ')
    p1=p1.next
    
