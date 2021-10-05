import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = int(input())
    ans = 1
    A = []
    B = []
    for i in range(2, n+1):
        if(ans % i  != 0):
            ans = ans*i
            B.append(i)
            # print(i)
    # for item in B:
    #     if(ans/item %item==0):
    #         ans = ans / item
            # print(item)
    print(int(ans)+1)
main()
