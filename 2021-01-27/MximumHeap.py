import io
import sys

_INPUT = """\
10
4 1 3 2 16 9 10 14 8 7
"""
sys.stdin = io.StringIO(_INPUT)


def maxHeap(i):
    left = 2*i
    right = 2*i+1
    if(left<=H and A[left]>A[i]):
        largest = left
    else:
        largest = i
    if(right<=H and A[right]>A[largest]):
        largest = right
    if(i != largest):
        A[i], A[largest] = A[largest], A[i]
        maxHeap(largest)

H = int(input())
A = list(map(int, input().split()))
A.insert(0,0)
for i in range(H//2,0,-1):
    maxHeap(i)
for i in range(H+1):
    if(i==0):
        continue
    print(" {0}".format(A[i]),end="")
print()