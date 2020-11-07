import io
import sys

_INPUT = """\
5 5
3 4
"""
sys.stdin = io.StringIO(_INPUT)

word = input().split()

a = word[1].upper()

if(a == word[0]):
    print("Yes")
else:
    print("No")