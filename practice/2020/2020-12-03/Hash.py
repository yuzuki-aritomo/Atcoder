import io
import sys
_INPUT = """\
100
insert T
insert AAA
find T
insert CAC
find A
insert AA
insert CA
insert T
find TAA
find TCG
find C
insert TG
find C
insert G
find A
find AAC
insert TC
insert T
insert AA
find C
insert G
find CTG
find CT
insert TT
find AC
find TTG
find CG
find T
insert TT
find G
insert TCG
insert GGT
find AGC
find T
insert GCT
insert CA
insert TAG
find CG
find C
insert A
find TAT
find C
find CGG
insert G
find ACG
insert TGT
insert G
insert C
find AA
find T
insert CG
insert T
insert GC
find C
insert CT
find AT
find CTG
find G
find T
find G
insert A
find CT
find AGT
insert T
find AGG
find AGG
insert G
insert C
find AAT
insert CG
find A
insert AT
insert TAG
insert TA
find TT
find CG
find CC
find GTC
insert ACG
insert CC
insert G
find CTC
insert TCT
insert A
insert AG
insert CAA
find TT
insert G
find T
find ATA
insert G
insert GT
find G
find AAA
find GT
find AA
find A
insert TTA
find AAG
insert TT
"""
sys.stdin = io.StringIO(_INPUT)

m = 1046527
T = [ 0 for _ in range(10000000)]

def strToInt(word):
    ans = ""
    for item in range(len(word)):
        if(word[item]=="A"):
            ans += "1"
        elif(word[item]=="C"):
            ans += "2"
        elif(word[item]=="G"):
            ans += "3"
        elif(word[item]=="T"):
            ans += "4"
    return int(ans)

def h1(key):
    global m
    return key%m

def h2(key):
    global m
    return 1 + (key % (m-1) )

def h(key, i):
    global m
    return (h1(key) + i*h2(key))%m

def insert(T,key):
    i = 0
    while(True):
        j = h(key, i)
        if(T[j] == 0 or T[j] == key):
            T[j] = key
            return j
        else:
            i = i+1

def search(T, key):
    i = 0
    while(True):
        j = h(key, i)
        if(T[j]==key):
            return True
        elif(T[j] == 0, i>=m):
            return False
        else:
            i = i+1

def main():
    n = int(input())
    for i in range(n):
        cmd, word = map(str, input().split())
        intWord = strToInt(word)
        if(cmd=="insert"):
            insert(T, intWord)
        else:
            if(search(T, intWord)):
                print("yes")
            else:
                print("no")

main()
