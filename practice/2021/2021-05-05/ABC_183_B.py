import io
import sys
_INPUT = """\
-9 99 -999 9999
"""
sys.stdin = io.StringIO(_INPUT)

SX, SY, GX, GY = map(int, input().split())

# (SX, -SY) , (GX, Gy) この2つが通る直線
#その直線のY=0 のXの値が答え

# (SX, -SY) , (GX, Gy) この2つが通る直線
a = (GY+SY) / (GX-SX)
b = GY - a*GX

# Y = a*X + b
# Y = 0

X = - b/a
print(X)


