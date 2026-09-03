class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            d = target - nums[i]
            if d in nums and i != nums.index(d):
                if nums.index(d) > i:
                    return [i, nums.index(d)]
                return [nums.index(d), i]
