import io
import sys

_INPUT = """\
5 100
p1 150
p2 80
p3 200
p4 350
p5 20
"""
sys.stdin = io.StringIO(_INPUT)

n,q = map(int,input().split())
order = {}
for i in range(n):
    tmp = input().split()
    order[tmp[0]] = int(tmp[1])

finishTime = {}
time = 0

def process(order, q):
    global time
    finish = []
    for item in order:
        if(q>=order[item]):
            finish.append(item)
            time += order[item]
            finishTime[item] = time
        else:
            time += q
            order[item] -= q
    for item in finish:
        order.pop(item)

while(order!={}):
    process(order, q)

for item in finishTime:
    print("{0} {1}".format(item, finishTime[item]))


