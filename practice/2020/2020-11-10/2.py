import io
import sys

_INPUT = """\
147 105
"""
sys.stdin = io.StringIO(_INPUT)

a, b = map(int, input().split())

print(a,b)

def gcd(a, b):
    n = a%b
    if(n != 0):
        gcd(b, n)
    return n

# def gcd(a, b):
#     if(a<b):
#         tmp = a
#         a = b
#         b = tmp
#     while(b>0):
#         r = a%b
#         a = b
#         b = r
#     return a

print(gcd(a,b))
