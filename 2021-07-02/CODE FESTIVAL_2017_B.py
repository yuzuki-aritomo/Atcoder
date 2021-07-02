import io
import sys
_INPUT = """\
babacccabab

"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

S = list(input())
Cnt = Counter(S)

if(len(Cnt) == 1):
  for item in Cnt:
    if(Cnt[item] == 1):
      print("YES")
    else:
      print("NO")
elif(len(Cnt) == 2):
  A = []
  for item in Cnt:
    A.append(Cnt[item])
  if(A[0] == 1 and A[1]==1):
    print("YES")
  else:
    print("NO")
else:
  a = Cnt["a"]
  b = Cnt["b"]
  c = Cnt["c"]
  m = max(a, b, c)
  if(m-a<2 and m-b<2 and m-c<2):
    print("YES")
  else:
    print("NO")
