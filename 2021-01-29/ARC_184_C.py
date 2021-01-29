import io
import sys
_INPUT = """\
1 1
1 1
"""
sys.stdin = io.StringIO(_INPUT)

r_1, c_1 = map(int, input().split())
r_2, c_2 = map(int, input().split())

x, y = abs(r_2-r_1), abs(c_2-c_1)
# print(x,y)
if(x==0 and y==0):
    print(0)
elif(x==y or x+y<4):
    print(1)
elif((x+y)%2==0 or x+y<7 or abs(x-y)<4):
    print(2)
else:
    print(3)
