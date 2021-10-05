import io
import sys

_INPUT = """\
48
ffoxoxuvgjyzmehmopfohrupffoxoxfofofoxffoxoxejffo
"""
sys.stdin = io.StringIO(_INPUT)


def remo(w):
    global ans
    for item in w:
        if(item=="f" and i<len(w)-2):
            if(w[i+1] == "o"):
                if(w[i+2] == "x"):
                    ans -= 3
        i += 1

k = 0
def rem(w):
    global k
    r = w.replace('fox','')
    k += 1
    if(k<n):
        rem(r)


n = int(input())
w = input()

# f = w.count("f")
# o = w.count("o")
# x = w.count("x")

# m = min(f,o,x)

while:
    w = w.replace('fox','') 
    if("fox" in w):
        continue
    else:
        break
print(len(w))
