import io
import sys

_INPUT = """\
10
insert 30
insert 88
insert 12
insert 1
insert 20
find 12
insert 17
insert 25
find 16
print
"""
sys.stdin = io.StringIO(_INPUT)

class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

def PreOrder(T,a):
    if(a==None):
        return
    print(" {0}".format(a), end="")
    PreOrder(T, T[a].left)
    PreOrder(T, T[a].right)

def InOrder(T,a):
    if(a==None):
        return
    InOrder(T, T[a].left)
    print(" {0}".format(a), end="")
    InOrder(T, T[a].right)

def Insert(T, z, FirstNode):
    x = FirstNode
    while(x != None):
        y = x
        # print(x)
        if( z < T[x].key):
            x = T[x].left
        else:
            x = T[x].right
    T[z] = Node(z)
    T[z].parent = y
    if( z < T[y].key):
        T[y].left = z
    else:
        T[y].right = z

def Find(T, FirstNode, v):
    x = FirstNode
    while(x != None and x != v):
        if(x > v):
            x = T[x].left
        else:
            x = T[x].right
    if(x==v):
        return True
    else:
        return False

def main():
    N = int(input())
    T = dict()
    Flag = 0
    FirstNode = -1
    for i in range(N):
        A = input()
        if("insert"==A[:6]):
            A, n = A.split()
            n = int(n)
            if(Flag==0):
                FirstNode = n
                T[n] = Node(n)
                Flag = 1
                continue
            Insert(T,n,FirstNode)
        elif("find" == A[:4]):
            A, n = A.split()
            n = int(n)
            if(Find(T, FirstNode, n)):
                print("Yes")
            else:
                print("No")
        else:
            InOrder(T, FirstNode)
            print()
            PreOrder(T, FirstNode)
            print()

if __name__=="__main__":
    main()
