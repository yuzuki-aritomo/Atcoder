import io
import sys

_INPUT = """\
13
0 3 1 4 10
1 2 2 3
2 0
3 0
4 3 5 6 7
5 0
6 0
7 2 8 9
8 0
9 0
10 2 11 12
11 0
12 0
"""
sys.stdin = io.StringIO(_INPUT)

def child(i):
    B = []
    i = childLeft[i]
    if(i==-1):
        return B
    else:
        while(siblinRight[i] != -1):
            B.append(i)
            i = siblinRight[i]
        B.append(i)
        return B

def depth(i):
    d = 0
    while(parent[i] != -1):
        i = parent[i]
        d += 1
    return d

n = int(input())

parent = [-1] * n
childLeft = [-1] * n
siblinRight = [-1] * n

for i in range(n):
    A = list(map(int, input().split()))
    for k in range(2,len(A)):
        parent[A[k]] = A[0]
        if(k>2):
            siblinRight[A[k-1]] = A[k]
    if(A[1] != 0):
        childLeft[A[0]] = A[2]

for i in range(n):
    order = "node " + str(i) + ": "
    order += "parent = " + str(parent[i]) + ", "
    order += "depth = " + str(depth(i))  + ", "
    if(parent[i] == -1):
        order += "root, "
    elif(childLeft[i] == -1):
        order += "leaf, "
    else:
        order += "internal node, "
    print(order, end="")
    print(child(i))






