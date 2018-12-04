'''
The solution for distinct integers was obvious (binary search).
But, for the solution with non-distinct integers, I had to look
at the solution in the book :(
'''

def findMagicIndex(arr, left, right):
    if left<0:
        return -1
    if right>=len(arr):
        return -1
    if right-left<=1:
        if arr[left]==left:
            return left
        if arr[right]==right:
            return right
    else:
        mid=(left+right)//2
        if arr[mid]==mid:
            return mid

        t=findMagicIndex(arr, mid+1, right)
        if t>=0:
            return t

        t=findMagicIndex(arr, left, mid-1)
        if t>=0:
            return t
        
    return -1
        
arr=list(map(int,input().split()))
print(findMagicIndex(arr, 0, len(arr)-1))
