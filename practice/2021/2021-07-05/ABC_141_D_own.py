import io
import sys
_INPUT = """\
10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
"""
sys.stdin = io.StringIO(_INPUT)

A = []
def insert(k):
  A.append(k)
  h = len(A)-1
  while(h>0):
    if(A[(h-1)//2] < A[h]):
      A[(h-1)//2], A[h] = A[h], A[(h-1)//2]
      h = (h-1)//2
    else:
      break
  return

def extract():
  ans = A[0]
  A[0] = A[-1]
  A.pop()
  h = 0
  while(h*2+1 < len(A)):
    n = h*2+1
    m = min(h*2+2, len(A)-1)
    if(A[h] < A[n] or A[h] < A[m]):
      if(A[n] < A[m]):
        A[h], A[m] = A[m], A[h]
        h = m
      else:
        A[h], A[n] = A[n], A[h]
        h = n
    else:
      break
  return ans


N, M = map(int, input().split())
A = list(map(int,input().split()))
A.sort(reverse=True)
# print(A)
for _ in range(M):
  u = extract()
  u //= 2
  insert(u)
  # print(A)

print(sum(A))