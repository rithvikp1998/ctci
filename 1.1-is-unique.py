s=input()

# Using additional data structures

counter=[0 for i in range(256)] # 1-byte chars
b=0
for i in s:
    if counter[ord(i)]==1:
        b=1
        print('NO')
        break
    else:
        counter[ord(i)]=1
if b==0:
    print('YES')

# Without using additional data structures

s=sorted(s)
for i in range(len(s)-1):
    if s[i+1]==s[i]:
        b=1
        print('NO')
        break
if b==0:
    print('YES')
