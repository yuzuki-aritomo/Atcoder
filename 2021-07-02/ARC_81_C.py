import io
import sys
_INPUT = """\
10
3 3 3 3 4 4 5 5 5 5
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int,input().split()))

from collections import Counter

Cnt = Counter(A)

H = []
for item in Cnt:
  if(Cnt[item]>3):
    H.append(item)
    H.append(item)
  elif(Cnt[item]>1):
    H.append(item)


if(len(H)<2):
  print(0)
else:
  H.sort(reverse=True)
  print(H[0]*H[1])

