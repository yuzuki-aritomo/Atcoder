import io
import sys

_INPUT = """\
4 3
2 3 1 5
2 4
1 2
1 3
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int,input().split())
A = list(map(int, input().split()))

class node:
    key = 0
    goto = []
    def __init__(self, key):
        self.key = key

town = []
for i in range(M):
    a, b = map(int,input().split())
    c = node(a)
    c.goto.append(b)
    town.append(c)

print()