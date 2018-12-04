'''
If the child is currently on the nth step,
then there are three possibilites as to how
it reached there:

1. Reached (n-3)th step and hopped 3 steps in one time
2. Reached (n-2)th step and hopped 2 steps in one time
3. Reached (n-1)th step and hopped 2 steps in one time

The total number of possibilities is the sum of these 3
'''
def count_possibilities(n, store):
    if store[n]!=0:
        return
    count_possibilities(n-1, store)
    count_possibilities(n-2, store)
    count_possibilities(n-3, store)
    store[n]=store[n-1]+store[n-2]+store[n-3]
    
n=int(input())
store=[0 for i in range(n+1)] # Stores the number of possibilites for every i<n
store[0]=0
store[1]=1
store[2]=2
store[3]=4

count_possibilities(n, store)
print(store[n])
