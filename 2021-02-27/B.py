import io
import sys
_INPUT = """\
10
158260522 877914575 602436426
24979445 861648772 623690081
433933447 476190629 262703497
211047202 971407775 628894325
731963982 822804784 450968417
430302156 982631932 161735902
880895728 923078537 707723857
189330739 910286918 802329211
404539679 303238506 317063340
492686568 773361868 125660016
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())

B = []
Flag = False
for i in range(N):
    A = list(map(int,input().split()))
    if(A[0]<A[2]):
        Flag = True
        B.append(A[1])
if(Flag):
    print(min(B))
else:
    print(-1)