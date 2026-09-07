class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        uniqueTriplets = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                    continue
                if nums[l] + nums[r] < target:
                    l += 1
                    continue
                if nums[l] + nums[r] == target:
                    uniqueTriplets.add((-target, nums[l], nums[r]))
                    l += 1
        output = [list(triplet) for triplet in uniqueTriplets]
        return output
        