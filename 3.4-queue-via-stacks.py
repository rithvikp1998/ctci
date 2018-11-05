'''
Always push into first stack. When pop() is called,
if the second stack is not empty, pop from it. If it
is empty, pop all elements from first stack and push
them into second stack
'''
class MyQueue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue(self,value):
        self.stack1.append(value)

    def dequeue(self):
        if self.stack2==[]:
            if self.stack1==[]:
                return None
            else:
                while self.stack1!=[]:
                    self.stack2.append(self.stack1[-1])
                    self.stack1=self.stack1[:-1]
                temp=self.stack2[-1]
                self.stack2=self.stack2[:-1]
                return temp
        else:
            temp=self.stack2[-1]
            self.stack2=self.stack2[:-1]
            return temp

queue=MyQueue()
while True:
    s=str(input())
    if s=='enqueue':
        queue.enqueue(int(input()))
    elif s=='dequeue':
        print(queue.dequeue())
    else:
        print('Invalid command')
