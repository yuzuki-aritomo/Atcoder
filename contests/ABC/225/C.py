import io
import sys
_INPUT = """\
10 4
1346 1347 1348 1349
1353 1354 1355 1356
1360 1361 1362 1363
1367 1368 1369 1370
1374 1375 1376 1377
1381 1382 1383 1384
1388 1389 1390 1391
1395 1396 1397 1398
1402 1403 1404 1405
1409 1410 1411 1412

"""
sys.stdin = io.StringIO(_INPUT)

N, M = map(int, input().split())
A = []
for i in range(N):
  A.append(list(map(int,input().split())))

for i in range(N):
  if(A[i][0] != A[0][0]+i*7):
    print("No")
    exit()

# tmp = A[0][0]%7
flag = False
for i in range(N):
  flag = False
  for j in range(M):
    tmp = A[i][j]%7
    if flag:
      print("No")
      exit()
    if( tmp == 0):
      flag = True
    if( A[i][j] != A[i][0]+j):
      print("No")
      exit()

print("Yes")

