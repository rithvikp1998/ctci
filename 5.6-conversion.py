a,b=map(int,input().split())
bina, binb=bin(a)[2:], bin(b)[2:]
# Add leading zeros to smaller number, if needed.
if len(bina)>len(binb):
    while len(binb)<len(bina):
        binb='0'+binb
elif len(binb)>len(bina):
    while len(bina)<len(binb):
        bina='0'+bina
count=0
for i in range(len(bina)):
    if bina[i]!=binb[i]:
        count+=1
print(bin(a), bin(b))
print(count)
