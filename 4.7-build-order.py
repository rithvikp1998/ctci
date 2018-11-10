class Node:
    def __init__(self, value):
        self.value=value
        self.dependencies=[]

def dfs(i, nodes, depthMap):
    if visited[i]==2:
        raise Exception # loop present. Better to use custom exception class.
    visited[i]=2 # Used to detect loops
    if visited[i]==1:
        return
    if nodes[i].dependencies==[]:
        visited[i]=1
        depthMap[i]=1
        return
    for j in nodes[i].dependencies:
        dfs(j, nodes, depthMap)
    depthMap[i]=max([depthMap[j] for j in nodes[i].dependencies])+1
    visited[i]=1
    
n=int(input())
nodes=[Node(i) for i in range(n)] # Using indexes instead of alphabets
for i in range(int(input())):
    a,b=map(int,input().split())
    nodes[b].dependencies.append(a)

visited=[0 for i in range(n)]
depthMap=[0 for i in range(n)]

for i in range(n):
    if visited[i]==1:
        continue
    else:
        try:
            dfs(i, nodes, depthMap)
        except:
            b=1
if b==1:
    print("No valid order")
else:
    order={}
    for i in range(n):
        if depthMap[i] not in order:
            order[depthMap[i]]=[i]
        else:
            order[depthMap[i]].append(i)

    for i in sorted(order.keys()):
        for j in order[i]:
            print(j, end=' ')
        
    
