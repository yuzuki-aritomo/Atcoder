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

def depth(i):
    d = 0
    global depth_max
    while(parent[i] != -1):
        i = parent[i]
        d += 1
    return d

def sibling(i):
    p = parent[i]
    l = child_left[p]
    r = child_right[p]
    if(i==l):
        return str(r)
    elif(i==r):
        return str(l)
    else:
        return str(-1)

def degree(i):
    l = child_left[i]
    r = child_right[i]
    if(l==-1 and r==-1):
        return "0"
    elif(l != -1 and r != -1):
        return "0"
    else:
        return "1"


def height(i):
    global h1
    global h2
    h1 = 0
    h2 = 0
    if(child_left[i] != -1):
        h1 = height(child_left[i]) + 1
    if(child_right[i] != -1):
        h2 = height(child_right[i]) + 1
    return max(h1,h2)



n = int(input())
parent = [-1] * n
child_left = [-1] * n
child_right = [-1] * n

for i in range(n):
    node, left, right = map(int, input().split())
    child_left[node] = left
    child_right[node] = right
    if(left != -1):
        parent[left] = node
    if(right != -1):
        parent[right] = node

for i in range(n):
    order = "node " + str(i) + ": "
    order += "parent = " + str(parent[i]) + ", "
    order += "sibling = " + sibling(i) + ", "
    order += "degree = " + degree(i) + ", "
    order += "depth = " + str(depth(i))  + ", "
    height(i)
    order += "height = " + str(max(h1,h2))  + ", "
    if(parent[i] == -1):
        order += "root"
    elif(child_left[i] == -1 and child_right[i] == -1):
        order += "leaf"
    else:
        order += "internal node"
    print(order)
