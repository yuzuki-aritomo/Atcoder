import io
import sys
_INPUT = """\
10 1 2
"""
sys.stdin = io.StringIO(_INPUT)

X, K, D = map(int, input().split())

if(K*D<=abs(X)):
    print(abs(X)-K*D)
    exit()

if(X==0):
    if(K%2==0):
        print(0)
    else:
        print(abs(D))
    exit()

if(D==0 or K==0):
    print(abs(X))
    exit()

i = abs(X)//D
n = abs(X)%D

if(n<abs(n-D)):
    i += 1
    n = abs(n-D)

if((K-i)%2==0):
    print(abs(n))
else:
    print(abs(D-abs(n)))