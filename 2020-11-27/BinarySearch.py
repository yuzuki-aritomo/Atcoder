import io
import sys

_INPUT = """\
5
1 1 2 2 3
2
1 2
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    ans = 0
    for item in T:
        if(binarySearch(S,item)):
            ans += 1
    print(ans)

def binarySearch(A,key):
    left = 0
    right = len(A)
    while(left<right):
        mid = (left + right) // 2
        if(A[mid] == key):
            return True
        elif(key<A[mid]):
            right = mid
        else:
            left = mid + 1
    return False

main()