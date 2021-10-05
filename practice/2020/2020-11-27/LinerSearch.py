import io
import sys

_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)

def main():

    n = int(input())
    S = list(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))

    ans = 0
    S.sort()
    tmp = "a"
    for t in T:
        for s in S:
            if(tmp==s):
                continue
            if(t==s):
                ans += 1
            tmp = s
    print(ans)

main()
