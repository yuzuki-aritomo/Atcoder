import io
import sys

_INPUT = """\
5
7 8 1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

class Node():
    def __init__(self,key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0,0)
    B = [0] * (N+1)
    for i in range(1,N+1):
        B[i] = Node(A[i])
        if(i>1):
            B[i].parent = A[i//2]
        if(2*i<=N):
            B[i].left = A[2*i]
        if(2*i+1 <=N):
            B[i].right = A[2*i+1]
    
    for i in range(1,N+1):
        print("node {0}: key = {1}, ".format(i,B[i].key),end="")
        if(B[i].parent != None):
            print("parent key = {0}, ".format(B[i].parent), end="")
        if(B[i].left != None):
            print("left key = {0}, ".format(B[i].left), end="")
        if(B[i].right != None):
            print("right key = {0}, ".format(B[i].right), end="")
        print()
main()