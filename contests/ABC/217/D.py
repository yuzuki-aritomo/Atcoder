import io
import sys
_INPUT = """\
100 10
1 31
2 41
1 59
2 26
1 53
2 58
1 97
2 93
1 23
2 84
"""
sys.stdin = io.StringIO(_INPUT)

L, Q = map(int, input().split())


#  N,Q = map(int,input().split())
par = [-1]*(L+1)
def find(x):
  if par[x] < 0:
    return x
  else:
    par[x] = find(par[x]) #経路圧縮
    return par[x]
def same(x,y):
  return find(x) == find(y)
def unite(x,y):
  x = find(x)
  y = find(y)
  if x == y:
    return 0
  else:
    if par[x] > par[y]:
      x,y = y,x
      par[x] += par[y]
      par[y] = x
def size(x):
  return -par[find(x)]



# A = [0, L]#切れ目

# import bisect

# for i in range(Q):
#   a, b = map(int,input().split())
#   if(a == 1):
#     bisect.insort_left(A, b)
#   else:
#     id = bisect.bisect_left(A, b)
#     print(A[id] - A[id-1])
#   # print(A)
