import io
import sys

_INPUT = """\
10
red
red
red
!orange
yellow
!blue
cyan
!green
brown
!gray
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    n =  int(input())
    A = set()
    Q = set()
    for i in range(n):
        w = input()
        if(w[0]=="!"):
            Q.add(w)
            w = w[1:]
            if w in A:
                print(w)
                return
        else:
            A.add(w)
            w = "!" + w
            if w in Q:
                print(w[1:])
                return
    print("satisfiable")
main()