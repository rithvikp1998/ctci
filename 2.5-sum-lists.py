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

n1=int(input())
ip1=list(map(int,input().split()))
n2=int(input())
ip2=list(map(int,input().split()))

list1=LinkedList(Node(ip1[0]))
for i in ip1[1:]:
    list1.addNode(Node(i))

list2=LinkedList(Node(ip2[0]))
for i in ip2[1:]:
    list2.addNode(Node(i))

'''
An easier implementation IMO is to convert
lists to numbers, add them and convert the
result back to a list
'''

curr=list1.head
num1=0
count=0
while curr!=None:
    num1+=(curr.value)*(10**count)
    curr=curr.next
    count+=1

curr=list2.head
num2=0
count=0
while curr!=None:
    num2+=(curr.value)*(10**count)
    curr=curr.next
    count+=1

ans=num1+num2
ansList=LinkedList(Node(ans%10))
ans=ans//10
while ans>0:
    ansList.addNode(Node(ans%10))
    ans=ans//10

ansList.printList()

'''
Probably the intended way
'''

# Add leading zeros to the shorter list

if n1>n2:
    for i in range(n1-n2):
        list2.addNode(Node(0))
elif n1<n2:
    for i in range(n2-n1):
        list1.addNode(Node(0))

p1=list1.head
p2=list2.head
ansList=LinkedList(Node((p1.value+p2.value)%10))
carry=(p1.value+p2.value)//10
p1=p1.next
p2=p2.next
while p1!=None:
    ansList.addNode(Node((p1.value+p2.value+carry)%10))
    carry=(p1.value+p2.value+carry)//10
    p1=p1.next
    p2=p2.next
if carry!=0:
    ansList.addNode(Node(carry))

ansList.printList()

'''
If the input is given in forward order
'''

list1=reverseList(list1)
list2=reverseList(list2)

# Add leading zeros to the shorter list

if n1>n2:
    for i in range(n1-n2):
        list2.addNode(Node(0))
elif n1<n2:
    for i in range(n2-n1):
        list1.addNode(Node(0))

p1=list1.head
p2=list2.head
ansList=LinkedList(Node((p1.value+p2.value)%10))
carry=(p1.value+p2.value)//10
p1=p1.next
p2=p2.next
while p1!=None:
    ansList.addNode(Node((p1.value+p2.value+carry)%10))
    carry=(p1.value+p2.value+carry)//10
    p1=p1.next
    p2=p2.next
if carry!=0:
    ansList.addNode(Node(carry))

ansList=reverseList(ansList)
ansList.printList()
