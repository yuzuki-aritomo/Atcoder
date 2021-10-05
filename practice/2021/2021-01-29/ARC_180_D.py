import io
import sys
_INPUT = """\
1 4 2 2
"""
sys.stdin = io.StringIO(_INPUT)

X, Y, A, B = map(int, input().split())

ans = 0

i = 0
while(True):
    if(X+B<X*A**i or X*A**i>Y):
        ans = i-1
        X = X*A**ans
        break
    i += 1

i = 0
a = Y - X
if(a%B==0):
    ans += a//B - 1
else:
    ans += a//B

print(ans)