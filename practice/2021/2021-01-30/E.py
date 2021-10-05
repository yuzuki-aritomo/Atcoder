import io
import sys
_INPUT = """\
4 3
1 4
2 4
3 4
3
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

class Node():
    def __init__(self, key):
        self.key = key
        self.link = []

N, M = map(int, input().split())
A = [Node(0)]
for i in range(1,N+1):
    A.append(Node(i))
for i in range(M):
    a,b = map(int, input().split())
    A[a].link.append(b)
    A[b].link.append(a)

K = int(input())
C = list(map(int,input().split()))

i = 0
Flag = False
def search(u):
    global i
    global Flag
    print(i)
    print(len(C))
    if(len(C)==i):
        Flag = True
        return
    for item in A[u].link:
        print("item:", item)
        if(C[i+1] == item):
            i += 1
            search(item)

search(1)
print(Flag)