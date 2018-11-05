'''
I couldn't think of a better solution
'''
class Stack:
    def __init__(self):
        self.values=[]

    def push(self,value):
        self.values.append(value)

    def pop(self):
        if self.values==[]:
            return None
        temp=self.values[-1]
        self.values=self.values[:-1]
        return temp

    def peek(self):
        return self.values[-1]

    def isEmpty(self):
        return self.values==[]

    def printStack(self):
        while self.values!=[]:
            print(self.values[-1],end=' ')
            self.values=self.values[:-1]

stack=Stack()
ip=list(map(int,input().split()))
for i in ip:
    stack.push(i)

stack2=Stack()
temp=-1 # Assuming the input contains only non-negative integers
count=0
while not stack.isEmpty(): # Getting length of the stack
    stack2.push(stack.pop())
    count+=1
stack_len=count
for i in range(stack_len):
    count=0
    while not stack2.isEmpty():
        if stack2.peek()>temp:
            if temp!=-1:
                stack.push(temp)
            temp=stack2.pop()
        else:
            stack.push(stack2.pop())
    while count!=stack_len-i-1:
        stack2.push(stack.pop())
        count+=1
    stack.push(temp)
    temp=-1
stack.printStack()
stack2.printStack()
