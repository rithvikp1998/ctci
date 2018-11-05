arr=[0 for i in range(10)]

'''
Divide the array into 3 equal parts,
use one part to implement one stack.
Some space will be wasted though.
'''
stack1_left=0
stack1_right=len(arr)//3
stack2_left=len(arr)//3
stack2_right=2*(len(arr)//3)
stack3_left=2*(len(arr)//3)
stack3_right=len(arr)-1

stack1_curr=stack1_left
stack2_curr=stack2_left
stack3_curr=stack3_left

def stack1_push(value):
    global stack1_curr
    if stack1_curr<stack1_right:
        arr[stack1_curr]=value
        stack1_curr+=1
    else:
        print("Stack 1 is full")

def stack1_pop():
    global stack1_curr
    if stack1_curr>stack1_left:
        stack1_curr-=1
        return arr[stack1_curr]
    else:
        print("Stack 1 is empty")

def stack2_push(value):
    global stack2_curr
    if stack2_curr<stack2_right:
        arr[stack2_curr]=value
        stack2_curr+=1
    else:
        print("Stack 2 is full")

def stack2_pop():
    global stack2_curr
    if stack2_curr>stack2_left:
        stack2_curr-=1
        return arr[stack2_curr]
    else:
        print("Stack 2 is empty")

def stack3_push(value):
    global stack3_curr
    if stack3_curr<stack3_right:
        arr[stack3_curr]=value
        stack3_curr+=1
    else:
        print("Stack 3 is full")

def stack3_pop():
    global stack3_curr
    if stack3_curr>stack3_left:
        stack3_curr-=1
        return arr[stack3_curr]
    else:
        print("Stack 3 is empty")

print(stack1_pop())
print(stack2_pop())
print(stack3_pop())
stack1_push(1)
stack1_push(2)
stack1_push(3)
stack1_push(4)
stack2_push(1)
stack2_push(2)
stack2_push(3)
stack2_push(4)
stack3_push(1)
stack3_push(2)
stack3_push(3)
stack3_push(4)
print(stack1_pop())
print(stack2_pop())
print(stack3_pop())
print(stack1_pop())
print(stack2_pop())
print(stack3_pop())
print(stack1_pop())
print(stack2_pop())
print(stack3_pop())
print(stack1_pop())
print(stack2_pop())
print(stack3_pop())

'''
TODO Implement dynamic stacks
'''
