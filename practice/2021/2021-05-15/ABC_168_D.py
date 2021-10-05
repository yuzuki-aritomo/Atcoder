import io
import sys
_INPUT = """\
6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6
"""
sys.stdin = io.StringIO(_INPUT)

N,M = map(int, input().split())

class Node:
    def __init__(self, n):
        self.id = n
    load = []

R = [Node(i) for i in range(N+1)]
for i in range(N):
    a, b = map(int, input().split())
    R[a].load.append(b)
    R[b].load.append(a)

from collections import deque
Q = deque()
Q.append(1)
color = [0 for _ in range(N+1)]
path = [0 for _ in range(N+1)]
while(len(Q)!=0):
    n = Q.popleft()
    color[n] = 1
    for item in R[n].load:
        if(color[item] == 0):
            path[item] = n
            Q.append(item)

print(path)
print("Yes")
for i in range(2, len(path)):
    print(path[i])


