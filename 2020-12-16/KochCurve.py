import io
import sys

_INPUT = """\
0
"""
sys.stdin = io.StringIO(_INPUT)

import math

n = int(input())

def koch(n, p1_x, p1_y, p2_x, p2_y):
    if(n == 0):
        return
    
    s_x = (2 * p1_x + p2_x)/3
    s_y = (2 * p1_y + p2_y)/3
    t_x = (p1_x + 2 * p2_x)/3
    t_y = (p1_y + 2 * p2_y)/3
    u_x = (t_x - s_x)*math.cos(math.radians(60)) - (t_y - s_y)*math.sin(math.radians(60)) + s_x
    u_y = (t_x - s_x)*math.sin(math.radians(60)) + (t_y - s_y)*math.cos(math.radians(60)) + s_y
    
    
    koch(n-1, p1_x,p1_y, s_x, s_y)
    print('{:.08f}'.format(s_x), '{:.08f}'.format(s_y))
    koch(n-1, s_x, s_y, u_x, u_y)
    print('{:.08f}'.format(u_x), '{:.08f}'.format(u_y))
    koch(n-1, u_x, u_y, t_x, t_y)
    print('{:.08f}'.format(t_x), '{:.08f}'.format(t_y))
    koch(n-1, t_x, t_y, p2_x, p2_y)

print('{:.08f}'.format(0), '{:.08f}'.format(0))
koch(n,0,0,100,0)
print('{:.08f}'.format(100), '{:.08f}'.format(0))