import io
import sys

_INPUT = """\
7
3
2
4
1
5
3
6
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

ans = nums[n-1] - nums[n-2]
b = 0
check = False
for i in range(1,n-1):
    a = nums[n-i] - nums[n-i-1]
    if(a>=0):
        if(check == False):
            b = 0
        b += a
        check = True
    elif(a<0):
        if(check):
            b = 0
        else:
            b = a
    if(ans<b):
        ans = b

print(ans)



