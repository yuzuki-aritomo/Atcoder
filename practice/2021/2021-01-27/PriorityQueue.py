import io
import sys

_INPUT = """\
insert 8
insert 2
extract
insert 10
extract
insert 11
extract
extract
end
"""
sys.stdin = io.StringIO(_INPUT)

def Insert(key):
    global H
    global A
    H += 1
    A.append(key)
    tmp = H
    while(tmp>1 and A[tmp]>A[tmp//2]):
        A[tmp], A[tmp//2] = A[tmp//2], A[tmp]
        tmp = tmp//2

def maxHeap(i):
    global H
    global A
    left = 2*i
    right = 2*i+1
    if(left<=H and A[left]>A[i]):
        largest = left
    else:
        largest = i
    if(right<=H and A[right]>A[largest]):
        largest = right
    if(i != largest):
        A[i], A[largest] = A[largest], A[i]
        maxHeap(largest)

def heapMaxChange():
    global H
    for i in range(H//2,0,-1):
        maxHeap(i)

def heapMaxPop():
    global H
    global A
    m = A[1]
    if(H>1):
        A[1] = A.pop(H)
    H -= 1
    heapMaxChange()
    return m

H = 0
A = [0]
while(True):
    # print(A)
    command = input()
    if(command == "end"):
        break
    if(command == "extract"):
        print(heapMaxPop())
    if(command[:6] == "insert"):
        c, n = command.split()
        n = int(n)
        Insert(n)