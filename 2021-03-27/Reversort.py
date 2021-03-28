import io
import sys
_INPUT = """\
3
4
4 2 1 3
2
1 2
7
7 6 5 4 3 2 1
"""
sys.stdin = io.StringIO(_INPUT)

def Reversort(A):
    ans = 0
    for i in range(len(A)-1):
        j = A.index(min(A[i:]))
        tmp = A[i:j+1]
        for k in range(i, j+1):
            A[k] = tmp.pop()
        ans += j-i+1
    return ans

def main():
    N = int(input())
    for i in range(N):
        ans = 0
        M = int(input())
        A = list(map(int,input().split()))
        ans = Reversort(A)
        print('Case #{}: {}'.format(i+1, ans))
main()