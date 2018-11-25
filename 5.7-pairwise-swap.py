'''
I had to look at hint #145 to figure out the answer
'''
n=int(input(),2)
odd_bits=n&0x55555555
even_bits=n&0xaaaaaaaa
ans=(0|(odd_bits<<1))|((even_bits>>1))
print(bin(ans)[2:])
