import io
import sys

_INPUT = """\
16
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
"""
sys.stdin = io.StringIO(_INPUT)

import math

def isprime(x):
    if(x == 2):
        return True
    elif( (x<2) or (x%2==0) ):
        return False
    
    i = 3
    rootx = int(math.sqrt(x))
    while( i <= rootx ):
        if( x%i == 0):
            return False
        i += 2
    return True

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

m = 0
for item in nums:
    if(isprime(item)):
        m += 1
print(m)