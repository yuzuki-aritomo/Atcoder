import io
import sys

_INPUT = """\
1000000000000 1
"""
sys.stdin = io.StringIO(_INPUT)

s,p = map(int, input().split())

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

def is_sum(P,s):
    n = len(P)
    for i in range(n):
        for j in range(i+1,n):
            if(P[i]+P[j] == s):
                return True
    if(n%2 == 1):
        m = P[n//2]
        if(m*2 == s):
            return True
    return False

p_div = make_divisors(p)
if(is_sum(p_div,s)==True):
    print("Yes")
else:
    print("No")
