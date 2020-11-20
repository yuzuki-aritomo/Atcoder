import io
import sys

_INPUT = """\
5
5
1
4
3
2
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = []
for i in range(n):
    A.append(int(input()))

def insertionSort(A, n, g):
    global cnt
    for i in range(g, n):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            cnt += 1
        A[j+g] = v

cnt = 0
G = [int(pow(4, i) + 3*pow(2, i-1) + 1) for i in range(10)[::-1]] + [1]
G = [v for v in G if v <= n]
m = len(G)
for i in range(m):
    insertionSort(A, n, G[i])
print(m)
print(*G)
print(cnt)
print(*A, sep='\n')

