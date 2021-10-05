import io
import sys
_INPUT = """\
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 3 ?CJJJ?J?
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

def calc(A, x, y):
    ans = 0
    for i in range(len(A)-1):
        if(A[i]=='C' and A[i+1]=='J'):
            ans += x
        if(A[i]=='J' and A[i+1]=='C'):
            ans += y
    return ans

def solve(word, x, y):
    cnt = Counter(word)
    qes = cnt['?']
    Ans = float('inf')
    for i in range(2**qes):
        tmp = word
        for j in range(qes):
            if(i>>j & 1):
                tmp = tmp.replace('?', 'J')
            else:
                tmp = tmp.replace('?', 'C')
        Ans = min(Ans, calc(tmp, x, y))
    return Ans

def main():
    N = int(input())
    for i in range(N):
        A = list(map(str, input().split()))
        X, Y = int(A[0]), int(A[1])
        word = A[2]
        print("Case #{}: {}".format( i+1, solve(word, X, Y)))

main()