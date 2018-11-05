'''
In my implementation, if you use popAt on any
stack other than the latest one, the stacks won't
be rearranged. However, the rearrange operation
itself is quite easy to implement
'''
class Stack:
    def __init__(self, max_size):
        self.max_size=max_size
        self.values=[[]]

    def push(self, value):
        if len(self.values[-1])>=self.max_size:
            self.values.append([value])
        else:
            self.values[-1].append(value)

    def pop(self):
        if len(self.values[-1])==0:
            if len(self.values)==1:
                return None
            else:
                self.values=self.values[:-1]
                temp=self.values[-1][-1]
                self.values[-1]=self.values[-1][:-1]
                return temp
        else:
            temp=self.values[-1][-1]
            self.values[-1]=self.values[-1][:-1]
            return temp

    def popAt(self, index):
        if index>len(self.values)-1:
            return None
        if self.values[index]==[]:
            return None
        else:
            temp=self.values[index][-1]
            self.values[index]=self.values[index][:-1]
            return temp

stack=Stack(int(input()))
while True:
    s=str(input())
    if s=='push':
        stack.push(int(input()))
    elif s=='pop':
        print(stack.pop())
    elif s=='popAt':
        print(stack.popAt(int(input())))
    else:
        print('Incorrect command')
