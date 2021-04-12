import io
import sys
_INPUT = """\
a
"""
sys.stdin = io.StringIO(_INPUT)

word = input()

for i in range(len(word)):
    if(i%2==0  and word[i].islower()):
        continue
    elif(i%2==1  and not(word[i].islower())):
        continue
    else:
        print("No")
        exit()
print("Yes")
