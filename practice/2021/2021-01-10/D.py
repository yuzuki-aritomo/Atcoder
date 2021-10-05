
import io
import sys

_INPUT = """\
5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409
"""
sys.stdin = io.StringIO(_INPUT)

N, C = map(int,input().split())

A = []
for i in range(N):
    s, g, p =  list(map(int, input().split()))
    A.append([s,p])
    A.append([g+1,0-p])

A.sort()

ans = 0
now_p = 0

for i in range(len(A)-1):
    now_p += A[i][1] 
    if(now_p>C):
        ans += C*(A[i+1][0]-A[i][0])
    else:
        ans += now_p*(A[i+1][0]-A[i][0])

print(ans)






# for i in range(len(A)):
#     if(A[i][1]==-1):
#         now_p += A[i][2] 
#         if(A[i+1][1] == 1):

#         if(now_p>C):
#             ans += C*(A[i+1][0]-A[i][0])
#         else:
#             ans += now_p*(A[i+1][0]-A[i][0])
        
#         if(A[i+1][0]==A[i][0] and A[i][1]==-1 and A[i+1][1]==0):
#             if(now_p>C):
#                 ans += C
#             else:
#                 ans += now_p
        
#     if(A[i][1]==0):
#         now_p -= A[i][2]
#         if(i != len(A)-1):
#             if(now_p>C and (A[i+1][0]-A[i][0]) != 0):
#                 ans += C*(A[i+1][0]-A[i][0]-1)
#             elif((A[i+1][0]-A[i][0]) != 0):
#                 ans += now_p*(A[i+1][0]-A[i][0]-1)

