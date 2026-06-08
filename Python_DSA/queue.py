import heapq

heap = []

heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,5)

print(heap)

print(heapq.heappop(heap))