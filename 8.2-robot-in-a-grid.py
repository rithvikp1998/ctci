'''
Assume you have to go to cell (x,y), then there
are two possibilities:

1. You go to (x-1,y) if a route exists,
   then go down from there.
2. You go to (x,y-1) if a route exists,
   then go right from there.

If you can't do either of those, then you are stuck.

'''

def getPath(grid, x, y):
    print(x,y) # Just to see how the grid is traversed in the recursive calls
    if x==0 and y==0:
        return ''
    if grid[x][y]=='x': # Indicates an off-limit cell
        return -1
    if x<0 or y<0: # Went off the grid
        return -1

    temp=getPath(grid,x-1,y)
    if temp!=-1: # There is a path from start to the cell to our north
        return temp+'D'

    temp=getPath(grid,x,y-1)
    if temp!=-1: # There is a path from start to the cell to our west
        return temp+'R'

    return -1

n=int(input()) # Assuming a n x n grid
grid=[str(input()) for i in range(n)]
print(getPath(grid,n-1,n-1))
