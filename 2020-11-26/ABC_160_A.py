import io
import sys

_INPUT = """\
coffee
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = input()
    a = 0
    if(len(n)>5):
        if(n[2] == n[3]):
            if(n[4] == n[5]):
                print("Yes")
                a = 1
    if(a==0):
        print("No")
main()