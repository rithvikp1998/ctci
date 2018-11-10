class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

def getLeftMost(node):
    while node.left!=None or node.right!=None:
        if node.left==None:
            node=node.right
        else:
            node=node.left
    return node

def followAncestors(node):
    if node.parent==None: # root node
        return None
    while node.parent!=None:
        if node.parent.left==node:
            break
        node=node.parent
    return node.parent

n=int(input())
nodes=[Node(i) for i in range(n)]
root=nodes[int(input())]
for i in range(n-1): # Edges
    subtree,a,b=input().split() # subtree: left or right; a,b: zero indexed
    a,b=int(a),int(b)
    if subtree=='left':
        nodes[a].left=nodes[b]
        nodes[b].parent=nodes[a]
    else:
        nodes[a].right=nodes[b]
        nodes[b].parent=nodes[a]
    
s=nodes[int(input())] # The node whose successor we need to find

'''
Pretty standard question. If the node has a right
child, find the left most element of the node's right
subtree. If the right child is None, keep going up
the ancestral chain until you find a node that is the
left child of its parent.
'''
if s.right!=None:
    print(getLeftMost(s.right).value)
else:
    t=followAncestors(s)
    if t==None:
        print(None)
    else:
        print(t.value)
        
