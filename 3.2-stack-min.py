'''
We can just maintain a second list which stores
the min-so-far values
'''

class Stack:
    def __init__(self):
        self.values=[] # You can use doubly-linked linked list instead
        self.mins=[]
    def push(self, value):
        if self.values==[]:
            self.values.append(value)
            self.mins.append(value)
        else:
            self.values.append(value)
            if value<self.mins[-1]:
                self.mins.append(value)
            else:
                self.mins.append(self.mins[-1])
    def pop(self):
        if self.values!=[]:
            temp=self.values[-1]
            self.values=self.values[:-1]
            self.mins=self.mins[:-1]
            return temp
        else:
            return

    def min(self):
        return self.mins[-1]

stack=Stack()

while True:
    s=str(input())
    if s=='push':
        stack.push(int(input()))
    elif s=='pop':
        print(stack.pop())
    elif s=='min':
        print(stack.min())
    else:
        print('Invalid command')
