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

mylist=LinkedList(Node(ip[0]))
for i in ip[1:]:
    mylist.addNode(Node(i))

'''
If extra buffer is allowed, use a hash table.
Then we can solve this in O(n) time.
'''
present={}
p1=mylist.head
p2=p1.next
present[p1.value]=1
while p2 is not None:
    if p2.value in present: # Delete node. The 'in' operation takes O(1)
        p1.next=p2.next
    else:
        present[p2.value]=1
    p1,p2=p2,p2.next

mylist.printList()

'''
TODO

If extra buffer is not allowed, we can sort the
linked list and then eliminate the duplicates.
Or there might be a better solution in the hints.
'''

