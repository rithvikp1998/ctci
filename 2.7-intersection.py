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

ip1=list(map(int,input().split()))
ip2=list(map(int,input().split()))
k1,k2=map(int,input().split())

'''
In order to create an input to test my code,
I am considering the node at k1 position in
list1 is the same as node at k2 position in
list2.
'''

list1=LinkedList(Node(ip1[0]))
list2=LinkedList(Node(ip2[0]))

for i in range(1,k1-1):
    list1.addNode(Node(ip1[i]))

for i in range(1,k2-1):
    list2.addNode(Node(ip2[i]))

'''
Since these are singly-linked lists, every
node after this common node will be the
same in both the lists.
'''
for i in ip1[k1-1:]: 
    node=Node(i)
    list1.addNode(node)
    list2.addNode(node)

'''
Reverse the first list, then traverse the
second list. The traversal should end in
the tail of the reversed first list. There
might be a simpler solution but I didn't
want to see the hints yet :)
'''

list1=reverseList(list1)
curr=list1.head
while curr.next!=None:
    print(curr.value,end=' ')
    curr=curr.next
print(curr.value)
tail1=curr # Tail of the reversed first list

curr=list2.head
while curr.next!=None:
    print(curr.value,end=' ')
    curr=curr.next
print(curr.value)
if curr==tail1:
    print('YES')
else:
    print('NO')

