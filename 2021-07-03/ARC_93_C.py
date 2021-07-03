import io
import sys
_INPUT = """\
6
-679 -2409 -3258 3095 -3291 -4462
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

Ans = 0
A.insert(0, 0)
A.append(0)
for i in range(N+1):
  Ans += abs(A[i] - A[i+1])

# i 番目を除く場合
# i番目を経由 - (i-1)から(i+1 )番目
# abs(A[i-1]- A[i]) + abs(A[i+1] - A[i])) - abs(A[i-1]-A[i+1])
diff = 0
for i in range(1, N+1):
  diff = abs(A[i-1]- A[i]) + abs(A[i] - A[i+1]) - abs(A[i-1]-A[i+1])
  print(Ans - diff)

# print(Ans - diff)