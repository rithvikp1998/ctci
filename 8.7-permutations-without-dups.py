'''
Pretty standard problem and quite similar to the
subsets problem (8.6).

If you need to generate the permutations of string
with n characters, then you can generate the permutations
of string with n-1 characters and the nth character can
be placed in any of the n positions in each if these
permutations of n-1 characters.
'''

def permutations(string):
    if len(string)<=1:
        return [string]
    arr=permutations(string[:-1])
    arr2=[]
    for i in arr:
        for j in range(len(i)+1):
            arr2.append(i[:j]+string[-1]+i[j:])
    return arr2

print(permutations(str(input())))
