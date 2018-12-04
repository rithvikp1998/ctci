'''
The recursive solution here is pretty straight forward.
The subsets of set {1,2,3,4} = The subsets of set {1,2,3}
+ The subsets which would be created because of the '4' (all
these subsets must have a 4 in them because the ones without
4 are already counted while counting subsets of {1,2,3})

'''

def getSubsets(s):
    if s==[]:
        return [s]
    if len(s)==1:
        return [[],[s[0]]]
    arr=getSubsets(s[:-1])
    n=len(arr)
    for i in range(n):
        arr.append(arr[i]+[s[-1]])
    return arr

s=list(map(int,input().split()))
subsets=getSubsets(s)
print('# of subsets:', len(subsets))
print(subsets)
