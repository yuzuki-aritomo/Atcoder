import io
import sys
_INPUT = """\
45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir
"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
S = list(input())
Ans = 0

for i in range(1, N):
  A = set(S[0:i])
  B = set(S[i:])
  C = A&B
  Ans = max(len(C), Ans)

print(Ans)


