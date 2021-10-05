import io
import sys

_INPUT = """\
5
1 2
2 3
2 4
4 5
4
1 1 1
1 4 10
2 1 100
2 2 1000
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = dict()
B = dict()
C = dict()
ans = [0] * n
for i in range(n):
    a, b = map(int,input().split())
    if a not in A:
        A[a] = []
        C[a] = []
    A[a].append(b)
    C[a].append(b)
    if b not in B:
        A[b] = []
        C[b] = []
    A[b].append(a)
    C[b].append(a)

m = int(input())

for i in range(m):
    t,k,v = map(int,input().split())
    if(t==1):
        a_b = A[k].copy()
        ans[k] += v
        b_a = B[k].copy()
        

def check(b_a,a_b):
    for item in b_a:
        v = C[item]
