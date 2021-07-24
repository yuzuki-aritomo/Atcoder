import io
import sys
_INPUT = """\
2B
3B
HR
3B
"""
sys.stdin = io.StringIO(_INPUT)


from collections import Counter

S = []
for i in range(4):
  S.append(input())

Cnt = Counter(S)

if(len(Cnt) == 4):
  print("Yes")
else:
  print("No")