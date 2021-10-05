import io
import sys
_INPUT = """\
6 12
2 3
4 6
1 2
4 5
2 6
1 5
4 5
1 3
1 2
2 6
2 3
2 5
5
3 5
1 4
2 6
4 6
5 6
"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(M):
    A.append(list(map(int,input().split())))
K = int(input())
B = []
for i in range(K):
    B.append(list(map(int,input().split())))

Ans = 0
Ball = [0 for i in range(K)]
Ball = set()
for bit in range(1<<K):
    Ball.clear()
    for i in range(K):
        if((bit>>i)&1):
            #1の時の処理
            Ball.add(B[i][1])
        else:
            Ball.add(B[i][0])

    ans = 0
    for item in A:
        if item[0] in Ball:
            if item[1] in Ball:
                ans += 1
    Ans = max(Ans, ans)
print(Ans)