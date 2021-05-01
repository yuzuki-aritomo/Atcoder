import io
import sys
_INPUT = """\
33
"""
sys.stdin = io.StringIO(_INPUT)

X = int(input())
for i in range(120):
    for j in range(-(10**2), 120**2):
        tmp = i**5 - j**5
        if(X == tmp):
            print(i, j)
            exit()

