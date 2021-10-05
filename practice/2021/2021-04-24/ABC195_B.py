import io
import sys
_INPUT = """\
300 333 1
"""
sys.stdin = io.StringIO(_INPUT)

import math
A, B, W = map(int, input().split())

up = 1000*W/A
low = 1000*W/B

low = math.ceil(low)
up = math.floor(up)

if(low>up):
    print("UNSATISFIABLE")
    exit()
print(low, up)

