import io
import sys

_INPUT = """\
9
insert 5
insert 2
insert 3
insert 1
delete 3
insert 6
delete 5
deleteFirst
deleteLast
"""
sys.stdin = io.StringIO(_INPUT)

from collections import deque

def main():
    n = int(input())
    ans = deque()
    # ans = []
    for item in range(n):
        order = input().split()
        # print(ans)
        # print(order[0])
        if(order[0]=="insert"):
            ans.appendleft(order[1])
            # print("------")
        elif(order[0]=="delete"):
            try:
                ans.remove(order[1])
            except:
                a = 0
        elif(order[0]=="deleteFirst"):
            ans.popleft()
        elif(order[0]=="deleteLast"):
            ans.pop()
    print(" ".join(map(str,ans)))

# def main2():
#     n = int(input())
#     ans = ["*"]*n
#     delete = 0
#     dele_n = 0
#     for item in range(n):
#         order = input().split()
#         # print(" ".join(map(str,ans[:(n-2*delete)][::-1])))
#         if(order[0]=="insert"):
#             ans[item-2*delete - dele_n] = order[1]
#         elif(order[0]=="delete"):
#             if order[1] in ans:
#                 ans = ans[::-1]
#                 ans.remove(order[1])
#                 delete += 1
#                 ans = ans[::-1]
#             else:
#                 dele_n += 1
#         elif(order[0]=="deleteFirst"):
#             del ans[item-2*delete -dele_n -1]
#             delete += 1
#         elif(order[0]=="deleteLast"):
#             del ans[0]
#             delete += 1
#     print(" ".join(map(str,ans[:(n-2*delete -dele_n)][::-1])))

main()

# b = [4,5,6,4]
# b = b[::-1]
# b.remove(4)
# b = b[::-1]
# print(b)

