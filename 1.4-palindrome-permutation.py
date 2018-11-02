s=input()
s=s.replace(' ','') # From the example, it seems that spaces are to be ignored
s=s.lower() # From the example, it seems case doesn't matter

counter=[0 for i in range(256)]
for i in s:
    counter[ord(i)]+=1

# Palindromes can have one char appearing odd number of times,
# but all the other chars must appear twice

b=0
c=0
for i in counter:
    if i%2==1:
        if b==1:
            c=1
            print('NO')
            break
        else:
            b=1
if c==0:
    print('YES')
        
