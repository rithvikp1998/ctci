s=input()
op=''
i=0
last=''
count=0
while i<len(s):
    if s[i]!=last:
        op+=str(count)
        last=s[i]
        count=1
        op+=s[i]
    else:
        count+=1
    i+=1
op+=str(count)
op=op[1:]  # There is a '0' at the beginning due to op+=str(count)
if len(op)>len(s):
    print(s)
else:
    print(op)
