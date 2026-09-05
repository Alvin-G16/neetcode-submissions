class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        listSet = set(nums)
        longest = 0

        for i in listSet:
            if (i - 1) not in listSet:
                length = 1

                while (i + length) in listSet:
                    length += 1

                longest  = max(longest, length)

        return longest
