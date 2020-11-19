import io
import sys
_INPUT = """\
5
H4 C9 S4 D2 C3
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
cards_b = input().split()
cards_s = cards_b.copy()

def bubblesort(A, n):
    m = 0
    flag = 1
    while(flag):
        flag = 0
        for j in range(1,n)[::-1]:
            if(int(A[j][1]) < int(A[j-1][1])):
                tmp = A[j]
                A[j] = A[j-1]
                A[j-1] = tmp
                flag = 1
                m += 1
    bouble = " ".join(map(str, A))
    print(bouble)
    print("Stable")
    return bouble

def selecrionSort(A, n, bouble):
    m = 0
    for i in range(n):
        minj = i
        for j in range(i,n):
            if(int(A[j][1]) < int(A[minj][1])):
                minj = j
        tmp = A[i]
        A[i] = A[minj]
        A[minj] = tmp
    selection = " ".join(map(str, A))
    print(selection)
    if(selection == bouble):
        print("Stable")
    else:
        print("Not stable")

bouble = bubblesort(cards_b, n)
selecrionSort(cards_s, n, bouble)
