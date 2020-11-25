import io
import sys

_INPUT = """\
\\//
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    A = input()
    Stack = []
    L = []
    n = 0
    su = 0
    for item in A:
        if(item=='\\'):
            Stack.append(n)
        elif(item=="/"):
            if(Stack != []):
                p = Stack.pop()
                a = n - p
                su += a
                while(L and L[-1][0] > p):
                    a += L.pop()[1]
                L.append([p, a])
        n += 1
    print(su)
    print(len(L), *(a for p, a in L))

main()