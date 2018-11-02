s,n=input().split(',')
n=int(n)

# Using python stdlib function

print(s[:n].replace(' ','%20')) # This feels like cheating

# Replacing manually

op=''
for i in s[:n]:
    if i==' ':
        op+='%20'
    else:
        op+=i
print(op)

# Doing this in-place (the intended way?). Used hint 53

i=n-1
j=len(s)-1

# We now have two indicators, i (last non-space char in the string) and
# j(the last index in s). Keep sliding i to the left and copy the chars
# starting at j and filling the s from the end. If you encounter a space,
# just replace it with '%20'

while i>0:
    if s[i]!=' ':
        s=s[:j]+s[i]+s[j+1:]
        j-=1
        i-=1
    else:
        s=s[:j-2]+'%20'+s[j+1:]
        j-=3
        i-=1

print(s)
