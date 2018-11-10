class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def printTree(root): # Pre-order traversal + Sanity check
    if root==None:
        print('None')
        return
    print(root.value)
    print('Going left',end=' ')
    printTree(root.left)
    print('Going right',end=' ')
    printTree(root.right)

'''
The middle element of the input arr will be the root.
The middle element of the left sub-arr will be its
left child and the middle element of the right sub-arr
will be its right child, hence we can recursively build
the tree
'''
def buildTree(arr):
    if arr==[]:
        return None
    node=Node(arr[len(arr)//2])
    node.left=buildTree(arr[:len(arr)//2])
    node.right=buildTree(arr[len(arr)//2+1:])
    return node

ip=list(map(int,input().split()))
root=buildTree(ip)
printTree(root)
