import io
import sys

_INPUT = """\
1 2 + 3 4 - *
"""
sys.stdin = io.StringIO(_INPUT)

A = input().split()
W = []
for item in A:
    if(item=="+"):
        W[-2] = W[-2] + W[-1]
        del W[-1]
    elif(item=="-"):
        W[-2] = W[-2] - W[-1]
        del W[-1]
    elif(item=="*"):
        W[-2] = W[-2] * W[-1]
        del W[-1]
    else:
        W.append(int(item))

print(W[0])



