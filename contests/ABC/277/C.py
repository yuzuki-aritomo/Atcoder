import io
import sys
_INPUT = """\
3
500000000 600000000
600000000 700000000
700000000 800000000
"""
sys.stdin = io.StringIO(_INPUT)

import sys
sys.setrecursionlimit(1000*1000)

n = int(input())
L = {}
S = set()
for i in range(n):
  a, b = map(int, input().split())
  if a in L:
    L[a].append(b)
  else:
    L[a] = [b]
  if b in L:
    L[b].append(a)
  else:
    L[b] = [a]

def dfs(i):
  if i in S:
    return
  S.add(i)
  if i in L:
    for j in L[i]:
      dfs(j)

dfs(1)
print(max(S))
