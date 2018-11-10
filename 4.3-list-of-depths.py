class TreeNode:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None

def buildTree(arr): # From a previous solution
    if arr==[]:
        return None
    node=TreeNode(arr[len(arr)//2])
    node.left=buildTree(arr[:len(arr)//2])
    node.right=buildTree(arr[len(arr)//2+1:])
    return node

def traverse(root, depthMap, depth): # DF traversal
    if root==None:
        return
    depthMap[root.value]=depth
    traverse(root.left, depthMap, depth+1)
    traverse(root.right, depthMap, depth+1)

class ListNode:
    def __init__(self, value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self, head):
        self.head=head
        self.tail=head

    def addNode(self, node):
        self.tail.next=node
        self.tail=node

    def printList(self):
        curr=self.head
        while curr!=None:
            print(curr.value, end=' ')
            curr=curr.next
        print()

n=int(input())
ip=[i for i in range(n)]
root=buildTree(ip)

depthMap=[0 for i in range(len(ip))] # Stores the depth of visited nodes
traverse(root, depthMap, 1)
lists={}
for i in range(n):
    if depthMap[i] not in lists:
        lists[depthMap[i]]=LinkedList(ListNode(i))
    else:
        lists[depthMap[i]].addNode(ListNode(i))

for i in lists:
    print(i, end=': ')
    lists[i].printList()
    
