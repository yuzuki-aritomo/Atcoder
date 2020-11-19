import io
import sys

_INPUT = """\
6
5 2 4 6 1 3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
card = list(map(int,input().split()))


def sort(n, card):
    for i in range(n):
        a = card[i]
        b = i - 1
        while(b>=0 and card[b]>a):
            card[b+1]  = card[b]
            b -= 1
        card[b+1]  = a
        
        word = ""
        for i in range(n):
            word += str(card[i])
            word += " "
        print(word[:-1])

sort(n, card)



