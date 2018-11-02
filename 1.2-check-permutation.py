s,s2=input().split()

# Using additional data structures

counter=[0 for i in range(256)] # 1-byte chars
b=0
for i in s:
    counter[ord(i)]+=1
for i in s2:
    counter[ord(i)]-=1
for i in counter:
    if i!=0:
        b=1
        print('NO')
        break
if b==0:
    print('YES')
    
# Without using additional data structures
if sorted(s)==sorted(s2):
    print('YES')
else:
    print('NO')

