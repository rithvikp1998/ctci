b=str(input()) # Input in binary format

'''
If we can find '101' sequences, flipping the
'0' bit could give the max length sequence. If
there is no '101' sequence, just find the max
length of sequence of 1s and flip the border '0'.
The result will be max of these two possibilities.
'''

last_seq=0
curr_seq=0
ans=0
for i in range(len(b)-1):
    if b[i]=='1':
        curr_seq+=1
    else:
        if curr_seq+last_seq+1>ans:
            ans=curr_seq+last_seq+1
        if b[i+1]=='1':
            last_seq=curr_seq
            curr_seq=0
        else:
            if curr_seq+1>ans:
                ans=curr_seq+1
            curr_seq=0
            last_seq=0
if b[-1]=='1':
    curr_seq+=1
if curr_seq+last_seq+1>ans:
    ans=curr_seq+last_seq+1
print(ans)
