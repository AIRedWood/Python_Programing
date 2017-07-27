#! /usr/bin/env python
# -*- coding: utf-8 -*-

'''
算法描述：
    1，辗转相除法获得最大公约数
    2，最小公倍数 = A * B / 最大公约数
'''

#input
NumA = int(input())
NumB = int(input())
A = NumA
B = NumB

#swap
if A < B:
    (A,B) = (B,A)

# The greatest common divisor
while A % B != 0:
    C = A % B
    A = B
    B = C
gcd = B

#The least common multiple
lcm = int(NumA * NumB / gcd)
print(lcm)