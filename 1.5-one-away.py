s,s2=input().split(',')
s,s2=s.strip(), s2.strip()
n,n2=len(s), len(s2)

if abs(n-n2)>1:
    print('NO')
elif n==n2: # Only replace possible
    b=0
    c=0
    for i in range(n):
        if s[i]!=s2[i]:
            if b==1:
                c=1
                print('NO')
                break
            else:
                b=1
    if c==0:
        print('YES')
else: # Only insert or remove possible
    
    # Making the longer string the second one so that only insert is possible
    if n>n2:
        s,s2=s2,s
        n,n2=n2,n
    i=0
    i2=0
    b=0
    c=0
    while i<n:
        if s[i]==s2[i2]:
            i+=1
            i2+=1
        else:
            if b==1:
                c=1
                print('NO')
                break
            else:
                b=1
            i+=1
            i2+=2
    if c==0:
        print('YES')
    
    
    
