'''
We need to modify the code written for 8.7 inorder
to make it work for strings with duplicates. In 8.7,
we were able to generate permutation of string with
n-1 characters and place the nth character in all
possible places (ie n places). Here, doing so will
create duplicates. So, instead of generating permutations
of n-1 characters and placing the nth character in
different places, we can fix the position of the nth
character and generate permutations of all other n-1
character strings. Plus, we need to keep count of the
characters so that we don't fix the same nth character
multiple times.
'''

def permutations(char_count, length):
    if length==0:
        return ['']
    perms=[]
    for i in char_count.keys():
        if char_count[i]>0:
            char_count[i]-=1 # Fixing this as the nth character, in the first place
            temp=permutations(char_count, length-1)
            char_count[i]+=1 # We have to set the count back so that the next key can use it to generate perms
            for j in temp:
                perms.append(i+j)
    return perms

s=str(input())
char_count={}
for i in s:
    if i in char_count:
        char_count[i]+=1
    else:
        char_count[i]=1

ans=permutations(char_count, len(s))
print('# of permutations: ', len(ans))
print(ans)
