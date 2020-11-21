import io
import sys

_INPUT = """\
_/\//
"""
sys.stdin = io.StringIO(_INPUT)

# a = list(repr(input()))
# print(a)
# for item in a:
#     print(item)

def main():
    A = list(repr(input()))
    # print(A)
    n = -1
    L = []
    deep = 0

    for item in A:
        # if(item != "'"):
        #     print("deep:{0}, item:{1}",format(deep,item))
        
        if(item=='\\'):
            if(deep==0):
                n += 1
                L.append(0)
            L[n] += deep + 0.5 
            deep += 1
            # print("plus deep")
        elif(item=="/"):
            if(deep>0):
                deep -= 1
                L[n] += deep + 0.5
        elif(item=="_"):
            if(deep != 0):
                L[n] += deep
        print(deep)
        print(L)
    L = [int(x) for x in L ]
    print(sum(L))
    a = " ".join(map(str,L))
    print("{0} {1}".format(n+1, a))

main()