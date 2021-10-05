import io
import sys
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)


import time

s = time.time()
path =[0] * (1000000)
print(s- time.time())

s = time.time()
path =[0 for _ in range(1000000)]
print(s - time.time())