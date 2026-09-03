import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = seen[num] + 1
            else:
                seen[num] = 0

        NfreqFirst = [[-freq, num] for num, freq in seen.items()]
        heapq.heapify(NfreqFirst)

        out = []
        for i in range(k):
            item = heapq.heappop(NfreqFirst)
            out.append(item[1])
        return out

        