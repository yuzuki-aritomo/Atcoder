import io
import sys
_INPUT = """\
314159265358979323 846264338327950288 419716939 937510582
"""
sys.stdin = io.StringIO(_INPUT)


import numpy
A, B, C, D = map(int, input().split())

if(A%C == 0):
    Cn = A//C  - 1
else:
    Cn = A//C
Cm = B//C + 1
a = max(Cm - Cn - 1, 0)

if(A%D == 0):
    Dn = A//D  - 1
else:
    Dn = A//D
Dm = B//D + 1
b = max(Dm - Dn - 1, 0)

CD = numpy.lcm(C, D)
if(A%(CD) == 0):
    CDn = A//(CD)  - 1
else:
    CDn = A//(CD)
CDm = B//(CD) + 1
c = max(CDm - CDn - 1, 0)

print(B - A + 1 - (a+b-c))
