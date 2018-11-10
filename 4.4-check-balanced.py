class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def setHeights(root, heightMap):
    if root==None:
        return
    if root.left==None and root.right==None: # leaf node
        heightMap[root.value]=1
    elif root.right==None:
        setHeights(root.left, heightMap)
        heightMap[root.value]=heightMap[root.left.value]+1
    elif root.left==None:
        setHeights(root.right, heightMap)
        heightMap[root.value]=heightMap[root.right.value]+1
    else:
        setHeights(root.left, heightMap)
        setHeights(root.right, heightMap)
        heightMap[root.value]=max(heightMap[root.left.value], heightMap[root.right.value])+1

def balanceCheck(root, heightMap, isBalanced):
    if root==None:
        return
    if root.left==None and root.right==None: # leaf node
        if heightMap[root.value]!=1:
            isBalanced[0]=False
            return
    elif root.right==None:
        if heightMap[root.left.value]>1:
            isBalanced[0]=False
            return
        balanceCheck(root.left, heightMap, isBalanced)
    elif root.left==None:
        if heightMap[root.right.value]>1:
            isBalanced[0]=False
            return
        balanceCheck(root.right, heightMap, isBalanced)
    else:
        if abs(heightMap[root.left.value]-heightMap[root.right.value])>1:
            isBalanced[0]=False
            return
        balanceCheck(root.left, heightMap, isBalanced)
        balanceCheck(root.right, heightMap, isBalanced)
    
n=int(input()) # No.of nodes
nodes=[Node(i) for i in range(n)]
root=nodes[int(input())] # Root node
for i in range(n-1): # Edges
    subtree,a,b=input().split() # subtree: left or right; a,b:Zero indexed
    if subtree=='left':
        nodes[int(a)].left=nodes[int(b)]
    else:
        nodes[int(a)].right=nodes[int(b)]
'''
Traverse the tree first, assigning the heights to nodes in a bottom-up
approach ie leaves get a height of 1 and a parent of two leaves get a
height of 2 and so on. Then traverse the tree again, this time comparing
the heights of the left subtree and right subtree.
'''
heightMap=[0 for i in range(n)] # Stores the heights of trees rooted at a node
setHeights(root, heightMap)
isBalanced=[True] # Inside an array to make it mutable. We can eliminate isBalanced as a param altogether.
balanceCheck(root, heightMap, isBalanced)
if isBalanced[0]:
    print('YES')
else:
    print('NO')
