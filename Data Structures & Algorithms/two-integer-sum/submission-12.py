class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in seen:
                if seen[d] > i:
                    return [i, seen[d]]
                return [seen[d], i]
            seen[nums[i]] = i