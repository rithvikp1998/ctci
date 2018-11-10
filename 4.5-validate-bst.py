class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def validate(root):
    if root==None:
        return 1
    if root.left==None and root.right==None:
        return 1
    elif root.right==None:
        if root.left.value<=root.value:
            return validate(root.left)
        else:
            return 0
    elif root.left==None:
        if root.right.value>root.value:
            return validate(root.right)
        else:
            return 0
    else:
        if root.left.value>root.value or root.right.value<=root.value:
            return 0
        return min(validate(root.left), validate(root.right))
    

n=int(input()) # No.of nodes
nodes=[Node(i) for i in range(n)]
root=nodes[int(input())] # Root node, zero indexed
for i in range(n-1): # Edges
    subtree,a,b=input().split() # subtree: left or right; a,b: zero indexed
    if subtree=='left':
        nodes[int(a)].left=nodes[int(b)]
    else:
        nodes[int(a)].right=nodes[int(b)]

if validate(root):
    print('YES')
else:
    print('NO')
