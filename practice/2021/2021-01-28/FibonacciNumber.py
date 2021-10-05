import io
import sys

_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
F = []
def fibonacci(i):
    # print(F)
    if(len(F)>i):
        return F[i]
    if(i==0 or i==1):
        F.append(1)
        return 1
    F.append(fibonacci(i-2) + fibonacci(i-1))
    return F[i]

# print(fibonacci(N))
