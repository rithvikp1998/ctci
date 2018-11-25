'''
I had to look this up online :( And I am pretty sure the
code can be cleaner.

http://binary-system.base-conversion.ro/real-number-converted-from-decimal-system-to-32bit-single-precision-IEEE754-binary-floating-point.php

'''

n=float(input())
sign_bit='0'

'''
We have to get enough bits from n such that the normalized
version of it will fill the entire mantissa. There are two
cases:
1. If we encounter a bit '1', we need to get 23 bits after that
2. If we don't encounter '1' bit at all, we still need to count
   127 + 23 bits, 127 for the exponent, 23 for mantissa
'''

found_bit1=0
bit1_index=0
bit_count=0
mantissa=''

while True:
    if found_bit1==1 and bit_count-bit1_index>=23:
        break
    elif found_bit1==0 and bit_count>=150:
        break
    else:
        if found_bit1==1:
            n*=2
            if n>=1:
                n-=1
                mantissa+='1'
                bit_count+=1
                if n==0:
                    break
            else:
                mantissa+='0'
                bit_count+=1
        else:
            n*=2
            if n>=1:
                n-=1
                mantissa+='1'
                bit_count+=1
                found_bit1=1
                bit1_index=bit_count
                if n==0:
                    break
            else:
                mantissa+='0'
                bit_count+=1
if found_bit1==0 or bit1_index>127:
    exponent_value=0
    exponent='00000000'
else:
    exponent_value=127-bit1_index
    exponent=''
    while exponent_value>0:
        exponent=str(exponent_value%2)+exponent  # Or you can use the inbuilt function instead.
        exponent_value//=2
    while len(exponent)<8:
        exponent='0'+exponent

ans=sign_bit+exponent
if found_bit1==1:
    ans+=mantissa[bit1_index:bit1_index+23]
else:
   ans+=mantissa[128:128+23]

if len(ans)==32:
    print('ERROR. Approximate value:', ans)
else:
    while len(ans)<32:
        ans+='0'
    print(ans)
    

