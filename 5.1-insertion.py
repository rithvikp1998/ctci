n,m=map(int,input().split())
i,j=map(int,input().split())

mask1=~((2**(j-i+1)-1)<<i)
mask2=m<<i
print(bin(n),bin(m))
print(bin((n&mask1)|mask2)) # There might be a simpler method
