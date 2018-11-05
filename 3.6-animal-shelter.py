'''
I am just checking if the customer gets a dog or a cat.
The solution can easily be extended to add a unique id
to the animals.
'''
class Node:
    def __init__(self, value):
        self.value=value # Either 'cat' or 'dog'.
        self.next=None
        self.prev=None

class Queue:
    def __init__(self):
        self.head=None
        self.tail=None

    def enqueue(self, value):
        if self.head==None:
            self.head=Node(value)
            self.tail=self.head
        else:
            self.tail.next=Node(value)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next

    def dequeueAny(self):
        if self.head==None:
            return None
        temp=self.head.value
        self.head=self.head.next
        if self.head!=None:
            self.head.prev=None
        return temp

    def dequeueDog(self):
        if self.head==None:
            return None
        curr=self.head
        while curr!=None:
            if curr.value=='dog':
                if curr.prev==None and curr.next==None:
                    self.head=None
                    self.prev=None
                elif curr.prev==None:
                    self.head=curr.next
                    curr.next.prev=None
                elif curr.next==None:
                    self.tail=curr.prev
                    curr.prev.next=None
                else:
                    curr.prev.next=curr.next
                    curr.next.prev=curr.prev
                return 'dog'
            curr=curr.next
        return None

    def dequeueCat(self):
        if self.head==None:
            return None
        curr=self.head
        while curr!=None:
            if curr.value=='cat':
                if curr.prev==None and curr.next==None:
                    self.head=None
                    self.prev=None
                elif curr.prev==None:
                    self.head=curr.next
                    curr.next.prev=None
                elif curr.next==None:
                    self.tail=curr.prev
                    curr.prev.next=None
                else:
                    curr.prev.next=curr.next
                    curr.next.prev=curr.prev
                return 'cat'
            curr=curr.next
        return None

    def printList():
        curr=self.head
        while curr!=None:
            print(curr.value)
            curr=curr.next

queue=Queue()
while True:
    s=str(input())
    if s=='enqueue':
        queue.enqueue(str(input())) # Input only 'cat' or 'dog'
    elif s=='dequeueAny':
        print(queue.dequeueAny())
    elif s=='dequeueDog':
        print(queue.dequeueDog())
    elif s=='dequeueCat':
        print(queue.dequeueCat())
    else:
        print('Invalid command')
    
    
            
            
