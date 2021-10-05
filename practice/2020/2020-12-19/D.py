import io
import sys

_INPUT = """\
5
31 41 59 26 53
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))

def test():
    ans = 0
    for i in range(n):
        for k in range(i,n):
            ans += abs(A[i]-A[k])
    print(ans)

def main():
    ans = 0
    before_sum = 0
    A.sort()
    sum_A = sum(A)
    tmp_sum = A[0] * n 
    ans =+ sum_A - tmp_sum - before_sum
    for i in range(1,n):
        tmp_sum = A[i] * (n-i) 
        before_sum += A[i-1]
        ans += sum_A - tmp_sum - before_sum
        # print("tmp_sum", tmp_sum)
        # print("before_sum",before_sum)
        # print("ans", ans)
    print(ans)

main()

