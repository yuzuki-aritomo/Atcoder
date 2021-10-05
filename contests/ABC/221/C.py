import io
import sys
_INPUT = """\
1123445562
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = input()
L = list(N)

L.sort(reverse=True)

a = ""
b = ""
j = 0
for i in range(len(L)):
  if(j%4==0):
    a += L[i]
  elif(j%4==1):
    b += L[i]
  elif(j%4==2):
    b += L[i]
  elif(j%4==3):
    a += L[i]
  j += 1

c = ""
d = ""
j = 0
for i in range(len(L)):
  if(j%2==0):
    c += L[i]
  elif(j%2==1):
    d += L[i]
  j += 1

print(int(c)*int(d))
print(int(a)*int(b))


