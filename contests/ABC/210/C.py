import io
import sys
_INPUT = """\
10 6
304621362 506696497 304621362 506696497 834022578 304621362 414720753 304621362 304621362 414720753


"""
sys.stdin = io.StringIO(_INPUT)

N, K = map(int, input().split())
A = list(map(int,input().split()))

from collections import Counter

Cnt = Counter(A[0:K])

Ans = len(Cnt)
for i in range(K, N):
  Cnt[A[i]] += 1
  if(Cnt[A[i-K]] == 1):
    Cnt.pop(A[i-K])
  else:
    Cnt[A[i-K]] -= 1
  Ans = max(Ans, len(Cnt))

print(Ans)
