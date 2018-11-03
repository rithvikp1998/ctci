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

ip=list(map(int,input().split()))
k=int(input()) # Inorder to test the code, I am assuming the loop begins at node k

mylist=LinkedList(Node(ip[0]))
count=1
loop_entry=None
for i in ip[1:]:
    if count==k-1:
        loop_entry=Node(i)
        mylist.addNode(loop_entry)
    else:
        mylist.addNode(Node(i))
    count+=1
mylist.tail.next=loop_entry

'''
I couldn't solve the problem by myself
so I ended up looking the solution on
the internet :(

1. Use the runner method to detect if there is a loop
2. If there is a loop, find it's size
3. Start from the head again with two pointers separated
   by loop_size-1 nodes in between. Move both the pointers
   by one node at a time until they intersect. That's the
   required node.
'''

# Finding if there is a loop

p1=mylist.head
p2=p1.next
while p2!=None:
    if p1==p2:
        break
    p1,p2=p1.next,p2.next.next

# Finding the length of the loop.
# Freeze p1 and move p2 until it coincides with p1 again.

count=1
p2=p2.next
while p1!=p2:
    #print(p2.value)
    p2=p2.next
    count+=1

# Start again with two pointers separated by count-1 nodes in between

p1=mylist.head
p2=mylist.head
for i in range(count):
    p2=p2.next

while p1!=p2:
    p1,p2=p1.next,p2.next

print(p1.value)


