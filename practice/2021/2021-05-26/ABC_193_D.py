import io
import sys
_INPUT = """\
2
9988#
1122#
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter
from itertools import combinations

K = int(input())
S = input()
T = input()


Cnt = Counter()
Takahashi = Counter()
Aoki = Counter()
for i in range(4):
    Cnt[int(S[i])] += 1
    Cnt[int(T[i])] += 1
    Takahashi[int(S[i])] += 1
    Aoki[int(T[i])] += 1


def solve(card):
    T_tmp = Takahashi.copy()
    A_tmp = Aoki.copy()
    T_tmp[card[0]] += 1
    A_tmp[card[1]] += 1
    T = 0
    A = 0
    for i in range(1, 9):
        T += i* (10**T_tmp[i])
        A += i* (10**A_tmp[i])
    if(T>A):
        return True
    return False


Card = []
for i in range(1, 10):
    if(K - Cnt[i]>=2):
        Card.append(i)
        Card.append(i)
    elif(K - Cnt[i]>=1):
        Card.append(i)

Ans_up = 0
for card in combinations(Card, 2):
    if(card[0] == card[1]):
        if(solve(card)):
            Ans_up += 1
    else:
        if(solve(card)):
            Ans_up += 1
        if(solve(card[::-1])):
            Ans_up += 1

print("len(Card):", len(Card))
print(Card)
print("((9*K-8)*(9*K-9)):", ((9*K-8)*(9*K-9)))
print("Ans_up:", Ans_up)
print(Ans_up/((9*K-8)*(9*K-9)))

