import io
import sys
_INPUT = """\
5 896 483
228 59
529 310
339 60
78 266
659 391
"""
sys.stdin = io.StringIO(_INPUT)

N, D, H = map(int, input().split())

X = 0.0
for i in range(N):
    d, h  = map(int, input().split())
    y = (H*d-h*D)/(h-H)
    x = (h*y)/(d+y)
    X = max(X, x)
print(X)

