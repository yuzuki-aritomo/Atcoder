import heapq


H = []
heapq.heapify(H)

heapq.heappush(H, (0, 1))
heapq.heappush(H, (4, 3))
heapq.heappush(H, (3, 3))
heapq.heappush(H, (1, 1))
heapq.heappush(H, (1, 3))
heapq.heappush(H, (1, 2))

while(len(H)>0):
  print(heapq.heappop(H))

print(H)