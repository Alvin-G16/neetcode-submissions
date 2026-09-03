class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] = seen[num] + 1
            else:
                seen[num] = 0

        sortedDict = sorted(seen.items(), key=lambda x: x[1], reverse=True)

        out = []
        for i in range(k):
            freqItem = sortedDict[i][0]
            out.append(freqItem)
        return out
        