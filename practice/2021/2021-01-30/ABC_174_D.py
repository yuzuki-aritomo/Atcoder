import io
import sys
_INPUT = """\
8
WRWWRWRR
"""
sys.stdin = io.StringIO(_INPUT)

from collections import Counter

N = int(input())
A = input()

cnt = Counter(A)
W = cnt["W"]
R = cnt["R"]

a = Counter(A[:cnt["R"]])
print(a["W"])
