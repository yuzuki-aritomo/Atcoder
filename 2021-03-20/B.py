import io
import sys
_INPUT = """\
482054928534958439584392583958239582958734827534827534827583427583475287583475289347528974837258743725874892789574389752894748.3
"""
sys.stdin = io.StringIO(_INPUT)

X = input()

flag = 0
for i in range(len(X), 0, -1):
    if(X[i-1] == "."):
        flag = i
        break
    if(len(X)-i >110):
        flag = 0
        break

if(flag!=0):
    ans = X[:flag-1]
    print(int(ans))
else:
    print(int(X))
