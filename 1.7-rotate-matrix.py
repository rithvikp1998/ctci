'''
Assuming we are rotating the matrix in clockwise direction, ie.

1 2 3       7 4 1

4 5 6  ==>  8 5 2

7 8 9       9 6 3 

Element at (i,j) becomes the element at (j,n-i+1) (1-based indexing)

'''

n=int(input())
ip=[]
for i in range(n):
    ip.append(list(map(int,input().split())))


# Using additional data structures

op=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        op[j][n-i-1]=ip[i][j]
print(op)


# TODO: Do this in-place. 

