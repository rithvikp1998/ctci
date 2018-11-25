'''
(n & (n-1)) will be zero in the following cases:
1. n is zero
2. n-1 is zero
3. n is a power of 2. If n='100000', n-1='011111', n&(n-1) is zero

In every other case, there is atleast a common '1' bit in both n and n-1
and (n & (n-1)) will not be zero.
'''
import math

def myPrediction(n):
    if n==0 or n==1:
        return True
    if math.log(n,2)%1==0:
        return True
    return False

# Testing my predictions
b=0
for n in range(10000000):
    if ((n&(n-1))==0)==myPrediction(n):
        continue
    else:
        print('Test failed for n:', str(n))
        b=1
        break
if b==0:
    print('Tests passed')
