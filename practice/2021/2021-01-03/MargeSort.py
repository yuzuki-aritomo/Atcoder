import io
import sys

_INPUT = """\
10
8 5 9 2 6 3 7 1 10 4
"""
sys.stdin = io.StringIO(_INPUT)

def main():
    n = int(input())
    A = list(map(int,input().split()))

def mergeSort(A, left, right):
    if(left+1 < right):
        mid = (left + right) /2
        mergeSort(A, left, mid)
        mergeSort(A, mid, right)
        merge()

def merge(A, left, mid, right):
    



