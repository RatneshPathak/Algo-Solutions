from typing import List
from sortedcontainers import SortedList
from heapq import heappush, heappop

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = SortedList(range(k))
        busy = []
        count = [0] * k

        for i, (t, d) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= t:
                _, s = heappop(busy)
                available.add(s)

            if not available:
                continue

            j = available.bisect_left(i % k)
            s = available[j] if j < len(available) else available[0]
            available.remove(s)
            count[s] += 1
            heappush(busy, (t + d, s))

        mx = max(count)
        return [i for i, c in enumerate(count) if c == mx]