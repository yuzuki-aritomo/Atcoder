import io
import sys
_INPUT = """\
3 3
1 2
2 3
3 1
"""
sys.stdin = io.StringIO(_INPUT)

n, M = map(int, input().split())

class Node:
    Child = set()
    def __init__(self, i):
        self.id = i

N = [0]
for i in range(1, n+1):
    N.append(Node(i))

for i in range(M):
    a, b = map(int, input().split())
    N[a].Child.add(b)
    N[b].Child.add(a)

for i in range(1, n+1):
    if(len(N[i].Child) >= 3):
        print(0)
        exit()

color = [0 for i in range(n+1)]
Ans = 0
def dfs(node, C, parent):
    global Ans
    color[node] = 1
    if(len(N[node].Child) == 1 and parent != 0):
        Ans += 1
        return
    for child in N[node].Child:
        if(color[child] != 1):
            break
    if(C == 0):
        for child in N[node].Child:
            if(child != parent):
                dfs(child, 1, node)
                dfs(child, 2, node)
    if(C == 1):
        for child in N[node].Child:
            if(child != parent):
                dfs(child, 0, node)
                dfs(child, 2, node)
    if(C == 2):
        for child in N[node].Child:
            if(child != parent):
                dfs(child, 0, node)
                dfs(child, 1, node)

dfs(1, 0, 0)
print(Ans)




print(N[a].Child)