import io
import sys
_INPUT = """\
3
0 0
0 1
1 0
2 0
3 0
3 1
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

S = []
T = []
sumX_S = 0
sumY_S = 0
sumX_T = 0
sumY_T = 0
for i in range(N):
  x, y = map(int,input().split())
  sumX_S += x
  sumY_S += y
  S.append([x, y])
for i in range(N):
  x, y = map(int,input().split())
  sumX_T += x
  sumY_T += y
  T.append([x, y])

x = sumX_S/N
y = sumY_S/N
for i in range(N):
  S[i][0] -= x
  S[i][1] -= y
x = sumX_T/N
y = sumY_T/N
for i in range(N):
  T[i][0] -= x
  T[i][1] -= y

maxS = 0
maxT = 0
for i in range(N):
  if(S[i][0]**2 + S[i][1]**2 > maxS):
    maxS = S[i][0]**2 + S[i][1]**2
    indS = i
  if(T[i][0]**2 + T[i][1]**2 > maxT):
    maxT = T[i][0]**2 + T[i][1]**2
    indT = i

print(indS)
print(indT)
print(S)
print(T)

import math
import numpy as np
mS = []
mT = []
# tmpA = np.arctan2(S[-1][1], S[-1][0])
# tmpB = np.arctan2(T[-1][1], T[-1][0])
for i in range(N):
  # # mS.append()
  # math.acos(S[i][0]/ ((S[i][0]**2 + S[i][1]**2)**(0.5)))
  a = np.degrees(np.arctan2(S[i][1], S[i][0]))
  b = np.degrees(np.arctan2(T[i][1], T[i][0]))
  mS.append(a)
  mT.append(b)
  # tmpA = a
  # tmpB = b
mS.sort()
mT.sort()
nS = []
nT = []
print("ms")
print(mS)
print(mT)

#sort rが正しいか
S.sort(key=lambda x: x[0]**2 + x[1]**2)
T.sort(key=lambda x: x[0]**2 + x[1]**2)

for i in range(N):
  if(round(S[i][0]**2 + S[i][1]**2, 12) == round(T[i][0]**2 + T[i][1]**2, 12)):
    continue
  else:
    print("No")
    # exit()

# tmp = S[i][0]**2 + S[i][1]**2
# for i in range(N):
#   if(tmp == S[i][0]**2 + S[i][1]**2):
#     C = i

# CheckS = S[0:C]
# CheckT = T[0:C]


a = math.acos(S[0][0]/ ((S[0][0]**2 + S[0][1]**2)**(0.5)))
b = math.asin(S[0][1]/ ((S[0][0]**2 + S[0][1]**2)**(0.5)))
print(a)
print(b+math.pi)