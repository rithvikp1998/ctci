class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        self.parent=None

n=int(input())
nodes=[Node(i) for i in range(n)]
for i in range(n-1):
    s,a,b=input().split() # s: left or right; a,b: zero indexed
    a,b=int(a),int(b)
    if s=='left':
        nodes[a].left=nodes[b]
        nodes[b].parent=nodes[a]
    else:
        nodes[a].right=nodes[b]
        nodes[b].parent=nodes[a]

n1,n2=map(int,input().split())
node1=nodes[n1]
node2=nodes[n2]

'''
Start from one of the nodes and go to the root
keeping track of all the visited nodes. Now start
from the second node and go to the root checking
if we find a node that has been visited. The first
such node is the first common ancestor.
'''

visited=[0 for i in range(n)]
curr=node1
while curr!=None:
    visited[curr.value]=1
    curr=curr.parent

curr=node2
while curr!=None:
    if visited[curr.value]==1:
        print(curr.value)
        break
    curr=curr.parent
