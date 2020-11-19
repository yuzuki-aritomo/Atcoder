import io
import sys
_INPUT = """\
6
5 2 4 6 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
nums = [int(i) for i in input().split()]

def selecrionSort(A, n):
    m = 0
    for i in range(n):
        minj = i
        for j in range(i,n):
            if(A[j] < A[minj]):
                minj = j
        tmp = A[i]
        A[i] = A[minj]
        A[minj] = tmp
        if(i != minj):
            m += 1
    print(" ".join(map(str, A)))
    print(m)

selecrionSort(nums, n)