import io
import sys
_INPUT = """\
4 3
1 4
1 3
2 3
2 10
1 100
3 1
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)
# sys.setrecursionlimit(100)

N, Q = map(int, input().split())
Child = [[] for i in range(N+1)]
Score = [0 for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    Child[a].append(b)
    Child[b].append(a)

for i in range(Q):
    a, b = map(int, input().split())
    Score[a] += b

Ans = [0 for i in range(N+1)]

#print("Child:", Child)
#print("Score:", Score)

def dps(id, plus, preId):
    for item in Child[id]:
        if(preId != item):
            #print("id:", id)
            #print("item:", item)
            dps(item, plus + Score[item], id)
    Ans[id] += plus

dps(1, Score[1], 1)

#print("Ans:", Ans)

for i in range(1,N+1):
    print(Ans[i], end=" ")
print()