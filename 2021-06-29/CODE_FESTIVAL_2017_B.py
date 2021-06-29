import io
import sys
_INPUT = """\
15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5

"""
sys.stdin = io.StringIO(_INPUT)


N = int(input())
D = list(map(int,input().split()))
M= int(input())
T = list(map(int,input().split()))

from collections import Counter

CntD = Counter(D)
CntT = Counter(T)

for item in CntT:
  if(CntT[item] > CntD[item]):
    print("NO")
    exit()

print("YES")
