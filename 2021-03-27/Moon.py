import io
import sys
_INPUT = """\
4
2 3 CJ?CC?
4 2 CJCJ
1 3 C?J
2 5 ??J???
"""
sys.stdin = io.StringIO(_INPUT)

def deleteQues(word_bfo):
    word = ''
    for i in range(len(word_bfo)):
        if(i <= (len(word_bfo)-2) and word_bfo[i]=='?' and word_bfo[i+1]=='?'):
            continue
        else:
            word += word_bfo[i]
    return word

def calc(B, x, y):
    ans = 0
    for i in range(len(B)-1):
        if(B[i]=='C' and B[i+1]=='J'):
            ans += x
        if(B[i]=='J' and B[i+1]=='C'):
            ans += y
    return ans

def solve(word, X, Y):
    word = list(word)
    ind=-1
    for item in word:
        ind += 1
        if(item!='?'):
            continue
        if(ind==0):
            if(len(word)==1):
                word[0] = 'C'
            else:
                word[0] = word[1]
        elif(ind == len(word)-1):
            word[ind] = word[ind-1]
        elif(ind==-1):
            break
        else:
            word[ind] = word[ind+1]
    word_str = "".join(word)
    return calc(word_str, X, Y)

def main():
    N = int(input())
    for i in range(N):
        A = list(map(str, input().split()))
        X, Y = int(A[0]), int(A[1])
        word_bfo = A[2]
        word = deleteQues(word_bfo)
        print('Case #{}: {}'.format(i+1, solve(word, X, Y)))

main()