import io
import sys
_INPUT = """\
5 7 20
2 7 8
2 6 4
4 1 9
1 5 4
2 2 7
5 5 2
1 7 2
4 6 6
1 4 1
2 1 10
5 6 9
5 3 3
3 7 9
3 6 3
4 3 4
3 3 10
4 2 1
3 5 4
1 2 6
4 7 9
"""
sys.stdin = io.StringIO(_INPUT)

H, W, N = map(int, input().split())
M = [[0 for i in range(W)] for i in range(H)]
order = []
for _ in range(N):
  tmp = list(map(int, input().split()))
  order.append(tmp)
  M[tmp[0]-1][tmp[1]-1] = tmp[2]

# print(M)

A = []
for i in range(H):
  for j in range(W):
    A.append((M[i][j],i,j))
A.sort(reverse=True)
h = [0 for _ in range(H)]
w = [0 for _ in range(W)]

ans = [[0 for i in range(W)] for i in range(H)]
id = -1
while id<=len(A)-2:
  tmp = []
  while True:
    id += 1
    ans[A[id][1]][A[id][2]] = max(h[A[id][1]], w[A[id][2]])
    tmp.append(id)
    if (id>=len(A)-1 or A[id+1][0] != A[id][0]):
      break

  while len(tmp)>0:
    d = tmp.pop()
    # u, i, j = u[0], u[1], u[2]
    # ans[i][j] = max(h[i], w[j])
    h[A[d][1]] = max(h[A[d][1]], ans[A[d][1]][A[d][2]]+1)
    w[A[d][2]] = max(w[A[d][2]], ans[A[d][1]][A[d][2]]+1)
    # print(u, i, j)
    # print(h)
    # print(w)
    # print(ans)

# print(ans)
for item in order:
  print(ans[item[0]-1][item[1]-1])
