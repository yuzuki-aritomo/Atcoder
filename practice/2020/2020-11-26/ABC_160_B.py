import io
import sys

_INPUT = """\
1000000000
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = int(input())
    happy = 0
    happy = (n//500) *1000
    happy += (n%500)//5 * 5
    print(happy)
main()

