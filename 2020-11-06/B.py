import io
import sys

_INPUT = """\
10000000000 10000000000
4 3
"""
sys.stdin = io.StringIO(_INPUT)

R, B = map(int,input().split())
X, Y = map(int,input().split())

r_max = int(R//X) +1
b_max = int(B//Y) +1

m = 0
for r in range(0,r_max):
    for b in range(0,b_max):
        if( X*r + b <= R):
            if(r + Y*b <= B):
                if(m < r + b):
                    m = r + b
                    
print(m)