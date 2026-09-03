class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for i in strs:
            sortedStr = "".join(sorted(i))
            if sortedStr in seen:
                seen[sortedStr].append(i)
            else:
                seen[sortedStr] = [i]
        return list(seen.values())