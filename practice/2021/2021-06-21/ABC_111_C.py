import io
import sys
_INPUT = """\
6
4 4 4 4 3 3
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
C = list(map(int,input().split()))
A = []
B = []

for  i in range(N):
  if(i%2==0):
    A.append(C[i])
  else:
    B.append(C[i])

from collections import Counter

CntA = Counter(A)
CntB = Counter(B)

mostA = CntA.most_common()
mostB = CntB.most_common()

mostA.append((0, 0))
mostB.append((0, 0))
# print("mostA:", mostA)
# print("mostB:", mostB)

indA = 0
indB = 0

if(mostA[0][0] != mostB[0][0]):
  indA = mostA[0][0]
  indB = mostB[0][0]
else:
  if(mostA[1][1] > mostB[1][1]):
    indA = mostA[1][0]
    indB = mostB[0][0]
  else:
    indA = mostA[0][0]
    indB = mostB[1][0]

print((N//2 - CntA[indA]) + (N//2 - CntB[indB]))

# print("CntA:", CntA)
# print("CntB:", CntB)