import io
import sys

_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)


n = int(input())

def check7(word):
    num_str = str(word) 
    for i in range(len(num_str)):
        if(num_str[i]=="7"):
            return True
    num_s = oct(word)
    num_8 = str(num_s)
    for i in range(len(num_8)):
        if(num_8[i]=="7"):
            return True
    return False


def main():
    a = 0
    for i in range(1,n+1):
        if(check7(i)):
            a += 1
    print(n-a)

main()

