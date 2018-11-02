m,n=map(int,input().split())
ip=[]
for i in range(m):
    ip.append(list(map(int,input().split())))

'''
Traverse the rows once keeping track of all the rows
and columns which should finally be set to 0.
'''
rows=[0 for i in range(m)]
columns=[0 for i in range(n)]

for i in range(m):
    for j in range(n):
        if ip[i][j]==0:
            rows[i]=1
            columns[j]=1

for i in range(m):
    if rows[i]==1:
        for j in range(n):
            ip[i][j]=0

for i in range(n):
    if columns[i]==1:
        for j in range(m):
            ip[j][i]=0

print(ip)
