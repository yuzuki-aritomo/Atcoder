import io
import sys

_INPUT = """\
13
insert AAA
insert AAC
insert AGA
insert AGG
insert TTT
find AAA
find CCC
find CCC
insert CCC
find CCC
insert T
find TTT
find T
"""
sys.stdin = io.StringIO(_INPUT)

if __name__ == "__main__":
    n = int(input())
    A = set()
    for i in range(n):
        cmd, word = map(str, input().split())
        if(cmd=="insert"):
            A.add(word)
        else:
            if word in A:
                print("yes")
            else:
                print("no")
