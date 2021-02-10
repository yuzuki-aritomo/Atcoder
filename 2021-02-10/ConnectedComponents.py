import io
import sys
_INPUT = """\
15 15
0 1
0 4
1 4
1 5
4 5
2 3
6 7
6 10
7 10
8 9
12 9
13 12
13 11
13 14
11 14
20
0 1
1 4
1 5
2 3
6 7
7 10
8 9
8 13
14 12
11 9
14 8
0 6
0 2
10 4
8 2
12 6
13 10
10 11
14 1
13 1
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

N, M = map(int, input().split())
A = [[] for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    A[a].append(b)

dq = deque()
Com = int(input())
for i in range(Com):
    color = [0 for i in range(N)]
    Flag = False
    a, b = map(int, input().split())
    for item in A[a]:
        dq.append(item)
    color[a] = 1
    while(len(dq)!=0):
        s = dq.popleft()
        if(s==b):
            Flag = True
            break
        color[s] = 1
        for item in A[s]:
            if(color[item]==0):
                dq.append(item)
    
    for item in A[b]:
        dq.append(item)
    color[b] = 1
    while(len(dq)!=0):
        s = dq.popleft()
        if(s==a):
            Flag = True
            break
        color[s] = 1
        for item in A[s]:
            if(color[item]==0):
                dq.append(item)
    if(Flag):
        print("yes")
    else:
        print("no")


