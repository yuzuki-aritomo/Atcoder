import io
import sys

_INPUT = """\
6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288
"""
sys.stdin = io.StringIO(_INPUT)

import bisect

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

A.sort()
C.sort()

def Search(D, i):
    left = 0
    right = len(D)-1
    while (left<=right):
        mid = (left + right) // 2
        if(A[mid]==i):
            return mid
        elif(D[mid]<i):
            left = mid + 1
        elif(D[mid]>i):
            right = mid - 1
    return None

ans = 0
for item_B in B:
    a = bisect.bisect_left(A,item_B)
    c = len(C) - bisect.bisect_right(C,item_B)
    ans += a*c
print(ans)