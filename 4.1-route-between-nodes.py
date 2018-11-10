class Node:
    def __init__(self, index):
        self.index=index
        self.adjacent=[]

    def addEdge(self, neighbour_index):
        self.adjacent.append(neighbour_index)

n=int(input()) # No of nodes
graph=[]
for i in range(n):
    graph.append(Node(i))

for i in range(int(input())): # Edges. Nodes should be zero-indexed
    a,b=map(int,input().split())
    graph[a].addEdge(b)

s,e=map(int,input().split()) # Zero-indexed start and end nodes

'''
BFS
'''
visited=[0 for i in range(n)]
visited[s]=1
queue=[s]
b=0
while queue!=[]:
    t=queue[0]
    queue=queue[1:]
    for i in graph[t].adjacent:
        if i==e:
            b=1
            print('YES')
            break
        if visited[i]==0:
            visited[i]=1
            queue.append(i)
    if b==1:
        break
if b==0:
    print('NO')
