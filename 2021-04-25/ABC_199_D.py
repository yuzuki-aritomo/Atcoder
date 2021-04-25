import io
import sys
_INPUT = """\
3 3
1 2
2 3
3 1
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
class Node:
    def __init__(self, id):
        self.id = id
        self.Child = set()
G = []
for i in range(N+1):
    G.append(Node(i))
for i in range(M):
    a, b = map(int, input().split())
    G[a].Child.add(b)
    G[b].Child.add(a)



print(G[1].Child)
print(G[2].Child)
print(G[3].Child)