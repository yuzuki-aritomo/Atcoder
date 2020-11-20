import io
import sys

_INPUT = """\
6
5 2 4 6 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
nums =[int(i) for i in input().split()] 

def bubblesort(A, n):
    m = 0
    flag = 1
    while(flag):
        flag = 0
        for j in range(1,n)[::-1]:
            if(A[j] < A[j-1]):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
                m += 1
    print(" ".join(map(str, A)))
    print(m)

bubblesort(nums, n)
