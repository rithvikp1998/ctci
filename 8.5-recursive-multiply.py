'''
At first, I thought of representing two numbers n,m as
n=10a+b
m=10c+d

But, writing n=2a+b and m=2c+d was making it easier to
implement in the code. And I guess it takes fewer operations
since we can use bit shifting.

n=2a+b; m=2c+d
a=n//2; c=m//2; b=n%2; d=m%2
nm=4ac+2ad+2bc+bd


TODO: Calculate which of these two methods take lesser
number of operations.
'''

def multiply(n,m):
    if n==0 or m==0:
        return 0
    if n==1:
        return m
    if m==1:
        return n
    a=n//2
    c=m//2
    b=n%2
    d=m%2
    return (multiply(a,c)<<2)+(multiply(a,d)<<1)+(multiply(b,c)<<1)+(multiply(b,d))

n,m=map(int,input().split())
print(multiply(n,m))
