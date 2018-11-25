s=str(input()) # Number n in binary format
s='0'+s # Trailing zero will make the code run for '11111' etc. without changes

first1=-1
seqend=-1
if s[-1]=='0':
    '''
    If s ends with '0', the next biggest number will be '1' followed by the
    number of '0's + one extra '0' followed by the number of '1's. For ex:

    if s   = 111000
    answer = 1000011
    '''
    for i in range(len(s)):
        if s[len(s)-i-1]=='1':
            if first1==-1:
                first1=len(s)-i-1
        else:
            if first1!=-1:
                seqend=len(s)-i-1+1
                break
    if seqend==0:
        print('Next smallest:', s[1:seqend]+'1'+(len(s)-1-first1+1)*'0'+(first1-seqend)*'1')
        next_smallest=int(s[1:seqend]+'1'+(len(s)-1-first1+1)*'0'+(first1-seqend)*'1',2)
    else:
        print('Next smallest:', s[1:seqend-1]+'1'+(len(s)-1-first1+1)*'0'+(first1-seqend)*'1')
        next_smallest=int(s[1:seqend-1]+'1'+(len(s)-1-first1+1)*'0'+(first1-seqend)*'1',2)
else:
    '''
    If s ends with '1', find the first '0' from the right, swap it with
    the bit just right of it.

    if s   = 111000111
    answer = 111001011
    '''
    first1=len(s)-1
    for i in range(len(s)):
        if s[len(s)-i-1]=='0':
            seqend=len(s)-i-1+1
            break
    print('Next smallest:', s[1:seqend-1]+'1'+'0'+(first1-seqend)*'1')
    next_smallest=int(s[1:seqend-1]+'1'+'0'+(first1-seqend)*'1', 2)

'''
I am assuming we cannot add trailing zero to the end, otherwise
next largest doesn't make much sense since we can keep adding trailing
zeros and the number will get larger and larger.

If s in not all '1's, the next largest will be the one with all '1's to
the left (if s is already the number with all '1's to the left, just add
a trailing zero). If s is all '1's the next largest will be s+'0'
'''
s=s[1:] # Remove the trailing zero we added earlier
print('Next largest:',end=' ')
if '0' not in s:
    print(s)
    next_largest=int(s,2)
else:
    ones=s.count('1')
    if s.index('0')==ones: # s is already all '1's to the left
        print(s)
        next_largest=int(s,2)
    else:
        print('1'*ones+'0'*(len(s)-ones))
        next_largest=int('1'*ones+'0'*(len(s)-ones),2)

# Testing next smallest code
i=int(s,2)+1
ones=s.count('1')
while True:
    if bin(i).count('1')==ones:
        if i==next_smallest:
            print('Next smallest test passed')
            break
        else:
            print('Next smallest test failed, found: ' + bin(next_smallest)[2:] + ' , needed: ' + bin(i)[2:])
            break
    i+=1

# Testing next largest code
i=int('1'*len(s),2)
while i>0:
    if bin(i).count('1')==ones:
        if i==next_largest:
            print('Next largest test passed')
            break
        else:
            print('Next largest test failed, found: ' + bin(next_largest)[2:] + ' , needed: ' + bin(i)[2:])
            break
    i-=1
