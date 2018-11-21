'''
The probability that a family has n children is 1/(2^n),
ie they have n-1 boys and 1 girl. The gender ratio of boys
to girls is (n-1)/1. The expected value of gender ratio
is limit(sum(((n-1)/1)*(1/(2^n)))) where n->infinity. The
limit can be calculated on paper and it's value will be 1.
'''

ans=0
for n in range(1, 100):
    ans+=((n-1)/1)*(1/(2**n))
    print(ans)
