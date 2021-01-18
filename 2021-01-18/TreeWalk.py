import io
import sys

_INPUT = """\
9
0 1 4
1 2 3
2 -1 -1
3 -1 -1
4 5 8
5 6 7
6 -1 -1
7 -1 -1
8 -1 -1
"""
sys.stdin = io.StringIO(_INPUT)

import sys

class Node:
    def __init__(self,node,left,right):
        self.node = node
        self.left = left
        self.right = right

def preParse(u):
    if(u==-1):
        return
    print(" %d"%(u),end="")
    preParse(Tree[u].left)
    preParse(Tree[u].right)

def inParse(u):
    if(u==-1):
        return
    inParse(Tree[u].left)
    print(" %d"%(u),end="")
    # print(" {0}".format(u),end="")
    inParse(Tree[u].right)

def postPerse(u):
    if(u==-1):
        return
    postPerse(Tree[u].left)
    postPerse(Tree[u].right)
    print(" %d"%(u),end = "")
    # print(" {0}".format(u),end="")

n = int(input())
Tree = []
for i in range(n):
    node, left, right = map(int, input().split())
    Tree.append(Node(node, left, right))

print("Preorder")
preParse(0)
print()

print("Inorder")
inParse(0)
print()

print("Postorder")
postPerse(0)
print()