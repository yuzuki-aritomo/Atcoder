import io
import sys
_INPUT = """\
10
9 4
4 3
1 1
4 2
2 4
5 8
4 0
5 3
0 5
5 2
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int,input().split())))

def IsSqere(A):
    if((A[1][0]-A[0][0]) * (A[2][0]-A[0][0]) + (A[1][1]-A[0][1]) * (A[2][1]-A[0][1]) == 0 ):
        if((A[1][0]-A[3][0]) * (A[2][0]-A[3][0]) + (A[1][1]-A[3][1]) * (A[2][1]-A[3][1]) == 0 ):
            if((A[3][0]-A[1][0]) * (A[0][0]-A[1][0]) + (A[3][1]-A[1][1]) * (A[0][1]-A[1][1]) == 0 ):
                if(abs(A[1][0]-A[0][0])**2 + abs(A[2][0]-A[0][0])**2 == abs(A[1][1]-A[0][1])**2 + abs(A[2][1]-A[0][1])**2):
                    return True
    return False

def solve():
    ans = 0
    tm = 0
    for i in range(N):
        for j in range(i+1 ,N):
            for k in range(j+1,N):
                for l in range(k+1, N):
                    tmp = [A[i], A[j], A[k], A[l]]
                    tmp.sort()
                    if(IsSqere(tmp)):
                        tm = abs(tmp[1][0]-tmp[0][0])**2 + abs(tmp[1][1]-tmp[0][1])**2
                        # print(tmp)
                        # print("tm:", tm)
                        ans = max(ans, tm)
    print(ans)
solve()

# A = [[1,1], [2,4], [4,0], [5,3]]
# A = [[4,2], [4,3], [5,2], [5,3]]
# if((A[1][0]-A[0][0]) * (A[2][0]-A[0][0]) + (A[1][1]-A[0][1]) * (A[2][1]-A[0][1]) == 0 ):
#     if((A[1][0]-A[3][0]) * (A[2][0]-A[3][0]) + (A[1][1]-A[3][1]) * (A[2][1]-A[3][1]) == 0 ):
#         if((A[3][0]-A[1][0]) * (A[0][0]-A[1][0]) + (A[3][1]-A[1][1]) * (A[0][1]-A[1][1]) == 0 ):
#             if(abs(A[1][0]-A[0][0])**2 + abs(A[2][0]-A[0][0])**2 == abs(A[1][1]-A[0][1])**2 + abs(A[2][1]-A[0][1])**2):
#                 print("--")
