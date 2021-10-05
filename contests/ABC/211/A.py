import io
import sys
_INPUT = """\
123 123


"""
sys.stdin = io.StringIO(_INPUT)


a,b = map(int, input().split())

print((a-b)/3 + b)