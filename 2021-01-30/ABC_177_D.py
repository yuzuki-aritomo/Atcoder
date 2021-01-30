import io
import sys
_INPUT = """\
0 0
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(500*500)

N, M = map(int, input().split())

if(M==0):
    print(1)
    exit()

class Person:
    def __init__(self, key):
        self.key = key
        self.friends = []

A = [Person(0)]
D = [0 for i in range(N+1)]
for i in range(1,N+1):
    A.append(Person(i))
for i in range(M):
    a, b = map(int, input().split())
    A[a].friends.append(b)
    A[b].friends.append(a)

m = 0
def dps(u):
    global m
    if(D[u]==0):
        D[u] = 1
        for item in A[u].friends:
            dps(item)
        m += 1

a = 0
for i in range(1, N+1):
    m = 0
    if(D[i]==0):
        dps(i)
        a = max(a,m)
        # print("i:", i)
        # print("m:", m)
        # print("a:", a)

print(a)