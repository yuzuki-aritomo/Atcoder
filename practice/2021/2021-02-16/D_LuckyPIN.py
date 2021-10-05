import io
import sys
_INPUT = """\
19
3141592653589793238
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
S = input()
ans = 0
for i in range(10):
    tmp = S.find(str(i))
    if(tmp == -1 or tmp == N):continue
    for j in range(10):
        T = S[tmp+1:]
        tmp_1 = T.find(str(j))
        if(tmp_1 == -1 or tmp_1>=N):continue
        for k in range(10):
            R = T[tmp_1+1:]
            tmp_2 = R.find(str(k))
            if(tmp_2 != -1 or tmp_2>=N): 
                ans+=1
                # print("i:", i, end="")
                # print("j:", j, end="")
                # print("k:", k, end="")
                # print("tmp:", tmp)
                # print("tmp_1:", tmp_1)
                # print("tmp_2:", tmp_2)
print(ans)