import io
import sys
_INPUT = """\
3 3 4 1
"""
sys.stdin = io.StringIO(_INPUT)

import itertools

H, W, A, B = map(int, input().split())
N = H*W
Map = [i for i in range(N)]

def has_duplicates(seq):
    return len(seq) != len(set(seq))

def solve(items):#[1,3,4]
    global B
    ans = 0
    for bit in range(2**B):
        tmp = []
        for item in items:
            print(item)
            tmp.append([item])
        for i in range(B):
            if(bit>>i&i):
                tmp[i].append(tmp[i]+H)
            else:
                tmp[i].append(tmp[i]+H)
        if(has_duplicates(tmp)):
            ans += 1
    return ans

C = [i for i in range(N)]
Ans = 0
for item in list(itertools.combinations(C, B)):
    Ans += solve(list(item))

print(Ans)