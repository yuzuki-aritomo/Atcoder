import io
import sys
_INPUT = """\
6174 100000
"""
sys.stdin = io.StringIO(_INPUT)

from functools import reduce
import sys
sys.setrecursionlimit(10000000)

N, K = map(int, input().split())

loop = 0
def calc(x):
    global loop
    loop += 1
    x_small = int(''.join(sorted(str(x))))
    x_big = int(''.join(sorted(str(x))[::-1]))
    return x_big - x_small
for i in range(K):
    N = calc(N)
print(N)
