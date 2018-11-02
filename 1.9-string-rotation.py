def isSubstring(s1,s2):
    if s1 in s2:
        return True
    else:
        return False

'''
I had to see all the three hints (34, 88, 104)
to figure out the answer :(
'''

s1,s2=input().split()
if isSubstring(s1,s2+s2):
    print('YES')
else:
    print('NO')
