import io
import sys
_INPUT = """\
4 3
1 2
2 3
2 4
2 10
1 100
3 1
"""
sys.stdin = io.StringIO(_INPUT)


class Node:
    def __init__(self,key):
        self.key = key
        self.plus = 0
        self.children = []
        self.count = 0

N, Q = map(int, input().split())
A = [Node(0)]
for i in range(1, N+1):
    A.append(Node(i))
for i in range(1, N):
    a, b = map(int, input().split())
    A[a].children.append(b)
for i in range(Q):
    p, x = map(int, input().split())
    A[p].plus += x

def plusCount(i, n):
    for item in A[i].children:
        A[item].count += n + A[item].plus
        # print("item:", item)
        plusCount(item, A[item].count)

plusCount(1,A[1].plus)
A[1].count = A[1].plus

for i in range(1,N+1):
    print(A[i].count)
