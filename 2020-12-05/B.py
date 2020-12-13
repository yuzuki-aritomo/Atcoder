import io
import sys

_INPUT = """\
22
1011011011011011011011
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
num = input()

if(n>4):
    if(num[0:3]=="011"):
        n += 1
    elif(num[0:3]=="111"):
        n += 2
    elif(num[0:3]=="110"):
        n += 3

    if(num[-3:]=="101"):
        n += 1
    elif(num[-3:]=="110"):
        n += 2
    elif(num[-3:]=="111"):
        n += 3
    print(10000000000000//n)
