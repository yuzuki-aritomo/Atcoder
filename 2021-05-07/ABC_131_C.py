import io
import sys
_INPUT = """\
10 40 6 8
"""
sys.stdin = io.StringIO(_INPUT)

A, B, C, D = map(int, input().split())

if(A%C == 0):
    Cn = A//C  - 1
else:
    Cn = A//C
Cm = B//C + 1
a = max(Cm - Cn - 1, 0)
print("a:", a)

if(A%D == 0):
    Dn = A//D  - 1
else:
    Dn = A//D
Dm = B//D + 1
b = max(Dm - Dn - 1, 0)
print("b:", b)

if(A%(C*D) == 0):
    CDn = A//(C*D)  - 1
else:
    CDn = A//(C*D)
CDm = B//(C*D) + 1
c = max(CDm - CDn - 1, 0)
print("c:", c)

print(B - A + 1 - (a+b-c))
